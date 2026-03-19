"""
Menu Principal - Gerenciador de Menu
"""

from src.utils import Relatorios, AlertaEstoque
from src.gerenciadores.usuarios import gerenciar_usuarios
from src.gerenciadores.pets import gerenciar_pets
from src.gerenciadores.servicos import gerenciar_servicos
from src.gerenciadores.agendamentos import gerenciar_agendamentos
from src.gerenciadores.produtos import gerenciar_produtos


def opcoes_menu():
    """Exibe as opções do menu principal"""
    while True:
        print("\n" + "="*50)
        print("🐾 PETSHOP - SISTEMA DE GERENCIAMENTO")
        print("="*50)
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Pets")
        print("3. Gerenciar Serviços")
        print("4. Gerenciar Agendamentos")
        print("5. Gerenciar Produtos")
        print("6. Gerenciar Vendas")
        print("7. Relatórios")
        print("8. Alertas de Estoque")
        print("0. Sair")
        print("="*50)

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            gerenciar_usuarios()
        elif escolha == '2':
            gerenciar_pets()
        elif escolha == '3':
            gerenciar_servicos()
        elif escolha == '4':
            gerenciar_agendamentos()
        elif escolha == '5':
            gerenciar_produtos()
        elif escolha == '6':
            print("\n⚠️  Módulo de Vendas em desenvolvimento...")
        elif escolha == '7':
            Relatorios.gerar_relatorio_excel()
        elif escolha == '8':
            AlertaEstoque.verificar_estoque()
        elif escolha == '0':
            print("\n👋 Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")
