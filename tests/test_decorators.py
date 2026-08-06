import pytest
import pandas as pd
from src.utils.decorators import handle_pandas_exceptions

def test_decorator_exceptions_arquivo_nao_encontrado(caplog):
    """Retorna mensagem de erro para arquivos não encontrados"""
    #arrange
    @handle_pandas_exceptions
    def dummy_function():
        raise FileNotFoundError("Erro simulado")

    #act e assert
    with pytest.raises(FileNotFoundError):
        dummy_function()

    assert "Arquivo não encontrado" in caplog.text

def test_decorator_exceptions_arquivo_vazio(caplog):
    """Retorna mensagem de erro para arquivos vazios"""

    @handle_pandas_exceptions
    def dummy_function_vazia():
        raise pd.errors.EmptyDataError("Erro simulado vazio")

    with pytest.raises(pd.errors.EmptyDataError):
        dummy_function_vazia()

    assert "O arquivo foi encontrado, mas está vazio" in caplog.text

def test_decorator_exceptions_nao_deve_interferir_em_funcoes_bem_sucedidas():
    """Garante que o decorator é invisível quando não há erros."""
    
    @handle_pandas_exceptions
    def dummy_function_sucesso():
        return "dados simulados"
        
    resultado = dummy_function_sucesso()
    
    assert resultado == "dados simulados"