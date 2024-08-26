#Camnh para o diretório de backup onde os relatoriosta armazenados
BACKUP_DIR="vendas/backup"
# Nome do arquivo final de relatorio
RELATORIO_FINAL="relatorio final.txt"
# Inicializa o arquivo final de relatório
echo "Consolidado dos Relatórios de Vendas" > $RELATORIO_FINAL
echo "-----------------------------------" >> $RELATORIO_FINAL
# Itera sobre todos os arquivos relatorio.txt no diretório de backup
for RELATORIO in $BACKUP_DIR/relatorio.txt
do
	# Adicionar o conteúdo de cada relatório ao arquivo final
	echo "Relatório de $(basename $RELATORIO)" >> $RELATORIO_FINAL
	cat $RELATORIO >> $RELATORIO_FINAL
	echo -e "--------------------------------" >> $RELATORIO_FINAL
done

# Mensagem de conclusão
echo "Consolidação dos relatórios concluída com sucesso!"
