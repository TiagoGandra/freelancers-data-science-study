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
Estrutura gerada com a extensão Draw Folder Structure do Krivoox no VSCODE
```
└── 📁data                                         # Repositório local de dados
    └── 📁processed
    └── 📁raw
        ├── global_freelancers_raw.csv
        └── global-freelancers-raw-dataset.zip
└── 📁src                                          # Módulos python
    └── 📁utils                                    # Funções utilitárias
        ├── decorators.py
    └── 📁etl                                      # Funções de ETL
        ├── __init__.py
        ├── extract.py
        ├── load.py
        └── transform.py
└── 📁tests                                        # Testes
    └── __init__.py
    ├── test_decorators.py
    └── test_extract.py
└── .gitignore
└── main.py                                         # Script principal
└── README.md
└── requirements.txt
```

## Referências 
[DATASET](https://www.kaggle.com/datasets/urvishahir/global-freelancers-raw-dataset?select=global_freelancers_raw.csv)