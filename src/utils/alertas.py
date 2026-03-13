"""
Classe de Alertas
"""
from ..models.database import Database


class AlertaEstoque:
    """Classe para alertar sobre produtos com estoque baixo"""
    
    @staticmethod
    def verificar_estoque():
        """Verifica produtos com estoque abaixo do mínimo"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, quantidade_estoque, estoque_minimo FROM produtos WHERE quantidade_estoque <= estoque_minimo")
            produtos_baixo_estoque = cursor.fetchall()
            
            if produtos_baixo_estoque:
                print("\n" + "="*80)
                print("ALERTA DE ESTOQUE BAIXO".center(80))
                print("="*80)
                for prod in produtos_baixo_estoque:
                    print(f"ID: {prod[0]:<3} | Produto: {prod[1]:<30} | Estoque: {prod[2]:<4} | Mínimo: {prod[3]}")
                print("="*80 + "\n")
            else:
                print("\n✓ Todos os produtos estão com estoque adequado.\n")
            
            conn.close()
            return produtos_baixo_estoque
        except Exception as e:
            print(f"✗ Erro ao verificar estoque: {e}")
            return []
