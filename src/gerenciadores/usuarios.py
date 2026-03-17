"""
Gerenciador de Usuários - Funções CRUD para Usuários
"""

from src.models import Usuario


def cadastrar_usuario():
    """Função para cadastrar um novo usuário"""
    print("\n=== Cadastrar Novo Usuário ===")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    usuario = Usuario(nome=nome, email=email, telefone=telefone)
    usuario.salvar()


def atualizar_usuario():
    """Função para atualizar um usuário existente"""
    print("\n=== Atualizar Usuário ===")
    id_usuario = input("ID do usuário a ser atualizado: ")
    
    usuario = Usuario(id=id_usuario)
    if usuario.id is None:
        print(f"✗ Usuário ID {id_usuario} não encontrado.")
        return
    nome = input(f"Novo nome (atual: {usuario.nome}): ") or usuario.nome
    email = input(f"Novo email (atual: {usuario.email}): ") or usuario.email
    telefone = input(f"Novo telefone (atual: {usuario.telefone}): ") or usuario.telefone
    usuario.nome = nome
    usuario.email = email
    usuario.telefone = telefone
    usuario.atualizar()


def deletar_usuario():
    """Função para deletar um usuário"""
    print("\n=== Deletar Usuário ===")
    id_usuario = input("ID do usuário a ser deletado: ")
    
    usuario = Usuario(id=id_usuario)
    if usuario.id is None:
        print(f"✗ Usuário ID {id_usuario} não encontrado.")
        return
    confirmacao = input(f"Tem certeza que deseja deletar o usuário '{usuario.nome}'? (s/n): ")
    if confirmacao.lower() == 's':
        usuario.deletar()
    else:
        print("Operação cancelada.")


def consultar_usuario_por_id():
    """Função para consultar um usuário por ID"""
    print("\n=== Consultar Usuário por ID ===")
    id_usuario = input("ID do usuário a ser consultado: ")
    
    usuario = Usuario.consultar_por_id(id_usuario)
    if usuario:
        print(f"ID: {usuario.id}")
        print(f"Nome: {usuario.nome}")
        print(f"Email: {usuario.email}")
        print(f"Telefone: {usuario.telefone}")
    else:
        print(f"✗ Usuário ID {id_usuario} não encontrado.")


def listar_usuarios():
    """Função para listar todos os usuários"""
    print("\n=== Listar Todos os Usuários ===")
    usuarios = Usuario.consultar_todos()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}")
    else:
        print("✗ Nenhum usuário encontrado.")


def gerenciar_usuarios():
    """Função para gerenciar usuários"""
    while True:
        print("\n=== Gerenciamento de Usuários ===")
        print("1. Cadastrar Usuário")
        print("2. Atualizar Usuário")
        print("3. Deletar Usuário")
        print("4. Consultar Usuário por ID")
        print("5. Listar Todos os Usuários")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            atualizar_usuario()
        elif escolha == '3':
            deletar_usuario()
        elif escolha == '4':
            consultar_usuario_por_id()
        elif escolha == '5':
            listar_usuarios()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
