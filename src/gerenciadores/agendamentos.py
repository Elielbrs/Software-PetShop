"""
Gerenciador de Agendamentos - Funções CRUD para Agendamentos
"""

from src.models import Agendamento


def cadastrar_agendamento():
    """Função para cadastrar um novo agendamento"""
    print("\n=== Cadastrar Novo Agendamento ===")
    pet_id = input("ID do Pet: ")
    servico_id = input("ID do Serviço: ")
    data_hora = input("Data e Hora (YYYY-MM-DD HH:MM): ")

    agendamento = Agendamento(pet_id=pet_id, servico_id=servico_id, data_hora=data_hora)
    agendamento.salvar()


def atualizar_agendamento():
    """Função para atualizar um agendamento existente"""
    print("\n=== Atualizar Agendamento ===")
    id_agendamento = input("ID do agendamento a ser atualizado: ")
    
    agendamento = Agendamento(id=id_agendamento)
    if agendamento.id is None:
        print(f"✗ Agendamento ID {id_agendamento} não encontrado.")
        return
    pet_id = input(f"Novo ID do pet (atual: {agendamento.pet_id}): ") or agendamento.pet_id
    servico_id = input(f"Novo ID do serviço (atual: {agendamento.servico_id}): ") or agendamento.servico_id
    data_hora = input(f"Nova data e hora (atual: {agendamento.data_hora}): ") or agendamento.data_hora
    agendamento.pet_id = pet_id
    agendamento.servico_id = servico_id
    agendamento.data_hora = data_hora
    agendamento.atualizar()


def deletar_agendamento():
    """Função para deletar um agendamento"""
    print("\n=== Deletar Agendamento ===")
    id_agendamento = input("ID do agendamento a ser deletado: ")
    
    agendamento = Agendamento(id=id_agendamento)
    if agendamento.id is None:
        print(f"✗ Agendamento ID {id_agendamento} não encontrado.")
        return
    confirmacao = input(f"Tem certeza que deseja deletar o agendamento ID '{agendamento.id}'? (s/n): ")
    if confirmacao.lower() == 's':
        agendamento.deletar()
    else:
        print("Operação cancelada.")


def consultar_agendamento_por_id():
    """Função para consultar um agendamento por ID"""
    print("\n=== Consultar Agendamento por ID ===")
    id_agendamento = input("ID do agendamento a ser consultado: ")
    
    agendamento = Agendamento.consultar_por_id(id_agendamento)
    if agendamento:
        print(f"ID: {agendamento.id}")
        print(f"ID do Pet: {agendamento.pet_id}")
        print(f"ID do Serviço: {agendamento.servico_id}")
        print(f"Data e Hora: {agendamento.data_hora}")
    else:
        print(f"✗ Agendamento ID {id_agendamento} não encontrado.")


def listar_agendamentos():
    """Função para listar todos os agendamentos"""
    print("\n=== Listar Todos os Agendamentos ===")
    agendamentos = Agendamento.listar_todos()
    if agendamentos:
        for agendamento in agendamentos:
            print(f"ID: {agendamento[0]}, ID do Pet: {agendamento[1]}, ID do Serviço: {agendamento[2]}, Data e Hora: {agendamento[3]}")
    else:
        print("✗ Nenhum agendamento encontrado.")


def gerenciar_agendamentos():
    """Função para gerenciar agendamentos"""
    while True:
        print("\n=== Gerenciamento de Agendamentos ===")
        print("1. Cadastrar Agendamento")
        print("2. Atualizar Agendamento")
        print("3. Deletar Agendamento")
        print("4. Consultar Agendamento por ID")
        print("5. Listar Todos os Agendamentos")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar_agendamento()
        elif escolha == '2':
            atualizar_agendamento()
        elif escolha == '3':
            deletar_agendamento()
        elif escolha == '4':
            consultar_agendamento_por_id()
        elif escolha == '5':
            listar_agendamentos()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
