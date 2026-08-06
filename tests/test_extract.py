import pandas as pd
import pytest
from src.extract import extract_dataset

def test_arquivo_nao_encontrado(caplog):
    """
        Arquivo não encontrado passando o nome de um arquivo errado
    """
    #arrange
    caminho_falso = "dados/caminho_inventado.csv"

    #act e assert:
    with pytest.raises(FileNotFoundError):
        extract_dataset(caminho_falso)

    assert "Arquivo não encontrado" in caplog.text

def test_arquivo_vazio(tmp_path, caplog):
    """ Arquivo criado em pasta temporaria, vazio, deve retornar erro"""

    #arrange
    pasta_temporaria = tmp_path / "data"
    pasta_temporaria.mkdir()

    arquivo_vazio = pasta_temporaria / "vendas_vazio.csv"
    arquivo_vazio.touch()

    #act e assert
    with pytest.raises(pd.errors.EmptyDataError):
        extract_dataset(str(arquivo_vazio))

    assert "O arquivo foi encontrado, mas está vazio" in caplog.text