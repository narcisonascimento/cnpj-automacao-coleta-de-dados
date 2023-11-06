# Renault - Automação de coleta de Dados <br> RPA - Robotic Process Automation
# Resultados:
****Otimização de 50% do tempo no segundo app desenvolvido.****<br>
**Sucesso de XX% na coleta dos dados.**

**Problema:** falta de CNAE em uma base de 5,7k CNPJs.<br>
**Objetivo:** coletar dados de forma automática e complementar a base de CNPJs.<br>
**Bibliotecas:** Pandas e Selenium<br>
**Dados Coletados:** CNPJ, CNAE, Situação cadastral, URL da página final<br>



### Passos do Projeto

**Passo 1:**<br>
Entendimento dos dados a serem coletados e pesquisa de possíveis sites para a coleta.

**Passo 2:**<br>
30% da base estava com dados incompletos. CNPJs precisam obrigatoriamente de 14 caracteres/números e na base recebida 30% estava com 13.
O problema estava por causa do 0 (zero) da esquerda, o Excel o ignora.
Tratamento foi feito diretamente no Excel.

**Passo 3:**<br>
Para diminuir o tempo das consultas, desenvolvi um código para separar as bases a cada 100 linhas, gerando 57 arquivos.

**Passo 4:**<br>
Desenvolvi a verificação em um site onde a construção da URL é simples possibilitando um _looping for_ na URL e coletar os dados.
O processo de coleta da primeira versão (arquivo: 'app-cnpj') foi demorado, levando ~33min para coletar 100 CNPJS.
A estrutura HTML/CSS do site é desorganizada e de difícil identificação dos elementos para coletar os dados. 

**Passo 5:**<br>
Com as dificuldades do passo 4.
Desenvolvi um novo robô (app-cnpj-2) para consultar em um site diferente otimizando a consulta de 100 CNPJS em 50% do tempo ~17min.
O passo a passo é mais complexo, onde: <br>
  **- Primeiro:** fazer a consulta na home<br>
  **- Segundo:** acessar a página de resultado de busca<br>
  **- Terceiro:** acessar a página de detalhe do CNPJ<br>
  **- Quarto:** coletar os dados<br>

**Passo 6:**<br>
Após a coleta de todos os dados, tratei os dados e exportei para excel.

**Passo 7:**<br>
Concatenar todas os arquivos em Excel separando dados com e sem CNAE.

**Passo 8:**<br>
Compartilhar com a área de negócios.
