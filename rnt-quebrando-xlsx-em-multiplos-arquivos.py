import pandas as pd

df = pd.read_excel(
    './data/output/rnt-cnpj-com-cnae-dia-01-11-2023-hora-19-57-14-sem-cnae.xlsx', converters={'cnpj': str})

rows_per_file = 100

n_chunks = len(df) // rows_per_file

for i in range(n_chunks):
    start = i*rows_per_file
    stop = (i+1) * rows_per_file
    sub_df = df.iloc[start:stop]
    sub_df.to_excel(
        f"data\output\Bases-separadas\-{i}.xlsx", sheet_name='sheet1', index=False)
if stop < len(df):
    sub_df = df.iloc[stop:]
    sub_df.to_excel(
        f"data\output\Bases-separadas\-{i}.xlsx", sheet_name='sheet1', index=False)
