"""
Classe de Relatórios
"""
from datetime import datetime
from ..models.database import Database


class Relatorios:
    """Classe para gerar relatórios diversos"""
    
    @staticmethod
    def faturamento_diario():
        """Calcula o faturamento do dia"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            data_atual = datetime.now().strftime("%Y-%m-%d")
            
            cursor.execute("""
                SELECT SUM(s.preco) 
                FROM agendamentos a
                JOIN servicos s ON a.id_servico = s.id
                WHERE a.data_hora LIKE ? AND a.status = 'concluído'
            """, (f"{data_atual}%",))
            
            serviços = cursor.fetchone()[0] or 0.0
            
            cursor.execute("""
                SELECT SUM(v.quantidade * v.preco_unitario)
                FROM vendas v
                WHERE v.data_venda LIKE ?
            """, (f"{data_atual}%",))
            
            vendas = cursor.fetchone()[0] or 0.0
            total = serviços + vendas
            
            print("\n" + "="*60)
            print(f"FATURAMENTO DO DIA {data_atual}".center(60))
            print("="*60)
            print(f"Serviços: R${serviços:.2f}")
            print(f"Vendas:   R${vendas:.2f}")
            print("-"*60)
            print(f"TOTAL:    R${total:.2f}")
            print("="*60 + "\n")
            
            conn.close()
            return total
        except Exception as e:
            print(f"✗ Erro ao calcular faturamento diário: {e}")
            return 0.0
    
    @staticmethod
    def faturamento_mensal():
        """Calcula o faturamento do mês"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            mes_atual = datetime.now().strftime("%Y-%m")
            
            cursor.execute("""
                SELECT SUM(s.preco) 
                FROM agendamentos a
                JOIN servicos s ON a.id_servico = s.id
                WHERE a.data_hora LIKE ? AND a.status = 'concluído'
            """, (f"{mes_atual}%",))
            
            serviços = cursor.fetchone()[0] or 0.0
            
            cursor.execute("""
                SELECT SUM(v.quantidade * v.preco_unitario)
                FROM vendas v
                WHERE v.data_venda LIKE ?
            """, (f"{mes_atual}%",))
            
            vendas = cursor.fetchone()[0] or 0.0
            total = serviços + vendas
            
            print("\n" + "="*60)
            print(f"FATURAMENTO DO MÊS {mes_atual}".center(60))
            print("="*60)
            print(f"Serviços: R${serviços:.2f}")
            print(f"Vendas:   R${vendas:.2f}")
            print("-"*60)
            print(f"TOTAL:    R${total:.2f}")
            print("="*60 + "\n")
            
            conn.close()
            return total
        except Exception as e:
            print(f"✗ Erro ao calcular faturamento mensal: {e}")
            return 0.0
    
    @staticmethod
    def faturamento_por_servico():
        """Faturamento por serviço do mês"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            mes_atual = datetime.now().strftime("%Y-%m")
            
            cursor.execute("""
                SELECT s.nome_servico, COUNT(a.id) as total_servicos, SUM(s.preco) as faturamento
                FROM agendamentos a
                JOIN servicos s ON a.id_servico = s.id
                WHERE a.data_hora LIKE ? AND a.status = 'concluído'
                GROUP BY s.nome_servico
                ORDER BY faturamento DESC
            """, (f"{mes_atual}%",))
            
            resultados = cursor.fetchall()
            
            print("\n" + "="*70)
            print(f"FATURAMENTO POR SERVIÇO - {mes_atual}".center(70))
            print("="*70)
            for resultado in resultados:
                print(f"Serviço: {resultado[0]:<30} | Qtd: {resultado[1]:<4} | Faturamento: R${resultado[2]:.2f}")
            print("="*70 + "\n")
            
            conn.close()
            return resultados
        except Exception as e:
            print(f"✗ Erro ao calcular faturamento por serviço: {e}")
            return []
    
    @staticmethod
    def faturamento_por_produto():
        """Faturamento por produto do mês"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            mes_atual = datetime.now().strftime("%Y-%m")
            
            cursor.execute("""
                SELECT p.nome, SUM(v.quantidade) as total_vendido, SUM(v.quantidade * v.preco_unitario) as faturamento
                FROM vendas v
                JOIN produtos p ON v.id_produto = p.id
                WHERE v.data_venda LIKE ?
                GROUP BY p.nome
                ORDER BY faturamento DESC
            """, (f"{mes_atual}%",))
            
            resultados = cursor.fetchall()
            
            print("\n" + "="*70)
            print(f"FATURAMENTO POR PRODUTO - {mes_atual}".center(70))
            print("="*70)
            for resultado in resultados:
                print(f"Produto: {resultado[0]:<35} | Qtd: {resultado[1]:<5} | Faturamento: R${resultado[2]:.2f}")
            print("="*70 + "\n")
            
            conn.close()
            return resultados
        except Exception as e:
            print(f"✗ Erro ao calcular faturamento por produto: {e}")
            return []
    
    @staticmethod
    def produto_mais_vendido():
        """Produto mais vendido do mês"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            mes_atual = datetime.now().strftime("%Y-%m")
            
            cursor.execute("""
                SELECT p.nome, SUM(v.quantidade) as total
                FROM vendas v
                JOIN produtos p ON v.id_produto = p.id
                WHERE v.data_venda LIKE ?
                GROUP BY p.nome
                ORDER BY total DESC
                LIMIT 1
            """, (f"{mes_atual}%",))
            
            resultado = cursor.fetchone()
            
            if resultado:
                print(f"\n✓ Produto mais vendido em {mes_atual}: {resultado[0]} ({resultado[1]} unidades)\n")
            else:
                print(f"\n⚠ Nenhuma venda registrada em {mes_atual}\n")
            
            conn.close()
            return resultado
        except Exception as e:
            print(f"✗ Erro ao buscar produto mais vendido: {e}")
            return None
