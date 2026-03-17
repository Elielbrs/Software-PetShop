"""
Gerenciador de Serviços - Funções CRUD para Serviços
"""

from src.models import Servico


def cadastrar_servico():
    """Função para cadastrar um novo serviço"""
    print("\n=== Cadastrar Novo Serviço ===")
    nome = input("Nome do Serviço: ")
    descricao = input("Descrição: ")
    preco = input("Preço: ")

    servico = Servico(nome=nome, descricao=descricao, preco=preco)
    servico.salvar()


def atualizar_servico():
    """Função para atualizar um serviço existente"""
    print("\n=== Atualizar Serviço ===")
    id_servico = input("ID do serviço a ser atualizado: ")
    
    servico = Servico(id=id_servico)
    if servico.id is None:
        print(f"✗ Serviço ID {id_servico} não encontrado.")
        return
    nome = input(f"Novo nome (atual: {servico.nome}): ") or servico.nome
    descricao = input(f"Nova descrição (atual: {servico.descricao}): ") or servico.descricao
    preco = input(f"Novo preço (atual: {servico.preco}): ") or servico.preco
    servico.nome = nome
    servico.descricao = descricao
    servico.preco = preco
    servico.atualizar()


def deletar_servico():
    """Função para deletar um serviço"""
    print("\n=== Deletar Serviço ===")
    id_servico = input("ID do serviço a ser deletado: ")
    
    servico = Servico(id=id_servico)
    if servico.id is None:
        print(f"✗ Serviço ID {id_servico} não encontrado.")
        return
    confirmacao = input(f"Tem certeza que deseja deletar o serviço '{servico.nome}'? (s/n): ")
    if confirmacao.lower() == 's':
        servico.deletar()
    else:
        print("Operação cancelada.")


def consultar_servico_por_id():
    """Função para consultar um serviço por ID"""
    print("\n=== Consultar Serviço por ID ===")
    id_servico = input("ID do serviço a ser consultado: ")
    
    servico = Servico.consultar_por_id(id_servico)
    if servico:
        print(f"ID: {servico.id}")
        print(f"Nome: {servico.nome}")
        print(f"Descrição: {servico.descricao}")
        print(f"Preço: {servico.preco}")
    else:
        print(f"✗ Serviço ID {id_servico} não encontrado.")


def listar_servicos():
    """Função para listar todos os serviços"""
    print("\n=== Listar Todos os Serviços ===")
    servicos = Servico.listar_todos()
    if servicos:
        for servico in servicos:
            print(f"ID: {servico[0]}, Nome: {servico[1]}, Descrição: {servico[2]}, Preço: {servico[3]}")
    else:
        print("✗ Nenhum serviço encontrado.")


def gerenciar_servicos():
    """Função para gerenciar serviços"""
    while True:
        print("\n=== Gerenciamento de Serviços ===")
        print("1. Cadastrar Serviço")
        print("2. Atualizar Serviço")
        print("3. Deletar Serviço")
        print("4. Consultar Serviço por ID")
        print("5. Listar Todos os Serviços")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar_servico()
        elif escolha == '2':
            atualizar_servico()
        elif escolha == '3':
            deletar_servico()
        elif escolha == '4':
            consultar_servico_por_id()
        elif escolha == '5':
            listar_servicos()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
