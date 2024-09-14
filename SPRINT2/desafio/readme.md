# Desafio de Normalização e Modelagem Dimensional de Base de Dados de Locadora

## Descrição do Projeto

Este projeto tem como objetivo a normalização de uma base de dados de uma locadora de veículos e a criação de modelos relacionais e dimensionais a partir da tabela de locações fornecida. O objetivo principal é otimizar a estrutura do banco de dados, garantindo a integridade dos dados, melhorando a organização e facilitando a análise de informações.

Normalização: Transformar a tabela de locações não normalizada em um conjunto de tabelas normalizadas, aplicando as formas normais;
Modelagem Relacional: Desenvolver um modelo de banco de dados relacional eficiente.
Modelagem Dimensional: Elaborar um diagrama dimensional para simplificar a análise de dados e a geração de relatórios.


A tabela de locações original continha informações de clientes, carros, vendedores e transações de locação, armazenadas de forma desnormalizada. Cada registro apresentava dados redundantes, exigindo a divisão em várias tabelas menores para garantir uma melhor organização e evitar duplicações desnecessárias;

Identificação de Entidades
Foram identificadas as seguintes entidades principais:
cliente;
Carro;
Vendedor;
Combustível;
Locações.
Cada entidade foi transformada em uma tabela no modelo normalizado.

## Modelagem Dimensional
Identificação de Fato e Dimensões
Tabela Fato: A tabela tb_locacao foi identificada como a tabela fato principal, armazenando os eventos de locação e os valores numéricos associados, como o valor da locação.

Tabelas de Dimensão: As tabelas Clientes, Carros, Combustivel, e Vendedores foram classificadas como tabelas de dimensão, contendo dados descritivos que contextualizam os eventos de locação.
Criação do Modelo Dimensional
No modelo dimensional, a tabela fato tb_locacao foi posicionada no centro, com as tabelas de dimensão conectadas a ela por meio de chaves estrangeiras. Essa estrutura permite uma análise rápida e eficaz dos dados, facilitando a geração de relatórios e consultas analíticas.

Ferramentas Utilizadas
DBeaver: Utilizado para gerenciar o banco de dados e executar as consultas SQL.
VSCode: Usado para editar scripts e realizar a integração com o sistema.
Conclusão
A normalização e modelagem resultaram em um banco de dados relacional eficiente e em um diagrama dimensional bem estruturado. Esses processos reduziram significativamente as redundâncias, garantiram a integridade referencial dos dados e facilitaram a análise das informações. A aplicação de boas práticas de design de banco de dados otimizou o sistema, tornando-o mais eficiente para consultas e relatórios futuros.
