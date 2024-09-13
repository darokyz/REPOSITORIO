-- Inserir dados em dim_Carros
INSERT INTO dim_Carros (
    idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    idCombustivel
)
SELECT DISTINCT
    idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    idCombustivel
FROM tb_locacao
GROUP BY idCarro;

-- Inserir dados em dim_Clientes
INSERT INTO dim_Clientes (
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
)
SELECT DISTINCT
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM tb_locacao;

-- Inserir dados em dim_Combustivel
INSERT INTO dim_Combustivel (
    idCombustivel,
    tipoCombustivel
)
SELECT DISTINCT
    idCombustivel,
    tipoCombustivel
FROM tb_locacao;

-- Inserir dados em dim_Vendedores
INSERT INTO dim_Vendedores (
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
)
SELECT DISTINCT
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM tb_locacao;

-- Inserir dados em dim_Locacoes
INSERT INTO dim_Locacoes (
    idLocacao,
    idCliente,
    idCarro,
    idVendedor,
    idTempo,
    qtdDiaria,
    vlrDiaria
)
SELECT DISTINCT
    LOL.idLocacao,
    LOL.idCliente,
    LOL.idCarro,
    LOL.idVendedor,
    Tmp.idTempo,
    LOL.qtdDiaria,
    LOL.vlrDiaria
FROM tb_locacao AS LOL
JOIN dim_Tempo AS Tmp ON LOL.dataEntrega = Tmp.dataEntrega AND
LOL.dataLocacao = Tmp.dataLocacao

-- Inserir dados em dim_Tempo
INSERT INTO dim_Tempo (
    dataLocacao,
    horaLocacao,
    dataEntrega,
    horaEntrega
)
SELECT DISTINCT
    dataLocacao,
    horaLocacao,
    dataEntrega,
    horaEntrega
FROM tb_locacao;
