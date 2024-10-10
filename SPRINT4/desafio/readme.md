
# Desafio de Análise de Dados do Google Play Store
    Este projeto tem como objetivo analisar um dataset da Google Play Store, explorando informações sobre aplicativos, como número de downloads, classificações de conteúdo, avaliações e preços. Através de diversas análises e visualizações, buscamos obter insights relevantes a partir dos dados.

📁 Dataset
    O dataset utilizado contém informações sobre aplicativos disponíveis na Google Play Store, com as seguintes colunas:

App: Nome do aplicativo
Category: Categoria do aplicativo
Rating: Avaliação média (de 0 a 5)
Reviews: Número de reviews (avaliações textuais) feitas pelos usuários
Size: Tamanho do aplicativo (em MB ou KB)
Installs: Número de instalações
Type: Tipo do aplicativo (Gratuito ou Pago)
Price: Preço do aplicativo
Content Rating: Classificação de conteúdo (ex: Everyone, Teen, Mature 17+)
Genres: Gêneros do aplicativo
Last Updated: Data da última atualização
Current Ver: Versão atual do aplicativo
Android Ver: Versão mínima do Android necessária para rodar o aplicativo

# 🔧 Funcionalidades Implementadas
### As principais análises realizadas no projeto incluem:

# 1. Remoção de Duplicatas e Limpeza de Dados
    O dataset foi processado para remover duplicatas e tratar valores ausentes ou inconsistentes, como dados textuais não numéricos nas colunas de preços e reviews.

# 2. Análises Estatísticas e Exploratórias
    Top 10 Aplicativos por Número de Reviews: Foi criado um ranking dos 10 apps com o maior número de reviews.
    Aplicativo Mais Caro: O aplicativo mais caro identificado foi I'm Rich - Trump Edition, com um valor de $400.
    Distribuição das Classificações de Conteúdo: Analisamos quantos aplicativos estão em cada faixa de classificação.
    
# 3. Visualizações de Dados
    Utilizamos gráficos para explorar os dados de forma visual:

    Gráfico de Barras: Mostrando a distribuição das classificações de conteúdo.
    Gráfico de Pizza: Exibindo as 10 categorias mais frequentes de aplicativos.
# 4. Outras Métricas Calculadas
    Top 10 Aplicativos por Melhor Avaliação (Rating): Lista dos apps com as melhores médias de avaliação.
    Média de Preço dos Aplicativos Pagos: Calculamos a média de preço de todos os aplicativos pagos no dataset.

🛠️ 
# Tecnologias Utilizadas
    Python: Linguagem de programação principal.
      Pandas: Para manipulação e análise de dados.
        Matplotlib: Para visualizações gráficas.
          Jupyter Notebook: Ambiente de desenvolvimento interativo.
             VSCode: Editor de código utilizado no projeto.