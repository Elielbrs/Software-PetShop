"""
Modelo de Venda
"""
from datetime import datetime
from .base import EntidadeBase
from .database import Database


class Venda(EntidadeBase):
    """Classe para gerenciar vendas"""
    
    def __init__(self, id=None, id_produto=None, quantidade=None, preco_unitario=None, data_venda=None):
        super().__init__(id)
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.data_venda = data_venda or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def salvar(self):
        """Registra uma venda e atualiza o estoque"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            # Verifica o produto
            cursor.execute("SELECT nome, preco, quantidade_estoque FROM produtos WHERE id = ?", (self.id_produto,))
            produto = cursor.fetchone()
            
            if not produto:
                print(f"✗ Produto ID {self.id_produto} não encontrado.")
                conn.close()
                return
            
            nome_produto, preco, estoque = produto
            
            if self.quantidade > estoque:
                print(f"✗ Quantidade solicitada ({self.quantidade}) excede o estoque ({estoque}).")
                conn.close()
                return
            
            # Registra a venda
            cursor.execute(
                "INSERT INTO vendas (id_produto, quantidade, preco_unitario) VALUES (?, ?, ?)",
                (self.id_produto, self.quantidade, preco)
            )
            
            # Atualiza o estoque
            novo_estoque = estoque - self.quantidade
            cursor.execute("UPDATE produtos SET quantidade_estoque = ? WHERE id = ?", (novo_estoque, self.id_produto))
            
            conn.commit()
            self.id = cursor.lastrowid
            print(f"✓ Venda registrada! {self.quantidade}x '{nome_produto}' por R${preco:.2f} cada. "
                f"Estoque restante: {novo_estoque}")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao registrar venda: {e}")
    
    def atualizar(self):
        """Atualização não é recomendada para vendas (use deletar + criar nova)"""
        print("⚠ Não é recomendado atualizar vendas. Delete e crie uma nova.")
    
    def deletar(self):
        """Deleta a venda do banco de dados e retorna o estoque"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            # Busca os dados da venda
            cursor.execute("SELECT id_produto, quantidade FROM vendas WHERE id = ?", (self.id,))
            venda = cursor.fetchone()
            
            if not venda:
                print(f"✗ Venda ID {self.id} não encontrada.")
                conn.close()
                return
            
            # Retorna o estoque
            id_produto, quantidade = venda
            cursor.execute("UPDATE produtos SET quantidade_estoque = quantidade_estoque + ? WHERE id = ?", 
                        (quantidade, id_produto))
            
            # Deleta a venda
            cursor.execute("DELETE FROM vendas WHERE id = ?", (self.id,))
            conn.commit()
            
            print(f"✓ Venda ID {self.id} deletada com sucesso! Estoque restaurado.")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao deletar venda: {e}")
    
    @staticmethod
    def consultar_todos():
        """Retorna todas as vendas"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT v.id, p.nome, v.quantidade, v.preco_unitario, 
                       (v.quantidade * v.preco_unitario) as total, v.data_venda
                FROM vendas v 
                JOIN produtos p ON v.id_produto = p.id 
                ORDER BY v.data_venda DESC
            """)
            vendas = cursor.fetchall()
            
            print("\n" + "="*110)
            print("HISTÓRICO DE VENDAS".center(110))
            print("="*110)
            total_geral = 0
            for venda in vendas:
                total_venda = venda[4]
                total_geral += total_venda
                print(f"ID: {venda[0]:<3} | Produto: {venda[1]:<25} | Qtd: {venda[2]:<4} | "
                    f"Preço Unit.: R${venda[3]:.2f} | Total: R${total_venda:.2f} | Data: {venda[5]}")
            print("-"*110)
            print(f"TOTAL GERAL: R${total_geral:.2f}".rjust(110))
            print("="*110 + "\n")
            
            conn.close()
            return vendas
        except Exception as e:
            print(f"✗ Erro ao consultar vendas: {e}")
            return []
