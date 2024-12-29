README - Sprint 10: Desafio de Filmes e Séries

Visão Geral

A Sprint 10 do Desafio de Filmes e Séries teve como foco principal a criação de dashboards e análises visuais utilizando os dados previamente tratados nas sprints anteriores. Essa etapa consolidou o fluxo de trabalho de processamento, modelagem e visualização de dados, demonstrando a capacidade de gerar insights acionáveis a partir de dados estruturados. O principal objetivo foi explorar os dados para identificar padrões, tendências e gerar previsões relacionadas ao desempenho de filmes de ação/animações japonesas.

Objetivos:

Desenvolver dashboards interativos:

Criar visualizações de dados intuitivas e informativas no AWS QuickSight.

Permitir a exploração dinâmica de diferentes aspectos dos dados, como tendências de popularidade e relação entre métricas-chave.

Gerar insights acionáveis:

Identificar padrões e tendências relevantes para a indústria cinematográfica.

Apresentar previsões e análises baseadas em comportamentos históricos de filmes.

Consolidar a utilização das ferramentas da AWS:

Utilizar o AWS QuickSight como ferramenta para criação de dashboards.

Garantir que os dados estivessem adequadamente preparados e estruturados na Refined Zone.

Etapas Realizadas

1. Preparar Dados na Refined Zone

Os dados previamente armazenados e transformados na camada Refined foram utilizados como base para as visualizações. As tabelas e views criadas na Sprint 9 no AWS Glue Data Catalog serviram como fonte primária para o QuickSight.

Formato dos Dados: Parquet

Categorias de Dados Analisados:

Filmes de ação/animações japonesas

2. Criação de Dashboards no AWS QuickSight
Popularidade e Data de Lançamento

Popularidade e Contagem de Votos por Artista

Popularidade das Franquias

Desvio Padrão do Tempo de Duração das Franquias

Soma de Votos por País de Produção em Relação ao Tempo de Duração

Production_countries (Países de Produção)

3. Geração de Insights
![DASHBOARD](./Folha_1_2024-12-27T13_49_09_page-0001%20(1).jpg)
Ferramentas Utilizadas

AWS Glue: Para processamento e organização dos dados na Refined Zone.

AWS QuickSight: Para a criação de dashboards e análises visuais.

Spark: Para transformações de dados em grande escala.

Resultados Alcançados

Dashboards Interativos: Permitiram uma compreensão clara dos padrões e tendências.

Análises Avançadas: Identificação de insights valiosos para a indústria de filmes.

Integração Completa no AWS: Processo fim a fim utilizando serviços da AWS para garantir escalabilidade e eficiência.


------------------------------------------------------------------------------------------------------------------------------------

4. INSIGHTS
1. Popularidade e Data de Lançamento
Gráfico de Barras

Descrição: Ilustra a popularidade ao longo do tempo, destacando os períodos de lançamento com diferentes cores. Cada barra representa um intervalo específico, com a altura da barra refletindo o nível de popularidade em cada período.

Insights: Picos de popularidade em determinados anos indicam lançamentos de grande sucesso. A utilização de cores distintas facilita a identificação visual rápida dos períodos de maior atividade. Pode ser correlacionado com o gráfico de Popularidade e Contagem de Votos por Artista para investigar se os picos de popularidade estão associados a lançamentos específicos de artistas.

2. Popularidade e Contagem de Votos por Artista
Gráfico de Área

Descrição: Apresenta a relação entre a popularidade e a contagem de votos de diferentes artistas, utilizando duas representações visuais distintas para cada variável. A área sombreada indica o nível de popularidade, enquanto a linha preta representa a contagem de votos.

Insights: Artistas com áreas sombreadas maiores e linhas de votos mais altas se destacam, indicando uma combinação de popularidade e forte apoio do público. Pode ser correlacionado com o gráfico de Popularidade e Data de Lançamento para verificar se os artistas mais populares coincidem com os lançamentos mais bem-sucedidos.

3. Popularidade das Franquias
Gráfico de Rosca

Descrição: Oferece uma representação visual da popularidade das diferentes franquias, dividindo o gráfico em seções que correspondem a cada franquia. O tamanho de cada seção reflete a popularidade relativa.

Insights: Franquias como "One Piece" e "Dragon Ball" são as mais populares. Facilita a comparação entre as franquias e pode ser correlacionado com o gráfico de Desvio Padrão do Tempo de Duração das Franquias para explorar a relação entre popularidade e consistência na duração dos episódios.

4. Desvio Padrão do Tempo de Duração das Franquias
Gráfico de Radar

Descrição: Ilustra o desvio padrão do tempo de duração dos episódios de diferentes franquias, permitindo visualizar a variabilidade nas durações ao longo do tempo.

Insights: Franquias com desvio padrão menor, como "Inuyasha", têm episódios de duração mais consistente. Franquias como "Dragon Ball" e "Outros" exibem maior variabilidade. Pode ser correlacionado com o gráfico de Popularidade das Franquias para investigar se a consistência na duração dos episódios tem impacto na popularidade.

5. Soma de Votos por País de Produção em Relação ao Tempo de Duração
Gráfico de Dispersão

Descrição: Apresenta a soma de votos em relação ao tempo de duração de filmes ou séries, segmentados por país de produção. Cada ponto representa uma obra específica, com o tamanho do ponto variando conforme a soma total de votos recebidos.

Insights: Obras com maior duração frequentemente acumulam mais votos, sugerindo que filmes ou séries mais longas atraem mais atenção e engajamento do público. Pode ser correlacionado com o gráfico de Mix de Tempo de Duração e Popularidade por Franquias e Países de Produção para analisar como a duração influencia a popularidade em diferentes mercados.

6. Production_countries (Países de Produção)
Gráfico de Linhas

Descrição: Ilustra a variação da popularidade e do tempo de duração ao longo do tempo para diferentes franquias, com foco nos países de produção. As linhas representam a evolução tanto da popularidade quanto da duração das obras ao longo do tempo.

Insights: Permite comparar tendências de popularidade e duração entre diferentes países de produção, como Japão e Japão/Reino Unido. Pode ser correlacionado com o gráfico de Soma de Votos por País de Produção em Relação ao Tempo de Duração para uma análise mais profunda sobre como a duração das obras impacta sua popularidade em diferentes contextos geográficos e culturais.

### INSIGHT GERAL
 Resumo e Insights Finais
A análise das franquias de anime revela informações sobre o comportamento do público e os fatores que influenciam o sucesso das produções. Franquias como "Dragon Ball" e "Ghost in the Shell" se destacam em popularidade, refletindo uma base de fãs fiel e impacto cultural significativo. Picos de popularidade indicam lançamentos estratégicos que se tornaram icônicos.

A consistência nas produções, exemplificada por "Inuyasha", mostra que a uniformidade no tempo de duração dos episódios pode contribuir para a fidelidade dos fãs e a continuidade do sucesso. A análise da qualidade percebida destaca "Ghost in the Shell", que além de popular, apresenta altas notas médias, indicando uma percepção de alta qualidade pela audiência.

Ghost in the Shell se beneficia da colaboração entre Japão e Reino Unido, aumentando sua visibilidade global e combinando técnicas de animação avançadas com estilos visuais únicos, resultando em uma experiência audiovisual inovadora e de alta qualidade.

Teia de Relações entre Análises
Observando todos os gráficos e suas interações, percebemos uma rede de relações que revela como variáveis como popularidade dos artistas, duração dos episódios, lançamento e influência cultural dos países se entrelaçam, impactando o sucesso das franquias.

Picos de popularidade frequentemente coincidem com lançamentos de filmes por artistas com base de fãs consolidada, refletindo-se em um aumento significativo nos votos. Artistas populares contribuem diretamente para o sucesso contínuo das franquias, aumentando sua relevância.

As franquias mais populares não necessariamente têm episódios de duração consistente. "Dragon Ball", por exemplo, mantém alta popularidade apesar da variabilidade, indicando que a qualidade das histórias e personagens icônicos compensam a falta de consistência. Por outro lado, a consistência na duração dos episódios pode ser benéfica para manter a fidelidade dos fãs, como visto em "Inuyasha".

Papel dos Países de Produção
Produções de países como o Japão, que são mais longas, tendem a atrair mais votos, indicando que o público valoriza produções robustas. Países que mantêm uma duração consistente colhem os frutos dessa regularidade, contribuindo para a estabilidade da popularidade das franquias.

Regularidade e Timing
A regularidade na produção e o timing estratégico dos lançamentos são essenciais para o sucesso a longo prazo de uma franquia. Quando uma franquia mantém uma duração consistente e é lançada em períodos chave, tende a atrair mais votos e engajamento. "Inuyasha" demonstra a importância de um conteúdo regular para garantir sucesso duradouro.

Essa análise mostra como popularidade, artistas, duração dos filmes e produção dos países interagem para determinar o sucesso das franquias de anime. A regularidade e o timing dos lançamentos, juntamente com a influência de artistas populares, são cruciais para construir e manter uma base de fãs leal e engajada.
[DETALHAMENTO DAS ANÁLISES](./StorytellingSPRINT10.pdf)

Conclusão

A Sprint 10 concluiu com sucesso o ciclo de processamento e análise de dados no Desafio de Filmes e Séries. Os dashboards criados não apenas demonstraram a viabilidade da estrutura implementada, mas também geraram insights práticos que podem ser aplicados na tomada de decisões para a indústria cinematográfica. A experiência consolidou habilidades em modelagem de dados, análises visuais e previsões baseadas em dados.