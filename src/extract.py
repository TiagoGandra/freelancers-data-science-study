import pandas as pd
from src.utils.decorators import handle_pandas_exceptions

@handle_pandas_exceptions
def extract_dataset(archive_path):
    """
        Load dataset and return a dataframe
    """
    df = pd.read_csv(archive_path)
    return df