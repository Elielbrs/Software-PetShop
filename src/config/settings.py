"""
Configurações gerais da aplicação
"""
import os

# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'pets.db')

# Banco de Dados
DATABASE_NAME = 'pets.db'
DATABASE_PATH = DB_PATH

# Criar diretório data se não existir
os.makedirs(DATA_DIR, exist_ok=True)
