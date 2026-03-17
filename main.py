"""
PetShop - Sistema de Gerenciamento de Loja de Animais
Arquivo principal (entry point)
"""

from src.models import Database
from src.gerenciadores.menu import opcoes_menu


def main():
    """Função principal da aplicação"""
    # Inicializa o banco de dados
    Database.inicializar_banco()
    print("✓ Banco de dados inicializado!\n")

    opcoes_menu()


if __name__ == "__main__":
    main()




