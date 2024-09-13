CREATE TABLE dim_Clientes (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente TEXT NOT NULL,
    cidadeCliente TEXT,
    estadoCliente TEXT,
    paisCliente TEXT
);

CREATE TABLE dim_Carros (
    idCarro INTEGER PRIMARY KEY,
    kmCarro REAL,
    classiCarro TEXT,
    marcaCarro TEXT,
    modeloCarro TEXT,
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES dim_Combustivel(idCombustivel)
);

CREATE TABLE dim_Combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel TEXT NOT NULL
);

CREATE TABLE dim_Tempo (
    idTempo INTEGER PRIMARY KEY AUTOINCREMENT,
    dataLocacao DATE,
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME
);
CREATE TABLE dim_Vendedores (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor TEXT,
    sexoVendedor INTEGER,
    estadoVendedor TEXT
);

CREATE TABLE dim_Locacoes (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idCarro INTEGER,
    idVendedor INTEGER,
    idTempo INT,
    qtdDiaria INTEGER,
    vlrDiaria REAL,
    FOREIGN KEY (idCliente) REFERENCES dim_Clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES dim_Carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES dim_Vendedores(idVendedor),
    FOREIGN KEY (idTempo) REFERENCES dim_Tempo(idTempo)
);