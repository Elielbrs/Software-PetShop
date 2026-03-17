"""
Gerenciador de Pets - Funções CRUD para Pets
"""

from src.models import Pet


def cadastrar_pet():
    """Função para cadastrar um novo pet"""
    print("\n=== Cadastrar Novo Pet ===")
    nome = input("Nome do Pet: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    dono_id = input("ID do Dono (Usuário): ")

    pet = Pet(nome=nome, especie=especie, racao=raca, idade=idade, dono_id=dono_id)
    pet.salvar()


def atualizar_pet():
    """Função para atualizar um pet existente"""
    print("\n=== Atualizar Pet ===")
    id_pet = input("ID do pet a ser atualizado: ")
    
    pet = Pet(id=id_pet)
    if pet.id is None:
        print(f"✗ Pet ID {id_pet} não encontrado.")
        return
    nome = input(f"Novo nome (atual: {pet.nome}): ") or pet.nome
    especie = input(f"Nova espécie (atual: {pet.especie}): ") or pet.especie
    raca = input(f"Nova raça (atual: {pet.racao}): ") or pet.racao
    idade = input(f"Nova idade (atual: {pet.idade}): ") or pet.idade
    dono_id = input(f"Novo ID do dono (atual: {pet.dono_id}): ") or pet.dono_id
    pet.nome = nome
    pet.especie = especie
    pet.racao = raca
    pet.idade = idade
    pet.dono_id = dono_id
    pet.atualizar()


def deletar_pet():
    """Função para deletar um pet"""
    print("\n=== Deletar Pet ===")
    id_pet = input("ID do pet a ser deletado: ")
    
    pet = Pet(id=id_pet)
    if pet.id is None:
        print(f"✗ Pet ID {id_pet} não encontrado.")
        return
    confirmacao = input(f"Tem certeza que deseja deletar o pet '{pet.nome}'? (s/n): ")
    if confirmacao.lower() == 's':
        pet.deletar()
    else:
        print("Operação cancelada.")


def consultar_pet_por_id():
    """Função para consultar um pet por ID"""
    print("\n=== Consultar Pet por ID ===")
    id_pet = input("ID do pet a ser consultado: ")
    
    pet = Pet.consultar_por_id(id_pet)
    if pet:
        print(f"ID: {pet.id}")
        print(f"Nome: {pet.nome}")
        print(f"Espécie: {pet.especie}")
        print(f"Raça: {pet.racao}")
        print(f"Idade: {pet.idade}")
        print(f"ID do Dono (Usuário): {pet.dono_id}")
    else:
        print(f"✗ Pet ID {id_pet} não encontrado.")


def listar_pets():
    """Função para listar todos os pets"""
    print("\n=== Listar Todos os Pets ===")
    pets = Pet.consultar_todos()
    if pets:
        for pet in pets:
            print(f"ID: {pet[0]}, Nome: {pet[1]}, Espécie: {pet[2]}, Raça: {pet[3]}, Idade: {pet[4]}, ID do Dono: {pet[5]}")
    else:
        print("✗ Nenhum pet encontrado.")


def gerenciar_pets():
    """Função para gerenciar pets"""
    while True:
        print("\n=== Gerenciamento de Pets ===")
        print("1. Cadastrar Pet")
        print("2. Atualizar Pet")
        print("3. Deletar Pet")
        print("4. Consultar Pet por ID")
        print("5. Listar Todos os Pets")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar_pet()
        elif escolha == '2':
            atualizar_pet()
        elif escolha == '3':
            deletar_pet()
        elif escolha == '4':
            consultar_pet_por_id()
        elif escolha == '5':
            listar_pets()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
