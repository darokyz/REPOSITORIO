# Sprint 5 - Desafio de Manipulação de Dados com AWS
### 1. Objetivo
O objetivo deste desafio é praticar os conhecimentos em AWS e manipulação de dados em Python. O foco está em operações com arquivos no S3, utilizando o Boto3 e a biblioteca Pandas para realizar manipulações em um conjunto de dados obtido no portal de dados públicos do Governo Brasileiro.

### 2. Entregáveis
Arquivo Markdown com documentação de cada etapa e prints de execução.
Código Python (.py) contendo os scripts desenvolvidos.
Arquivo CSV com os dados originais e o CSV processado.

### 3. Desafio
Descrição das Etapas
Selecionar o Conjunto de Dados: Escolhemos um arquivo CSV do portal dados.gov.br com informações sobre alunos bolsistas. Garantimos que o arquivo é único na turma.

Análise Inicial: Inspecionamos o arquivo CSV localmente para conhecer o conteúdo e identificar quais manipulações poderiam ser realizadas.

Upload para o S3: Com um script Python, fizemos o upload do arquivo para um bucket do S3 utilizando a biblioteca Boto3.

## Manipulação de Dados com Pandas:

#### Filtragem: Filtramos alunos com bolsa mensal superior a R$500 e período de recebimento em 2024.
##### Agregações: Calculamos a média e o total dos valores das bolsas.
##### Função Condicional: Classificamos os valores das bolsas como "Alta Bolsa" ou "Baixa Bolsa".
##### Conversão de Moeda: Convertendo o valor da bolsa para dólares.
##### Extração de Data: Extraímos o ano de início do período de recebimento.
##### Formatação de String: Transformamos os nomes dos bolsistas em letras maiúsculas.
### Resultado Final
A tabela final, após todas as manipulações, foi armazenada como um novo arquivo CSV no S3. Para acessar o arquivo, consulte a pasta dados processados.

## Links Rápidos para Pastas e Arquivos

- [Pasta de Evidências (prints de execução)](./evidencias/)
  - [Imagem 1 de Execução](./evidencias/imagem1.png)
  - [Imagem 2 de Execução](./evidencias/imagem2.png)
- [Código Python - Script Principal](./importando.py)
- [Arquivo de Dados Processados (CSV)](./alunos_dados_processados.csv)
