"""
Gerenciamento de banco de dados
"""
import sqlite3
from ..config.settings import DATABASE_PATH


class Database:
    """Classe para gerenciar conexões com o banco de dados"""
    
    _db_path = DATABASE_PATH
    
    @staticmethod
    def get_connection():
        """Retorna uma conexão com o banco de dados"""
        return sqlite3.connect(Database._db_path)
    
    @staticmethod
    def inicializar_banco():
        """Inicializa todas as tabelas no banco de dados"""
        conn = Database.get_connection()
        cursor = conn.cursor()
        
        # Tabela Usuários
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT
        )''')
        
        # Tabela Pets
        cursor.execute('''CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            racao TEXT,
            idade INTEGER,
            dono_id INTEGER,
            FOREIGN KEY (dono_id) REFERENCES usuarios(id)
        )''')
        
        # Tabela Serviços
        cursor.execute('''CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_servico TEXT NOT NULL,
            preco REAL NOT NULL
        )''')
        
        # Tabela Agendamentos
        cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pet INTEGER,
            id_servico INTEGER,
            data_hora DATETIME NOT NULL,
            status TEXT DEFAULT 'pendente',
            FOREIGN KEY (id_pet) REFERENCES pets(id),
            FOREIGN KEY (id_servico) REFERENCES servicos(id)
        )''')
        
        # Tabela Produtos
        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade_estoque INTEGER NOT NULL,
            estoque_minimo INTEGER DEFAULT 5
        )''')
        
        # Tabela Vendas
        cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_produto) REFERENCES produtos(id)
        )''')
        
        conn.commit()
        conn.close()
