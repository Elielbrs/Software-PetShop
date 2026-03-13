"""
Modelo de Produto
"""
from .base import EntidadeBase
from .database import Database


class Produto(EntidadeBase):
    """Classe para gerenciar produtos"""
    
    def __init__(self, id=None, nome=None, descricao=None, preco=None, quantidade_estoque=None, estoque_minimo=5):
        super().__init__(id)
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.estoque_minimo = estoque_minimo
    
    def salvar(self):
        """Insere um novo produto no banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO produtos (nome, descricao, preco, quantidade_estoque, estoque_minimo) VALUES (?, ?, ?, ?, ?)",
                (self.nome, self.descricao, self.preco, self.quantidade_estoque, self.estoque_minimo)
            )
            conn.commit()
            self.id = cursor.lastrowid
            print(f"✓ Produto '{self.nome}' cadastrado com sucesso! ID: {self.id}")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao cadastrar produto: {e}")
    
    def atualizar(self):
        """Atualiza os dados do produto"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE produtos SET nome = ?, descricao = ?, preco = ?, quantidade_estoque = ?, estoque_minimo = ? WHERE id = ?",
                (self.nome, self.descricao, self.preco, self.quantidade_estoque, self.estoque_minimo, self.id)
            )
            conn.commit()
            print(f"✓ Produto ID {self.id} atualizado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao atualizar produto: {e}")
    
    def deletar(self):
        """Deleta o produto do banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (self.id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"✗ Produto ID {self.id} não encontrado.")
            else:
                print(f"✓ Produto ID {self.id} deletado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao deletar produto: {e}")
    
    @staticmethod
    def consultar_todos():
        """Retorna todos os produtos"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, descricao, preco, quantidade_estoque FROM produtos ORDER BY nome")
            produtos = cursor.fetchall()
            
            print("\n" + "="*110)
            print("LISTA DE PRODUTOS".center(110))
            print("="*110)
            for prod in produtos:
                status = "✓ EM ESTOQUE" if prod[4] > 0 else "✗ ESGOTADO"
                print(f"ID: {prod[0]:<3} | Nome: {prod[1]:<20} | Descrição: {prod[2]:<33} | "
                    f"Preço: R${prod[3]:.2f} | Qtd: {prod[4]:<4} ({status})")
            print("="*110 + "\n")
            
            conn.close()
            return produtos
        except Exception as e:
            print(f"✗ Erro ao consultar produtos: {e}")
            return []
