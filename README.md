# PetShop - Sistema de Gerenciamento

Sistema completo de gerenciamento para pet shops, desenvolvido em Python com SQLite3. Oferece funcionalidades para gerenciar usuários, pets, serviços, agendamentos, produtos e vendas.

## 📁 Estrutura do Projeto

```
PetShop/
├── main.py                          # Arquivo principal (entry point)
├── README.md                        # Este arquivo
├── requirements.txt                 # Dependências do projeto
├── data/                            # Dados (banco de dados)
│   └── pets.db                      # Arquivo SQLite
└── src/                             # Código-fonte da aplicação
    ├── __init__.py
    ├── config/                      # Configurações
    │   ├── __init__.py
    │   └── settings.py              # Variáveis de configuração
    ├── models/                      # Modelos de dados
    │   ├── __init__.py
    │   ├── base.py                  # Classe base abstrata (EntidadeBase)
    │   ├── database.py              # Gerenciamento do banco de dados
    │   ├── usuario.py               # Modelo de Usuário
    │   ├── pet.py                   # Modelo de Pet
    │   ├── servico.py               # Modelo de Serviço
    │   ├── agendamento.py           # Modelo de Agendamento
    │   ├── produto.py               # Modelo de Produto
    │   └── venda.py                 # Modelo de Venda
    └── utils/                       # Utilitários
        ├── __init__.py
        ├── relatorios.py            # Classe de Relatórios
        └── alertas.py               # Classe de Alertas de Estoque
```

## 🚀 Instalação

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes)

### Passos

1. **Clone ou obtenha o projeto**
```bash
cd PetShop
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute o programa**
```bash
python main.py
```

## 💾 Dependências

- **sqlite3**: Fornecido nativa com Python para gerenciamento de banco de dados
- **datetime**: Fornecido nativa com Python para manipulação de datas
- **abc**: Fornecido nativa com Python para classes abstratas

Todas as dependências são parte da biblioteca padrão do Python!

## 📚 Guia de Uso

### Importar Classes

```python
from src.models import Database, Usuario, Pet, Servico, Agendamento, Produto, Venda
from src.utils import Relatorios, AlertaEstoque
```

### Inicializar o Banco de Dados

```python
Database.inicializar_banco()
```

### Criar um Usuário

```python
usuario = Usuario(nome="João Silva", email="joao@email.com", telefone="11999999999")
usuario.salvar()
```

### Criar um Pet

```python
pet = Pet(nome="Rex", especie="Cachorro", racao="Raça", idade=3, dono_id=1)
pet.salvar()
```

### Consultar Pets com Informações do Dono

```python
pets = Pet.consultar_todos()
# Retorna todos os pets com nome, espécie, raça, idade e informações do dono
```

### Criar um Serviço

```python
servico = Servico(nome_servico="Banho", preco=50.00)
servico.salvar()
```

### Agendar um Serviço

```python
agendamento = Agendamento(
    id_pet=1, 
    id_servico=1, 
    data_hora="2024-01-20 14:30:00",
    status="pendente"
)
agendamento.salvar()
```

### Consultar Agendamentos Pendentes

```python
agendamentos = Agendamento.consultar_pendentes()
```

### Criar um Produto

```python
produto = Produto(
    nome="Ração Premium",
    descricao="Ração para cães adultos",
    preco=85.00,
    quantidade_estoque=50,
    estoque_minimo=10
)
produto.salvar()
```

### Registrar uma Venda

```python
venda = Venda(id_produto=1, quantidade=2, preco_unitario=85.00)
venda.salvar()
# Automaticamente deduz do estoque!
```

### Gerar Relatórios

```python
# Faturamento do dia
Relatorios.faturamento_diario()

# Faturamento do mês
Relatorios.faturamento_mensal()

# Faturamento por serviço
Relatorios.faturamento_por_servico()

# Faturamento por produto
Relatorios.faturamento_por_produto()

# Produto mais vendido
Relatorios.produto_mais_vendido()
```

### Verificar Alertas de Estoque

```python
AlertaEstoque.verificar_estoque()
# Exibe produtos com estoque abaixo do mínimo
```

## 🏗️ Arquitetura

### Padrão OOP com Herança

Todas as classes de modelo (`Usuario`, `Pet`, `Servico`, `Agendamento`, `Produto`, `Venda`) herdam de `EntidadeBase`, uma classe abstrata que define a interface CRUD:

```python
class EntidadeBase(ABC):
    @abstractmethod
    def salvar(self): pass
    
    @abstractmethod
    def atualizar(self): pass
    
    @abstractmethod
    def deletar(self): pass
```

### Gerenciamento Centralizado de Banco de Dados

A classe `Database` gerencia toda a conexão e schema:

- `Database.get_connection()` - Retorna conexão SQLite
- `Database.inicializar_banco()` - Cria todas as tabelas

### Configuração Centralizada

O arquivo `settings.py` define:
- `BASE_DIR` - Diretório base do projeto
- `DATA_DIR` - Diretório de dados
- `DATABASE_PATH` - Caminho completo do banco de dados

## 📊 Banco de Dados (Schema)

### Tabela: usuarios
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT
)
```

### Tabela: pets
```sql
CREATE TABLE pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especie TEXT NOT NULL,
    racao TEXT,
    idade INTEGER,
    dono_id INTEGER,
    FOREIGN KEY (dono_id) REFERENCES usuarios(id)
)
```

### Tabela: servicos
```sql
CREATE TABLE servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_servico TEXT NOT NULL,
    preco REAL NOT NULL
)
```

### Tabela: agendamentos
```sql
CREATE TABLE agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pet INTEGER,
    id_servico INTEGER,
    data_hora DATETIME NOT NULL,
    status TEXT DEFAULT 'pendente',
    FOREIGN KEY (id_pet) REFERENCES pets(id),
    FOREIGN KEY (id_servico) REFERENCES servicos(id)
)
```

### Tabela: produtos
```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    quantidade_estoque INTEGER NOT NULL,
    estoque_minimo INTEGER DEFAULT 5
)
```

### Tabela: vendas
```sql
CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
)
```

## 🎯 Funcionalidades Principais

✅ **Gerenciamento de Usuários** - Criar, atualizar, deletar e consultar clientes  
✅ **Gerenciamento de Pets** - Associar pets aos donos com informações completas  
✅ **Serviços** - Cadastrar ofertas de serviços com preços  
✅ **Agendamentos** - Agendar serviços com status de acompanhamento  
✅ **Produtos** - Gerenciar inventário com controle de estoque  
✅ **Vendas** - Registrar vendas com atualização automática de estoque  
✅ **Relatórios** - Consultas de faturamento diário, mensal, por serviço e produto  
✅ **Alertas** - Notificações de produtos com estoque baixo  

## 🔍 Estrutura de Métodos

### Métodos CRUD Básicos
Todos os modelos implementam:
- `salvar()` - Insere novo registro
- `atualizar()` - Modifica registro existente
- `deletar()` - Remove registro

### Métodos de Consulta
- `consultar_todos()` - Retorna todos os registros (com JOINs quando apropriado)
- `consultar_por_id(id)` - Retorna um registro específico

### Métodos Especiais
- `Agendamento.consultar_pendentes()` - Apenas agendamentos com status 'pendente'
- `Venda.salvar()` - Declara estoque automaticamente
- `Venda.deletar()` - Restaura estoque automaticamente

## 📝 Exemplos Prácticos

### Fluxo Completo de Uso

```python
from src.models import Database, Usuario, Pet, Servico, Agendamento, Produto, Venda
from src.utils import Relatorios, AlertaEstoque

# 1. Inicializar
Database.inicializar_banco()

# 2. Criar usuário
usuario = Usuario(nome="Maria Silva", email="maria@email.com", telefone="11988888888")
usuario.salvar()

# 3. Criar pet
pet = Pet(nome="Spike", especie="Cachorro", racao="PitBull", idade=2, dono_id=1)
pet.salvar()

# 4. Criar serviço
servico = Servico(nome_servico="Tosa", preco=75.00)
servico.salvar()

# 5. Agendar
agendamento = Agendamento(id_pet=1, id_servico=1, data_hora="2024-01-25 10:00:00")
agendamento.salvar()

# 6. Criar produto
produto = Produto(nome="Shampoo Premium", descricao="Para cães", preco=45.00, quantidade_estoque=20)
produto.salvar()

# 7. Vender
venda = Venda(id_produto=1, quantidade=1, preco_unitario=45.00)
venda.salvar()

# 8. Consultar
Pet.consultar_todos()
Agendamento.consultar_pendentes()
Produto.consultar_todos()

# 9. Relatórios
Relatorios.faturamento_diario()
AlertaEstoque.verificar_estoque()
```

## 🤝 Contribuições

Para melhorias futuras:
- [ ] Interface gráfica (tkinter/PyQt)
- [ ] API REST (Flask/FastAPI)
- [ ] Autenticação de usuários
- [ ] Backup automático de banco de dados
- [ ] Notificações e lembretes
- [ ] Integração com WhatsApp/Email

## 📄 Licença

Este projeto é fornecido como-está para fins educacionais e comerciais.

---

**Desenvolvido com ❤️ em Python**
