#!/bin/bash

# subdiretório vendas e cópia do CSV
mkdir -p ~/ecommerce/vendas
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/vendas/
# Cria do subdiretório backup e backup com data
mkdir -p ~/ecommerce/backup
DATA=$(date +%Y%m%d)
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/backup/dados-$DATA.csv

# Renomeia o arquivo de backup
mv ~/ecommerce/backup/dados-$DATA.csv ~/ecommerce/backup/backup-dados-$DATA.csv

# tualização do relatório com uma variaveel
cd ~/ecommerce/backup
RELATORIO="relatorio-$(date +%Y%m%d-%H%M%S).txt"
echo "Data do sistema: $(date +'%Y/%m/%d %H:%M')" > $RELATORIO

# Info arquivo CSV
PRIMEIRO_REGISTRO=$(head -n 2 backup-dados-$DATA.csv | cut -d ',' -f 5)
ULTIMO_REGISTRO=$(tail -n 1 backup-dados-$DATA.csv | cut -d ',' -f 5)
QUANTIDADE_ITENS=$(cut -d ',' -f 2 backup-dados-$DATA.csv | tail -n +2 | sort | uniq | wc -l)

echo "Data do primeiro registro de venda: $PRIMEIRO_REGISTRO" >> $RELATORIO
echo "Data do último registro de venda: $ULTIMO_REGISTRO" >> $RELATORIO
echo "Quantidade total de itens diferentes vendidos: $QUANTIDADE_ITENS" >> $RELATORIO

# Adiciona as primeiras 10 linhas 
echo -e "\nPrimeiras 10 linhas do arquivo:" >> $RELATORIO
head -n 11 backup-dados-$DATA.csv >> $RELATORIO

# Compressão do arquivo CSV
zip backup-dados-$DATA.zip backup-dados-$DATA.csv

# Exclusão do arquivo CSV original e da cópia de vendas
rm backup-dados-$DATA.csv
rm ~/ecommerce/vendas/dados_de_vendas.csv

# Mensagem de conclusão
echo " >.< Processamento concluído com sucesso s2!"

