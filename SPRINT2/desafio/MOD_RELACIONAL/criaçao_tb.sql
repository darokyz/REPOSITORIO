CREATE TABLE Clientes (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente TEXT NOT NULL,
    cidadeCliente TEXT,
    estadoCliente TEXT,
    paisCliente TEXT
);

CREATE TABLE Carros (
    idCarro INTEGER PRIMARY KEY,
    kmCarro REAL,
    classiCarro TEXT,
    marcaCarro TEXT,
    modeloCarro TEXT,
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

CREATE TABLE Combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel TEXT NOT NULL
);

CREATE TABLE Vendedores (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor TEXT,
    sexoVendedor INTEGER,
    estadoVendedor TEXT
);

CREATE TABLE Locacoes (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idCarro INTEGER,
    idVendedor INTEGER,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INTEGER,
    vlrDiaria REAL,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedores(idVendedor)
);
