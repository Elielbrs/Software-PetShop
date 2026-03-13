"""
Modelo de Agendamento
"""
from .base import EntidadeBase
from .database import Database


class Agendamento(EntidadeBase):
    """Classe para gerenciar agendamentos"""
    
    def __init__(self, id=None, id_pet=None, id_servico=None, data_hora=None, status='pendente'):
        super().__init__(id)
        self.id_pet = id_pet
        self.id_servico = id_servico
        self.data_hora = data_hora
        self.status = status
    
    def salvar(self):
        """Insere um novo agendamento no banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO agendamentos (id_pet, id_servico, data_hora, status) VALUES (?, ?, ?, ?)",
                (self.id_pet, self.id_servico, self.data_hora, self.status)
            )
            conn.commit()
            self.id = cursor.lastrowid
            print(f"✓ Agendamento cadastrado com sucesso! ID: {self.id}")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao cadastrar agendamento: {e}")
    
    def atualizar(self):
        """Atualiza os dados do agendamento"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE agendamentos SET id_pet = ?, id_servico = ?, data_hora = ?, status = ? WHERE id = ?",
                (self.id_pet, self.id_servico, self.data_hora, self.status, self.id)
            )
            conn.commit()
            print(f"✓ Agendamento ID {self.id} atualizado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao atualizar agendamento: {e}")
    
    def deletar(self):
        """Deleta o agendamento do banco de dados"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM agendamentos WHERE id = ?", (self.id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"✗ Agendamento ID {self.id} não encontrado.")
            else:
                print(f"✓ Agendamento ID {self.id} deletado com sucesso!")
            conn.close()
        except Exception as e:
            print(f"✗ Erro ao deletar agendamento: {e}")
    
    @staticmethod
    def consultar_pendentes():
        """Retorna todos os agendamentos pendentes"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.id, a.status, p.nome, s.nome_servico, a.data_hora, u.nome
                FROM agendamentos a 
                JOIN pets p ON a.id_pet = p.id 
                JOIN servicos s ON a.id_servico = s.id
                JOIN usuarios u ON p.dono_id = u.id
                WHERE a.status = 'pendente'
                ORDER BY a.data_hora ASC
            """)
            agendamentos = cursor.fetchall()
            
            print("\n" + "="*100)
            print("AGENDAMENTOS PENDENTES".center(100))
            print("="*100)
            for agend in agendamentos:
                print(f"ID: {agend[0]:<3} | Status: {agend[1]:<10} | Pet: {agend[2]:<15} | "
                      f"Serviço: {agend[3]:<20} | Data/Hora: {agend[4]:<19} | Cliente: {agend[5]:<20}")
            print("="*100 + "\n")
            
            conn.close()
            return agendamentos
        except Exception as e:
            print(f"✗ Erro ao consultar agendamentos: {e}")
            return []
    
    @staticmethod
    def consultar_todos():
        """Retorna todos os agendamentos"""
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.id, a.status, p.nome, s.nome_servico, a.data_hora, u.nome
                FROM agendamentos a 
                JOIN pets p ON a.id_pet = p.id 
                JOIN servicos s ON a.id_servico = s.id
                JOIN usuarios u ON p.dono_id = u.id
                ORDER BY a.data_hora DESC
            """)
            agendamentos = cursor.fetchall()
            
            print("\n" + "="*100)
            print("TODOS OS AGENDAMENTOS".center(100))
            print("="*100)
            for agend in agendamentos:
                print(f"ID: {agend[0]:<3} | Status: {agend[1]:<10} | Pet: {agend[2]:<15} | "
                      f"Serviço: {agend[3]:<20} | Data/Hora: {agend[4]:<19} | Cliente: {agend[5]:<20}")
            print("="*100 + "\n")
            
            conn.close()
            return agendamentos
        except Exception as e:
            print(f"✗ Erro ao consultar agendamentos: {e}")
            return []
