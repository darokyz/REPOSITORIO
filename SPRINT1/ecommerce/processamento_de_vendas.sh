#!/bin/bash

# Criar subdiretório vendas
mkdir -p ~/ecommerce/vendas
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/vendas/

# Criar subdiretório backup e fazer o backup com data
mkdir -p ~/ecommerce/backup
DATA=$(date +%Y%m%d)
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/backup/dados-$DATA.csv

# Renomear o arquivo de backup
mv ~/ecommerce/backup/dados-$DATA.csv ~/ecommerce/backup/backup-dados-$DATA.csv

# Criar relatorio.txt no diretório backup
cd ~/ecommerce/backup
echo "Data do sistema: $(date +'%Y/%m/%d %H:%M')" > relatorio.txt

# Extrai informações do arquivo CSV
PRIMEIRO_REGISTRO=$(head -n 2 backup-dados-$DATA.csv | cut -d ',' -f 5)
ULTIMO_REGISTRO=$(tail -n 1 backup-dados-$DATA.csv | cut -d ',' -f 5)
QUANTIDADE_ITENS=$(cut -d ',' -f 2 backup-dados-$DATA.csv | tail -n +2 | sort | uniq | wc -l)

echo "Data do primeiro registro de venda: $PRIMEIRO_REGISTRO" >> relatorio.txt
echo "Data do último registro de venda: $ULTIMO_REGISTRO" >> relatorio.txt
echo "Quantidade total de itens diferentes vendidos: $QUANTIDADE_ITENS" >> relatorio.txt

# Adiciona as primeiras 10 linhas do arquivo CSV ao relatorio.txt
echo -e "\nPrimeiras 10 linhas do arquivo:" >> relatorio.txt
head -n 11 backup-dados-$DATA.csv >> relatorio.txt

# Comprimir o arquivo CSV
zip backup-dados-$DATA.zip backup-dados-$DATA.csv

# Apagar o arquivo CSV original e o arquivo de vendas
rm backup-dados-$DATA.csv
rm ~/ecommerce/vendas/dados_de_vendas.csv

# Mensagem de conclusão
echo "Processamento concluído com sucesso!"
