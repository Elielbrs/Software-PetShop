"""
Modelo de Serviço
"""
from .base import EntidadeBase
from .database import Database


class Servico(EntidadeBase):
    """Classe para gerenciar serviços"""
    
    def __init__(self, id=None, nome_servico=None, preco=None):
        super().__init__(id)
        self.nome_servico = nome_servico
        self.preco = preco
    
    def salvar(self):
        """Insere um novo serviço no banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO servicos (nome_servico, preco) VALUES (?, ?)",
                (self.nome_servico, self.preco)
            )
            conn.commit()
            self.id = cursor.lastrowid
            print(f"✓ Serviço '{self.nome_servico}' cadastrado com sucesso! ID: {self.id}")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao cadastrar serviço: {e}")
    
    def atualizar(self):
        """Atualiza os dados do serviço"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE servicos SET nome_servico = ?, preco = ? WHERE id = ?",
                (self.nome_servico, self.preco, self.id)
            )
            conn.commit()
            print(f"✓ Serviço ID {self.id} atualizado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao atualizar serviço: {e}")
    
    def deletar(self):
        """Deleta o serviço do banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM servicos WHERE id = ?", (self.id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"✗ Serviço ID {self.id} não encontrado.")
            else:
                print(f"✓ Serviço ID {self.id} deletado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao deletar serviço: {e}")
    
    @staticmethod
    def consultar_todos():
        """Retorna todos os serviços"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome_servico, preco FROM servicos ORDER BY nome_servico")
            servicos = cursor.fetchall()
            
            print("\n" + "="*60)
            print("LISTA DE SERVIÇOS".center(60))
            print("="*60)
            for servico in servicos:
                print(f"ID: {servico[0]:<3} | Serviço: {servico[1]:<35} | Preço: R${servico[2]:.2f}")
            print("="*60 + "\n")
            
            conn.close()
            return servicos
        except Exception as e:
            print(f"✗ Erro ao consultar serviços: {e}")
            return []
