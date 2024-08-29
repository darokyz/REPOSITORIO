README DESAFIO:
Criação do Diretório:

Primeiramente, criamos um diretório chamado ecommerce utilizando o comando mkdir no terminal. Este diretório será o local onde armazenaremos nosso arquivo dados_de_vendas.csv
Criação do Script:

Com o diretório e o arquivo de vendas, criamos um script para processar os dados. Utilizamos o editor nano para criar um arquivo chamado processamento_de_vendas.sh dentro do diretório ecommerce
Edição do Script:

Dentro do arquivo, escrevemos o seguinte script em bash, que realiza várias operações, como criar subdiretórios, fazer backup do arquivo de vendas e gerar um relatório.
"#!/bin/bash

"# Criar subdiretório vendas
mkdir -p ~/ecommerce/vendas
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/vendas/

"# Criar subdiretório backup e fazer o backup com data
mkdir -p ~/ecommerce/backup
DATA=$(date +%Y%m%d)
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/backup/dados-$DATA.csv

"# Renomear o arquivo de backup
mv ~/ecommerce/backup/dados-$DATA.csv ~/ecommerce/backup/backup-dados-$DATA.csv

"# Criar relatorio.txt no diretório backup
cd ~/ecommerce/backup
echo "Data do sistema: $(date +'%Y/%m/%d %H:%M')" > relatorio.txt

"# Extrai informações do arquivo CSV
PRIMEIRO_REGISTRO=$(head -n 2 backup-dados-$DATA.csv | cut -d ',' -f 5)
ULTIMO_REGISTRO=$(tail -n 1 backup-dados-$DATA.csv | cut -d ',' -f 5)
QUANTIDADE_ITENS=$(cut -d ',' -f 2 backup-dados-$DATA.csv | tail -n +2 | sort | uniq | wc -l)

echo "Data do primeiro registro de venda: $PRIMEIRO_REGISTRO" >> relatorio.txt
echo "Data do último registro de venda: $ULTIMO_REGISTRO" >> relatorio.txt
echo "Quantidade total de itens diferentes vendidos: $QUANTIDADE_ITENS" >> relatorio.txt

"# Adiciona as primeiras 10 linhas do arquivo CSV ao relatorio.txt
echo -e "\nPrimeiras 10 linhas do arquivo:" >> relatorio.txt
head -n 11 backup-dados-$DATA.csv >> relatorio.txt

"# Comprimir o arquivo CSV
zip backup-dados-$DATA.zip backup-dados-$DATA.csv

"# Apagar o arquivo CSV original e o arquivo de vendas
rm backup-dados-$DATA.csv
rm ~/ecommerce/vendas/dados_de_vendas.csv

"# Mensagem de conclusão
echo " >.< Processamento concluído com sucesso s2!"

Conceder Permissões de Execução:
Antes de agendar o script para execução automática, é necessário garantir que ele tenha permissões de execução. Isso é feito com o comando chmod.
Comando:
chmod +x

gendar a Execução do Script:
Para garantir que o script seja executado automaticamente todos os dias de segunda a quinta-feira às 15:27, utilizamos o cron. Edite as crontabs com o comando crontab -e e adicione a seguinte linha ao arquivo de cron
Criação do Consolidador:

Agora, criamos um segundo script chamado consolidador_de_processamento_de_vendas.sh, também com o comando nano.
"#!/bin/bash

"# Caminho para o diretório de backup onde os relatórios estão armazenados
BACKUP_DIR="~/ecommerce/backup"

"# Nome do arquivo final de relatório
RELATORIO_FINAL="relatorio_final.txt"

"# Inicializa o arquivo final de relatório
echo "Consolidado dos Relatórios de Vendas" > $RELATORIO_FINAL
echo "-----------------------------------" >> $RELATORIO_FINAL

"# Itera sobre todos os arquivos relatorio.txt no diretório de backup
for RELATORIO in $BACKUP_DIR/relatorio.txt
do
    "# Adicionar o conteúdo de cada relatório ao arquivo final
    echo "Relatório de $(basename $RELATORIO)" >> $RELATORIO_FINAL
    cat $RELATORIO >> $RELATORIO_FINAL
    echo -e "--------------------------------" >> $RELATORIO_FINAL
done

"# Mensagem de conclusão
echo "Consolidação dos relatórios concluída com sucesso!"
