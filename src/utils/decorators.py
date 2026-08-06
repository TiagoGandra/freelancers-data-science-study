import pandas as pd
from functools import wraps
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s') # substitui o 'print'

def handle_pandas_exceptions(func):
    """
        Handler central para capturar erros de extração e transformação de dados
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            #tenta executar a função original
            return func(*args, **kwargs)

        #Múltiplas exceções mapeadas no handler:
        except FileNotFoundError as e:
            logging.error(f'Arquivo não encontrado no caminho fornecido: {e}')
            raise # repassa o erro para parar a pipeline

        except pd.errors.EmptyDataError:
            logging.error("O arquivo foi encontrado, mas está vazio.")
            raise

        except pd.errors.ParserError: 
            logging.error("Erro de formatação no arquivo (ex: colunas quebradas).")
            raise

        except Exception as e:
            logging.error(f"Erro inesperado durante a execução: {e}")
            raise

    return wrapper