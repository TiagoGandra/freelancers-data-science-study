from src.etl.extract import extract_dataset
import pandas as pd

df_raw = extract_dataset("./data/raw/global_freelancers_raw.csv")
print(df_raw.head())