"""
Classe base abstrata para todas as entidades
"""
from abc import ABC, abstractmethod


class EntidadeBase(ABC):
    """Classe base abstrata para todas as entidades"""
    
    def __init__(self, id=None):
        self.id = id
    
    @abstractmethod
    def salvar(self):
        """Salva a entidade no banco de dados"""
        pass
    
    @abstractmethod
    def atualizar(self):
        """Atualiza a entidade no banco de dados"""
        pass
    
    @abstractmethod
    def deletar(self):
        """Deleta a entidade do banco de dados"""
        pass
