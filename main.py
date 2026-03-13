"""
PetShop - Sistema de Gerenciamento de Loja de Animais
Arquivo principal (entry point)
"""

# Importa todas as classes do projeto
from src.models import (
    Database,
    Usuario,
    Pet,
    Servico,
    Agendamento,
    Produto,
    Venda
)
from src.utils import Relatorios, AlertaEstoque


def main():
    """Função principal da aplicação"""
    # Inicializa o banco de dados
    Database.inicializar_banco()
    print("✓ Banco de dados inicializado!\n")
    
    # Aqui você pode adicionar a lógica principal da aplicação
    # ou deixar disponíveis as classes para uso


if __name__ == "__main__":
    main()




