"""
Script de teste para verificar se a estrutura do projeto está funcionando
Execute este arquivo para testar as funcionalidades básicas
"""

from src.models import Database, Usuario, Pet, Servico, Agendamento, Produto, Venda
from src.utils import Relatorios, AlertaEstoque


def testar_projeto():
    """Executa testes básicos do projeto"""
    
    print("\n" + "="*80)
    print("INICIANDO TESTES DO SISTEMA PETSHOP".center(80))
    print("="*80 + "\n")
    
    # 1. Inicializar banco
    print("1️⃣ Testando inicialização do banco de dados...")
    Database.inicializar_banco()
    
    # 2. Testar Usuários
    print("\n2️⃣ Testando criação de usuários...")
    u1 = Usuario(nome="João Silva", email="joao@email.com", telefone="11999999999")
    u1.salvar()
    
    u2 = Usuario(nome="Maria Santos", email="maria@email.com", telefone="11988888888")
    u2.salvar()
    
    # 3. Consultar usuários
    print("\n3️⃣ Consultando usuários...")
    Usuario.consultar_todos()
    
    # 4. Testar Pets
    print("4️⃣ Testando criação de pets...")
    p1 = Pet(nome="Rex", especie="Cachorro", racao="Labrador", idade=3, dono_id=1)
    p1.salvar()
    
    p2 = Pet(nome="Whiskers", especie="Gato", racao="Persa", idade=2, dono_id=2)
    p2.salvar()
    
    # 5. Consultar pets com donos
    print("\n5️⃣ Consultando pets com informações dos donos...")
    Pet.consultar_todos()
    
    # 6. Testar Serviços
    print("6️⃣ Testando criação de serviços...")
    s1 = Servico(nome_servico="Banho", preco=50.00)
    s1.salvar()
    
    s2 = Servico(nome_servico="Tosa", preco=75.00)
    s2.salvar()
    
    # 7. Consultar serviços
    print("\n7️⃣ Consultando serviços...")
    Servico.consultar_todos()
    
    # 8. Testar Agendamentos
    print("8️⃣ Testando criação de agendamentos...")
    a1 = Agendamento(id_pet=1, id_servico=1, data_hora="2024-01-25 10:00:00", status="pendente")
    a1.salvar()
    
    # 9. Consultar agendamentos pendentes
    print("\n9️⃣ Consultando agendamentos pendentes...")
    Agendamento.consultar_pendentes()
    
    # 10. Testar Produtos
    print("🔟 Testando criação de produtos...")
    prod1 = Produto(nome="Ração Premium", descricao="Para cães adultos", preco=85.00, 
                    quantidade_estoque=50, estoque_minimo=10)
    prod1.salvar()
    
    prod2 = Produto(nome="Brinquedo de Corda", descricao="Brinquedo para cães", preco=25.00,
                    quantidade_estoque=3, estoque_minimo=5)
    prod2.salvar()
    
    # 11. Consultar produtos
    print("\n1️⃣1️⃣ Consultando produtos...")
    Produto.consultar_todos()
    
    # 12. Testar Vendas
    print("1️⃣2️⃣ Testando registro de vendas...")
    v1 = Venda(id_produto=1, quantidade=2, preco_unitario=85.00)
    v1.salvar()
    
    # 13. Consultar vendas
    print("\n1️⃣3️⃣ Consultando vendas...")
    Venda.consultar_todos()
    
    # 14. Testar alertas de estoque
    print("1️⃣4️⃣ Verificando alertas de estoque baixo...")
    AlertaEstoque.verificar_estoque()
    
    # 15. Testar relatórios
    print("1️⃣5️⃣ Gerando relatórios...")
    Relatorios.faturamento_diario()
    
    print("\n" + "="*80)
    print("✓ TODOS OS TESTES COMPLETADOS COM SUCESSO!".center(80))
    print("="*80 + "\n")
    
    print("📝 PRÓXIMOS PASSOS:")
    print("   - Integre este código com uma interface (GUI/Web)")
    print("   - Configure backups automáticos do banco de dados")
    print("   - Implemente autenticação de usuários")
    print("   - Crie dashboards de relatórios")
    print("\n")


if __name__ == "__main__":
    try:
        testar_projeto()
    except Exception as e:
        print(f"\n❌ ERRO DURANTE OS TESTES: {e}\n")
        import traceback
        traceback.print_exc()
