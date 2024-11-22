# Desafio de Análise de Filmes e Séries 🎬
Visão Geral
Desenvolvimento do desafio proposto na Sprint 6, mas agora realizando a parte da spinrt 7 que é: foco em ingestão de dados de APIs, processamento e análise utilizando ferramentas de Big Data e computação em nuvem. Aqui estão detalhadas as etapas concluídas e o planejamento para entregas futuras, bem como a documentação das análises previstas e evidências de execução.

1. Objetivo
Este projeto tem como objetivo consolidar os conhecimentos adquiridos ao longo do programa, combinando diferentes ferramentas e práticas para criar um pipeline de dados robusto.

Foco desta entrega (Etapa 2)
--Ingestão de dados de filmes e séries via API (TMDB) utilizando AWS Lambda.
--Persistência de dados coletados no Amazon S3, camada RAW Zone, em formato JSON, seguindo boas práticas de organização e segurança.
--Complementar as informações já carregadas na etapa anterior, sem modificá-las.
2. Estrutura do Projeto
Entregáveis
Código-fonte organizado;
Markdown explicativo: [MARKDOWN](../desafio/markdown.md)
Pipeline na AWS Lambda: Código Python em formato .py configurado para ingestão e persistência de dados. [SCRIPT](../desafio/(lambda_version_py)desafio_sprint_7_API_dados_brutos.py)

Análises planejadas: Questões investigativas e insights a serem explorados com os dados coletados.
3. Escopo Atual 
Escopo Atual
Ingestão de Dados da API do TMDB
Realizar chamadas para coletar dados complementares ao arquivo CSV da etapa anterior.
Organizar os dados em arquivos JSON com, no máximo, 100 registros, armazenados no S3.
Configuração do AWS Lambda
Configuração de camadas no AWS Lambda para bibliotecas externas (ex.: tmdbv3api).
Implementação de um código Python com a biblioteca boto3 para:
Realizar chamadas à API do TMDB.
Agrupar os dados e salvá-los no S3.
Boas Práticas
Segurança: Tokens e credenciais protegidos, utilizando variáveis de ambiente.
#### Desenvolvimento local: Testes realizados localmente antes da migração para a AWS.

4. Questões de Análise Planejadas
 1. Relação entre tempo de duração e número de votos
 2. Como o tempo de duração de filmes de ação influencia o engajamento do público?
 3. Popularidade ao longo do tempo
 4. Quais mudanças ocorreram na popularidade de filmes de ação nas últimas décadas?
 5. Diversidade linguística
 6. O idioma original afeta a popularidade dos filmes globalmente?
 7. Comparação entre filmes longos e curtos
 8. Filmes mais longos têm desempenho superior em termos de votos?
 9. Modelo Preditivo de Popularidade
    Prever popularidade com base em variáveis como duração e número de votos.


5. Arquitetura de Solução
Abaixo está a arquitetura utilizada para o pipeline de dados:

TMDB API: Fonte primária de dados.
AWS Lambda: ingestão e pré-processamento.
Amazon S3: armzenamento de dados brutos (RAW Zone).
Athena: Consultas SQL para análise exploratória.
6. Ferramentas Utilizadas
Python: Para ingestão de dados e manipulação.
AWS Lambda: Execução do código.
Boto3: Interação com os serviços AWS.
tmdbv3api: Biblioteca para consumo da API do TMDB.
Amazon S3: Persistência de dados em JSON.
7. Evidências de Execução
[EVIDENCIAS](../evidencias/lambda_script_sucess.png)

8. Conclusão e Próximos Passos
Esta etapa inicial estabelece a base para um pipeline escalável e robusto. Na próxima fase, serão exploradas análises aprofundadas para responder às questões levantadas






