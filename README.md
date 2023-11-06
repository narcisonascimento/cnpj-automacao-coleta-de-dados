# Renault - Automação de coleta de Dados
## RPA - Robotic Process Automation
### Problema: falta de CNAE em uma base de 5,7k CNPJs.

**Objetivo:** coletar dados de forma automática e complementar a base de CNPJs.
**Bibliotecas:** Pandas e Selenium
**Dados Coletados:** CNPJ, CNAE, Situação cadastral, URL da página final

**Passo 1:**
Entendimento dos dados a serem coletados e pesquisa de possíveis sites para a coleta.

**Passo 2:**
30% da base estava com dados incompletos. CNPJs precisam obrigatoriamente de 14 caracteres/números e na base recebida 30% estava com 13.
O problema estava por causa do 0 (zero) da esquerda, o Excel o ignora.
Tratamento foi feito diretamente no Excel.

**Passo 3:**
Para diminuir o tempo das consultas, desenvolvi um código para separar as bases a cada 100 linhas, gerando 57 arquivos.

**Passo 4:**
Desenvolvi a verificação em um site onde a construção da URL é simples possibilitando um _looping for_ na URL e coletar os dados.
O processo de coleta da primeira versão (arquivo: 'app-cnpj') foi demorado, levando ~33min para coletar 100 CNPJS.
A estrutura HTML/CSS do site é desorganizada e de difícil identificação dos elementos para coletar os dados. 

**Passo 5:**
Com as dificuldades do passo 4.
Desenvolvi um novo robô para consultar em um site diferente otimizando a consulta de 100 CNPJS em 50% do tempo ~17min.
O passo a passo é mais complexo, onde:
  **Primeiro:** fazer a consulta na home
  **Segundo:** acessar a página de resultado de busca
  **Terceiro:** acessar a página de detalhe do CNPJ
  **Quarto:** coletar os dados

**Passo 6:**
Após a coleta de todos os dados, tratei os dados e exportei para excel.

**Passo 7:**
Concatenar todas os arquivos em Excel separando dados com e sem CNAE.

**Passo 8:**
Compartilhar com a área de negócios.
