README do Desafio de Filmes e Séries - Sprint 9

Introdução

A Sprint 9 foi um gratificante projeto, pois envolveu a modelagem e processamento de dados para a camada Refined do data lake. A proposta era utilizar conceitos de modelagem multidimensional e tecnologias como AWS Glue, Apache Spark e o formato Parquet para transformar dados da camada Trusted em dados otimizados para análises e consultas futuras.

Este README também traz uma visão completa das experiências e etapas percorridas em todo o desafio, com destaque para os aprendizados obtidos.

Objetivo

O objetivo principal foi criar uma camada Refined robusta, que suportasse consultas e análises multidimensionais, seguindo boas práticas de organização e estruturação de dados. O desafio incluiu a modelagem de tabelas, a criação de jobs no AWS Glue para transformação dos dados e a garantia de que os mesmos estivessem prontos para visualização no Amazon QuickSight.

Passo a Passo da Implementação

1. Modelagem da Camada Refined 
![Refined](/SPRINT9/evidencias/camada_refined.png)
O primeiro passo foi definir um modelo de dados multidimensional. A ideia por trás desse modelo foi organizar os dados de maneira eficiente para permitir consultas rápidas e intuitivas. Após analisar as necessidades do projeto, desenvolvi uma modelagem que incluiu tabelas fato e dimensões, utilizando ferramentas específicas para garantir precisão no desenho e entendimento do modelo.

2. Preparação do Ambiente

Para garantir que o ambiente estivesse preparado, validei a integridade dos dados na camada Trusted. Em seguida, configurei os jobs no AWS Glue, utilizando workers otimizados para processar os dados com eficiência. Os jobs foram configurados com G 1x, 2 workers e um timeout de 60 minutos.

3. Transformação dos Dados

Os dados da camada Trusted foram transformados para atender às necessidades da camada Refined. Nesse processo, utilizei o Apache Spark dentro do AWS Glue para realizar transformações como limpeza de dados, padronização de formatos e particionamento para otimização das consultas futuras. Os dados foram salvos no formato Parquet.

4. União de Dados e Superação de Desafios

Quando tentei realizar o join entre os Parquet do CSV e do JSON, enfrentei dificuldades devido à ausência de uma chave única confiável. Inicialmente, os joins estavam limitados porque eu estava usando os títulos dos filmes como critério para o inner join, o que resultava em muitas inconsistências e divergências nos dados. Após análise, percebi que seria muito custoso tentar corrigir essas inconsistências diretamente.

Decidi voltar algumas etapas do processo e recuperar os dados novamente da API do TMDB, dessa vez incluindo o campo "imdb_id". Essa decisão foi crucial, pois permitiu que os joins funcionassem perfeitamente, garantindo a consistência e a completude dos dados.

Além disso, tive que refazer o código que transformava o CSV em Parquet, pois uma das partições estava corrompida. Isso exigiu uma análise detalhada de cada etapa do pipeline para identificar e corrigir o problema.

![UNIAO](/SPRINT9/evidencias/select_do_join.png)

5. Validação dos Resultados

Após transformar e unir os dados, validei os resultados comparando amostras das tabelas Trusted e Refined. Utilizei consultas no AWS Glue Data Catalog para garantir que as informações estavam corretas e consistentes. Também validei a performance das consultas, confirmando que o particionamento e o formato Parquet estavam otimizados.

6. Persistência e Organização

Os dados processados foram salvos na camada Refined. Além disso, foram criadas tabelas no AWS Glue Data Catalog para facilitar o consumo dos dados pelas ferramentas de visualização, como o Amazon QuickSight.

Explicação das Análises Realizadas

Como parte da Sprint 9, os dados foram preparados para futuras análises e visualizações no Amazon QuickSight. As prováveis análises planejadas incluíram:
Neste documento, apresento as análises realizadas sobre filmes de anime de ação, focando em aspectos como popularidade, notas médias, número de votos e suas relações com diversas dimensões, como o tempo de lançamento, gêneros, países de produção e artistas envolvidos.

## Dimensões e Fatos

Dimensões:
Dim_Filme: Contém informações específicas dos filmes, como idioma, título, data de lançamento, gêneros, duração e países de produção.
Dim_Artista: Contém informações sobre os artistas, como nome e profissão.
Dim_Tempo: Contém informações de data, como data de lançamento, ano, mês, dia e dia da semana.
![DIMENSÕES](/SPRINT9/evidencias/camada_dim.png)
Fatos:
Fato_Popularidade: Armazena a métrica de popularidade dos filmes.
Fato_NotaMedia: Armazena a média das avaliações dos filmes.
Fato_NumeroVotos: Armazena o número total de votos recebidos pelos filmes.
![FATOS](/SPRINT9/evidencias/dim_fatos_athena.png)


### Experiência ao Longo do Desafio

Minha jornada no Desafio de Filmes e Séries começou com etapas introdutórias, passando por desafios técnicos e culminando em entregas robustas, como a Sprint 9. Cada etapa trouxe aprendizados importantes, tanto técnicos quanto estratégicos:

Consumo de Dados da API do TMDB: No início, coletei dados detalhados de filmes e séries, lidando com estruturações JSON e extrações CSV. O foco inicial foi entender as informações disponíveis e garantir a qualidade dos dados para as etapas futuras.

Transformação e Armazenamento: Adaptei os pipelines para mover dados da Raw Zone para a Trusted Zone, com foco na limpeza e padronização. Cada ajuste foi planejado para facilitar os passos seguintes.

Superação de Obstáculos: Enfrentei problemas, como partições corrompidas e inconsistências nos dados, que exigiram investigações minuciosas. O uso de "imdb_id" como chave foi um divisor de águas para resolver os desafios de joins.

--Novas análises: [MARKDOWN](/SPRINT9/desafio/markdown.md)--

Modelagem e Análises: A Sprint 9 consolidou o aprendizado ao aplicar modelagem multidimensional e preparar os dados para análises avançadas no QuickSight.

Ao longo do desafio, o apoio das ferramentas AWS e o planejamento cuidadoso me permitiram atingir os objetivos, mesmo diante de dificuldades técnicas. Essa experiência fortaleceu minha compreensão de pipelines de dados complexos e modelagem analítica.

Conclusão

A Sprint 9 foi finalizada com sucesso, atendendo todos os requisitos definidos. Os dados da camada Refined estão prontos para serem utilizados em análises e visualizações na próxima etapa do desafio. O aprendizado prático proporcionado pela combinação de ferramentas como AWS Glue, Apache Spark e QuickSight foi essencial para consolidar conhecimentos e preparar terreno para desafios futuros.

Com a finalização desta sprint, estou pronto para iniciar a próxima etapa, que envolverá a visualização de dados e a geração de insights no QuickSight. O trabalho realizado até aqui reflete não apenas o avanço técnico, mas também uma maturidade crescente em lidar com projetos de dados complexos.