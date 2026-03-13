"""
Modelo de Pet
"""
from .base import EntidadeBase
from .database import Database
from .usuario import Usuario


class Pet(EntidadeBase):
    """Classe para gerenciar pets"""
    
    def __init__(self, id=None, nome=None, especie=None, racao=None, idade=None, dono_id=None):
        super().__init__(id)
        self.nome = nome
        self.especie = especie
        self.racao = racao
        self.idade = idade
        self.dono_id = dono_id
    
    def salvar(self):
        """Insere um novo pet no banco de dados"""
        try:
            if self.dono_id:
                dono = Usuario.consultar_por_id(self.dono_id)
                if not dono:
                    print(f"✗ Dono com ID {self.dono_id} não existe!")
                    return
            
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO pets (nome, especie, racao, idade, dono_id) VALUES (?, ?, ?, ?, ?)",
                (self.nome, self.especie, self.racao, self.idade, self.dono_id)
            )
            conn.commit()
            self.id = cursor.lastrowid
            print(f"✓ Pet '{self.nome}' cadastrado com sucesso! ID: {self.id}")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao cadastrar pet: {e}")
    
    def atualizar(self):
        """Atualiza os dados do pet"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE pets SET nome = ?, especie = ?, racao = ?, idade = ?, dono_id = ? WHERE id = ?",
                (self.nome, self.especie, self.racao, self.idade, self.dono_id, self.id)
            )
            conn.commit()
            print(f"✓ Pet ID {self.id} atualizado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao atualizar pet: {e}")
    
    def deletar(self):
        """Deleta o pet do banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pets WHERE id = ?", (self.id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"✗ Pet ID {self.id} não encontrado.")
            else:
                print(f"✓ Pet ID {self.id} deletado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao deletar pet: {e}")
    
    @staticmethod
    def consultar_todos():
        """Retorna todos os pets com informações de seus donos"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, p.nome, p.especie, p.racao, p.idade, 
                       u.id, u.nome, u.email, u.telefone
                FROM pets p 
                LEFT JOIN usuarios u ON p.dono_id = u.id
                ORDER BY p.nome
            """)
            pets = cursor.fetchall()
            
            print("\n" + "="*120)
            print("LISTA DE PETS".center(120))
            print("="*120)
            for pet in pets:
                dono_info = f"{pet[6]} ({pet[7]})" if pet[5] else "Não atribuído"
                print(f"ID: {pet[0]:<3} | Nome: {pet[1]:<15} | Espécie: {pet[2]:<12} | Raça: {pet[3]:<15} | "
                      f"Idade: {pet[4]:<4} anos | Dono: {dono_info:<40}")
            print("="*120 + "\n")
            
            conn.close()
            return pets
        except Exception as e:
            print(f"✗ Erro ao consultar pets: {e}")
            return []
    
    @staticmethod
    def consultar_por_id(id):
        """Retorna um pet específico"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, especie, racao, idade, dono_id FROM pets WHERE id = ?", (id,))
            pet = cursor.fetchone()
            conn.close()
            if pet:
                return Pet(pet[0], pet[1], pet[2], pet[3], pet[4], pet[5])
            else:
                print(f"✗ Pet ID {id} não encontrado.")
                return None
        except Exception as e:
            print(f"✗ Erro ao buscar pet: {e}")
            return None
