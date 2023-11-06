# importando as bibliotecas

import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# arquivo com os CNPJs para criar a lista de CNPJs
# aqui pode ser feito uma melhoria, onde o usuário pode colocar o nome do arquivo via CMD sem ter que abrir o vscode
df = pd.read_excel(
    'data/output/bases-separadas/-11.xlsx', converters={'cnpj': str}
)

# lista final
cnpj_lista = df['cnpj'].values.tolist()

# teste de CNPJ
# cnpj_lista = ['29614931000161']
# lista teste
# cnpj_lista = ['29614931000161', '50864554000105']
# lista teste
# cnpj_lista = ['50864554000105']
# lista teste com ultimo cnpj errado
# cnpj_lista = ['29614931000161', '50864554000105', '1234455555555']

# Listas
cnpj_lista_verificado = []

# Acessar o site https://cnpj.linkana.com/
for i in list(cnpj_lista):
    services = Service(ChromeDriverManager().install())

    try:
        driver = webdriver.Chrome(service=services)
        url = "https://cnpj.linkana.com/"
        driver.get(url)
        driver.implicitly_wait(7)

        # Inserir o CNPJ no campo de busca
        # wait = WebDriverWait(driver, 5)
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-sm")))
        driver.find_element(By.CLASS_NAME, "text-sm").clear()
        driver.find_element(By.CLASS_NAME, "text-sm").send_keys(i)

        # Clicar buscar
        driver.find_element(By.CLASS_NAME, "rounded-full").click()

        # Se existir resultado, Clicar no primeiro resultado encontrado, caso contrário
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "text-dark2")))
        resultado = driver.find_element(By.CLASS_NAME, "text-dark2").text

        if "resultados foram encontrados" in resultado:
            driver.find_element(By.CLASS_NAME, "text-brand").click()

            dado_cnpj_verificar = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/main/div[2]/div[7]/div/h2/b[2]").text
            dado_cnae = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/main/div[2]/div[8]/ul/li[2]").text
            dado_situacao_cadastral = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/main/div[2]/ul[1]/li[3]/p").text
            dado_url = driver.current_url

            # colocar os dados na lista
            cnpj_lista_verificado.append(
                [i, dado_cnpj_verificar, dado_cnae, dado_situacao_cadastral, dado_url])

        else:
            dado_cnpj_verificar = "cnpj nao encontrado"
            dado_cnae = "cnpj nao encontrado"
            dado_situacao_cadastral = "cnpj nao encontrado"
            dado_url = "cnpj nao encontrado"
            cnpj_lista_verificado.append(
                [i, dado_cnpj_verificar, dado_cnae, dado_situacao_cadastral, dado_url])

    except:
        dado_cnpj = i
        dado_cnpj_verificar = "cnpj nao encontrado"
        dado_cnae = "cnpj nao encontrado"
        dado_situacao_cadastral = "cnpj nao encontrado"
        dado_url = "cnpj nao encontrado"
        cnpj_lista_verificado.append(
            [i, dado_cnpj_verificar, dado_cnae, dado_situacao_cadastral, dado_url])

    driver.quit()

# tratar os dados antes de exportar
df = pd.DataFrame(cnpj_lista_verificado,
                  columns=['cnpj',
                           'cnpj_verificar',
                           'cnae',
                           'situacao_cadastral',
                           'url']).drop_duplicates().reset_index(drop=True)

df['cnpj'] = df['cnpj'].astype('object')
df.loc[:, 'cnae'] = df['cnae']
df['cnae'] = df['cnae'].astype('str')
df['cnae'] = df['cnae'].str.replace("<u>", "")
df['cnae'] = df['cnae'].str.replace("</u>", "")
df['cnpj_verificar'] = df['cnpj_verificar'].astype('object')
df['cnpj_verificar'] = df['cnpj_verificar'].str.replace(".", "")
df['cnpj_verificar'] = df['cnpj_verificar'].str.replace("/", "")
df['cnpj_verificar'] = df['cnpj_verificar'].str.replace("-", "")

# Create a loop to compare the values
for index, row in df.iterrows():
    if row['cnpj'] != row['cnpj_verificar']:
        df.loc[df['cnpj'] != df['cnpj_verificar'], [
            'cnae', 'situacao_cadastral', 'url']] = "cnpj nao encontrado"
        # print(f"The values are equal for row {index}")
    else:
        pass
        # df.loc[df['cnpj'] != df['cnpj_verificar'], [
        #     'cnae', 'situacao_cadastral', 'url']] = "cnpj nao encontrado"
        # print(f"The values are not equal for row {index}")

# retirando coluna de verificação de CNPJ
df = df.drop(columns=['cnpj_verificar'])

# Criando o nome do arquivo antes de exportar
todays_date = time.strftime("%d-%m-%Y")
todays_time = time.strftime("%H-%M-%S")
excelfilename = "rnt-cnpj-com-cnae" + "-dia-" + \
    todays_date + "-hora-" + todays_time + ".xlsx"

# Exportando o arquivo para o excel
df.to_excel(
    f"data\output\lista-cnpjs-separados\{excelfilename}", sheet_name='sheet1', index=False)
# df.to_excel(
#     f"data\output\lista-teste\{excelfilename}", sheet_name='sheet1', index=False)
