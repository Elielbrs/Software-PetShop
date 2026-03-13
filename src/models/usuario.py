"""
Modelo de Usuário
"""
from .base import EntidadeBase
from .database import Database


class Usuario(EntidadeBase):
    """Classe para gerenciar usuários (donos de pets)"""
    
    def __init__(self, id=None, nome=None, email=None, telefone=None):
        super().__init__(id)
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def salvar(self):
        """Insere um novo usuário no banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)",
                (self.nome, self.email, self.telefone)
            )
            conn.commit()
            self.id = cursor.lastrowid
            print(f"✓ Usuário '{self.nome}' cadastrado com sucesso! ID: {self.id}")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao cadastrar usuário: {e}")
    
    def atualizar(self):
        """Atualiza os dados do usuário"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE usuarios SET nome = ?, email = ?, telefone = ? WHERE id = ?",
                (self.nome, self.email, self.telefone, self.id)
            )
            conn.commit()
            print(f"✓ Usuário ID {self.id} atualizado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao atualizar usuário: {e}")
    
    def deletar(self):
        """Deleta o usuário do banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (self.id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"✗ Usuário ID {self.id} não encontrado.")
            else:
                print(f"✓ Usuário ID {self.id} deletado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao deletar usuário: {e}")
    
    @staticmethod
    def consultar_todos():
        """Retorna todos os usuários com seus pets"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.id, u.nome, u.email, u.telefone, COUNT(p.id) as total_pets
                FROM usuarios u 
                LEFT JOIN pets p ON u.id = p.dono_id
                GROUP BY u.id
            """)
            usuarios = cursor.fetchall()
            
            print("\n" + "="*80)
            print("LISTA DE USUÁRIOS".center(80))
            print("="*80)
            for user in usuarios:
                print(f"ID: {user[0]} | Nome: {user[1]:<20} | Email: {user[2]:<25} | Telefone: {user[3]:<12} | Pets: {user[4]}")
            print("="*80 + "\n")
            
            conn.close()
            return usuarios
        except Exception as e:
            print(f"✗ Erro ao consultar usuários: {e}")
            return []
    
    @staticmethod
    def consultar_por_id(id):
        """Retorna um usuário específico"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, email, telefone FROM usuarios WHERE id = ?", (id,))
            usuario = cursor.fetchone()
            conn.close()
            if usuario:
                return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])
            else:
                print(f"✗ Usuário ID {id} não encontrado.")
                return None
        except Exception as e:
            print(f"✗ Erro ao buscar usuário: {e}")
            return None
