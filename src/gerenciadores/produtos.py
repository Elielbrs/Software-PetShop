"""
Gerenciador de Produtos - Funções CRUD para Produtos
"""

from src.models import Produto


def cadastrar_produto():
    """Função para cadastrar um novo produto"""
    print("\n=== Cadastrar Novo Produto ===")
    nome = input("Nome do Produto: ")
    descricao = input("Descrição: ")
    preco = input("Preço: ")
    quantidade_estoque = input("Quantidade em Estoque: ")

    produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade_estoque=quantidade_estoque)
    produto.salvar()


def atualizar_produto():
    """Função para atualizar um produto existente"""
    print("\n=== Atualizar Produto ===")
    id_produto = input("ID do produto a ser atualizado: ")
    
    produto = Produto(id=id_produto)
    if produto.id is None:
        print(f"✗ Produto ID {id_produto} não encontrado.")
        return
    nome = input(f"Novo nome (atual: {produto.nome}): ") or produto.nome
    descricao = input(f"Nova descrição (atual: {produto.descricao}): ") or produto.descricao
    preco = input(f"Novo preço (atual: {produto.preco}): ") or produto.preco
    quantidade_estoque = input(f"Nova quantidade em estoque (atual: {produto.quantidade_estoque}): ") or produto.quantidade_estoque
    produto.nome = nome
    produto.descricao = descricao
    produto.preco = preco
    produto.quantidade_estoque = quantidade_estoque
    produto.atualizar()


def deletar_produto():
    """Função para deletar um produto"""
    print("\n=== Deletar Produto ===")
    id_produto = input("ID do produto a ser deletado: ")
    
    produto = Produto(id=id_produto)
    if produto.id is None:
        print(f"✗ Produto ID {id_produto} não encontrado.")
        return
    confirmacao = input(f"Tem certeza que deseja deletar o produto '{produto.nome}'? (s/n): ")
    if confirmacao.lower() == 's':
        produto.deletar()
    else:
        print("Operação cancelada.")


def listar_produtos():
    """Função para listar todos os produtos"""
    print("\n=== Listar Todos os Produtos ===")
    produtos = Produto.listar_todos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Descrição: {produto[2]}, Preço: {produto[3]}, Estoque: {produto[4]}")
    else:
        print("✗ Nenhum produto encontrado.")


def consultar_produto_por_id():
    """Função para consultar um produto por ID"""
    print("\n=== Consultar Produto por ID ===")
    id_produto = input("ID do produto a ser consultado: ")
    
    produto = Produto.consultar_por_id(id_produto)
    if produto:
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Descrição: {produto.descricao}")
        print(f"Preço: {produto.preco}")
        print(f"Estoque: {produto.quantidade_estoque}")
    else:
        print(f"✗ Produto ID {id_produto} não encontrado.")


def gerenciar_produtos():
    """Função para gerenciar produtos"""
    while True:
        print("\n=== Gerenciamento de Produtos ===")
        print("1. Cadastrar Produto")
        print("2. Atualizar Produto")
        print("3. Deletar Produto")
        print("4. Consultar Produto por ID")
        print("5. Listar Todos os Produtos")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            atualizar_produto()
        elif escolha == '3':
            deletar_produto()
        elif escolha == '4':
            consultar_produto_por_id()
        elif escolha == '5':
            listar_produtos()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
