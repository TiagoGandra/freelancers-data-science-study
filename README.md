# Exercício de engenharia de dados

## Objetivo
Aquecer minha habilidade em engenharia de dados com um dataset do kaggle fictício com dados "raw".

## Tecnologia
**Linguagem**: Python
**Bibliotecas**: Pandas e sklearn

## Como rodar
- Clonar repositório
- Criar ambiente virtual isolado:
`python -m venv venv`
- Ativar ambiente:
`source venv/bin/activate`
- Instalar dependências:
`pip install requirements.txt`
- Rodar o programa: 
`python main.py`

## Como rodar os testes
- Comando para rodar os testes unitários: `pytest tests/ -v`

## Estrutura de pastas
```
└── 📁data
    └── 📁processed
    └── 📁raw
        ├── global_freelancers_raw.csv
        └── global-freelancers-raw-dataset.zip
└── 📁src
    └── 📁__pycache__
        ├── __init__.cpython-312.pyc
        ├── extract.cpython-312.pyc
    └── 📁utils
        └── 📁__pycache__
            ├── __init__.cpython-312.pyc
            ├── decorators.cpython-312.pyc
        ├── __init__.py
        ├── decorators.py
    ├── __init__.py
    ├── extract.py
    ├── load.py
    └── transform.py
└── 📁tests
    └── __init__.py
    ├── test_decorators.py
    └── test_extract.py
└── .gitignore
└── main.py
└── README.md
└── requirements.txt
```