Resumo da Sprint 7: Desafio de Análise de Filmes e Séries
Objetivo Geral
Integrar e aplicar conhecimentos sobre ingestão de dados via API, armazenamento no AWS S3, análises exploratórias avançadas, utilizando ferramentas de Big Data.

Etapa: Ingestão de API e Exploração de Dados
Coleta de Dados do TMDB
Processo: Realizadas chamadas à API do TMDB para complementar os dados carregados anteriormente.
Armazenamento: Dados salvos no AWS S3 (RAW Zone) em formato JSON, com limite de 100 registros por arquivo.
Desenvolvimento Local(PARA TESTE)/ Desenvolvimento no Lambda para ingestão final.

#### Código implementado localmente e adaptado para execução no AWS Lambda.

Boas práticas aplicadas, como modularização e segurança no gerenciamento de tokens de acesso.
Planejamento de Análises
Definidas 8 análises principais, com foco em tendências, correlações e variáveis linguísticas.
Planejamento de um modelo preditivo para prever a popularidade de filmes com base em variáveis como duração e número de votos...
[Teste local](../SPRINT7/evidencias/cod_test_injet_s3_concluido.png)

## Exercício Prático: Processamento com Spark no Docker
Objetivo
Implementar um processamento no Apache Spark utilizando Docker, simulando um cenário de análise de grandes volumes de dados.

Etapas Realizadas
Configuração do Ambiente:
Utilização da imagem jupyter/all-spark-notebook no Docker.
Configuração de portas para acessar o Jupyter Lab e inicialização do terminal Spark interativo.
Execução e Transformações:
Processamento do arquivo README.md, incluindo:
Divisão das linhas em palavras.
Contagem da frequência de palavras, utilizando operações Spark.
Conclusão
O exercício consolidou conceitos básicos de processamento distribuído com Spark e introduziu práticas essenciais para trabalhar com conjuntos de dados.

## Exercício: ETL com AWS Glue e Crawlers
Objetivo
Criar um fluxo ETL para transformação, particionamento e catalogação de dados no AWS S3.

Etapas Realizadas
Configuração de Permissões:
Criação da role AWSGlueServiceRole-Lab4 com permissões específicas para Glue, Lake Formation e S3.
Processamento com Glue:
Desenvolvimento de um job ETL que:
Transformou o arquivo CSV nomes.csv em JSON, particionado por sexo e ano.
Armazenou os resultados no S3 com estrutura organizada.
Catalogação e Consultas:
Criação de um crawler para gerar tabelas no Glue Catalog.
Integração com Athena para realizar consultas SQL.  -- (até o momento nao consegui realizar essa etapa)
#### (Demonstraçao dos exercícios )
[DEMO. EXs](../SPRINT7/exercicios)
### Conclusão
A atividade demonstrou como automatizar fluxos de dados utilizando Glue, desde a transformação até a catalogação, integrando diferentes serviços AWS para análises avançadas.

## Análises Exploradas com os Dados do TMDB
[Desafio](../SPRINT7/desafio/markdown.md)

Nesta sprint, avançamos na construção de um pipeline robusto para coleta e análise de dados, aplicando boas práticas e ferramentas modernas como Docker, Spark e AWS Glue. As análises definidas trazem insights relevantes sobre tendências no mercado de filmes de ação, com potencial para prever popularidade de lançamentos futuros.

Esse trabalho integra conceitos técnicos e análises estratégicas, alinhando aprendizado prático com aplicações reais no mercado de entretenimento e Big Data.