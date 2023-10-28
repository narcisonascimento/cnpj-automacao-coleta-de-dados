# importando as bibliotecas

import openpyxl
import pandas as pd
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

# arquivo com os CNPJs para criar a lista de CNPJs e montar a URL
# df = pd.read_excel('data/output/bases-separadas/-7.xlsx')

# lista de CNPJS
df = pd.read_excel('data/output/bases-separadas/-0.xlsx')
cnpj_lista = df['cnpj'].values.tolist() # lista final

# teste de CNPJ
# cnpj_lista = ['29614931000161'] # página teste
# cnpj_lista = ['29614931000161', '50864554000105'] # lista teste
# cnpj_lista = ['29614931000161', '50864554000105', '1234455555555'] # lista teste com ultimo cnpj errado


cnpj_lista_verificado = []

# acessar o site por uma lista de URLS 
for i in list(cnpj_lista):
    try:
        driver = webdriver.Chrome()
        url = f"https://cnpj.biz/{i}"
        # url = f"https://amazon.com/"
        driver.get(url)

        #tempo para carregar o popup da página
        time.sleep(7)

        #clicar no botão do popup
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div[2]/button[2]").click()

        # extrair os dados de cnpj e cnae e colocar na lista
        dado_cnpj = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/p[1]/span[2]/b").text
        dado_cnae = driver.find_element(By.XPATH, "//span[contains(@style,'cursor: pointer;')]").text

        # colocar os dados na lista
        cnpj_lista_verificado.append([dado_cnpj, dado_cnae])

    # caso o cnpj ou a a página não seja encontrada
    except:
        dado_cnpj = i
        dado_cnae = "cnpj nao encontrado"
        cnpj_lista_verificado.append([dado_cnpj, dado_cnae])


    # print(cnpj_lista_verificado)
    driver.quit()

    # tempo de pausa entre consultas
    time.sleep(3)

# tratar os dados antes de exportar
df_cnpj_verificado = pd.DataFrame(cnpj_lista_verificado, columns=['cnpj', 'cnae']).drop_duplicates().reset_index(drop=True)
df['cnpj'] = df['cnpj'].astype('object')
df.loc[:, 'cnae'] = df_cnpj_verificado['cnae']
df['cnae'] = df['cnae'].astype('str')
df['cnae'] = df['cnae'].str.replace("<u>", "")
df['cnae'] = df['cnae'].str.replace("</u>", "")

# Criando o nome do arquivo antes de exportar
todays_date = time.strftime("%d-%m-%Y")
todays_time = time.strftime("%H-%M-%S")
excelfilename = "rnt-cnpj-com-cnae" + "-dia-" + todays_date + "-hora-" + todays_time +".xlsx"

# Exportando o arquivo para o excel
df.to_excel(f"data\output\lista-cnpjs-separados\{excelfilename}", sheet_name='sheet1', index=False)