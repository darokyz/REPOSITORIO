INSERT INTO Carros (
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
GROUP BY idCarro

INSERT INTO Clientes (
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
FROM tb_locacao

INSERT INTO Combustivel (
    idCombustivel,
    tipoCombustivel 
)
SELECT DISTINCT
    idCombustivel,
    tipoCombustivel
FROM tb_locacao

INSERT INTO Vendedores(
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
FROM tb_locacao

INSERT INTO Locacoes(
    idLocacao,
    idCliente,
    idCarro,
    idVendedor,
    dataLocacao,
    horaLocacao,
    qtdDiaria,
    vlrDiaria,
    dataEntrega,
    horaEntrega
)
SELECT DISTINCT
    idLocacao,
    idCliente,
    idCarro,
    idVendedor,
    dataLocacao,
    horaLocacao,
    qtdDiaria,
    vlrDiaria,
    dataEntrega,
    horaEntrega
FROM tb_locacao