from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import pandas as pd

# arquivo com os CNPJs para criar a lista de CNPJs e montar a URL
df = pd.read_excel('data/output/bases-separadas/-7.xlsx')

# lista de CNPJS
cnpj_lista = ['29614931000161', '50864554000105'] # lista teste
# cnpj_lista = df['cnpj'].values.tolist() # lista final

# acessar o site por uma lista de URLS 
for i in list(cnpj_lista):
    driver = webdriver.Chrome()
    url = f"https://cnpj.biz/{i}"
    driver.get(url)

# extrair os dados de cnpj e cnae

# criar planilha no excel


# inserir os dados na planilha
