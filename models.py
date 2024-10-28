import sqlite3

def validar_cpf(cpf):
    conn = sqlite3.connect('projetoES3.db')  
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
    count = cursor.fetchone()[0]

    conn.close()
    return count > 0

def criar_conexao():
    return sqlite3.connect('projetoES3.db')

def criar_tabela_seguradora():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Seguradora" (
            "nome" TEXT NOT NULL,
            "cnpj" TEXT NOT NULL CHECK (LENGTH(cnpj) = 14),
            "email" TEXT NOT NULL,
            "endereco" TEXT NOT NULL,
            "telefone" TEXT NOT NULL,
            PRIMARY KEY("cnpj")
        );
    ''')
    conexao.commit()
    conexao.close()

def criar_tabela_veiculos():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Veiculos" (
        "placa" TEXT PRIMARY KEY,  -- 'placa' é a chave primária
        "cpf" INTEGER NOT NULL,
        "modelo" TEXT NOT NULL,
        "ano" TEXT NOT NULL,
        "cor" TEXT NOT NULL,
        "combustivel" TEXT CHECK(combustivel IN ('gasolina', 'alcool', 'flex', 'eletrico')),
        "chassi" TEXT NOT NULL,
        "pernoite" TEXT CHECK(pernoite IN ('casa', 'rua', 'apt')),
        "cep_pernoite" INTEGER,
        "garagem" INTEGER CHECK(garagem IN (0, 1)),
        "rastreador" INTEGER CHECK(rastreador IN (0, 1)),
        "remunerada" INTEGER CHECK(remunerada IN (0, 1)),
        "ir_trabalho_estudo" INTEGER CHECK(ir_trabalho_estudo IN (0, 1)),
        "estacionamento" INTEGER CHECK(estacionamento IN (0, 1)),
        FOREIGN KEY ("cpf") REFERENCES clientes(cpf)
    );
    ''')
    conexao.commit()
    conexao.close()

def criar_tabela_cotacoes():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Cotacoes" (
            "id_cotacao" INTEGER PRIMARY KEY AUTOINCREMENT,
            "placa" TEXT NOT NULL,  -- Mantendo apenas 'placa' como chave estrangeira
            "cpf" INTEGER NOT NULL,
            "data_inicio" TEXT NOT NULL,
            "valor" REAL NOT NULL,
            "cnpj_seguradora" TEXT NOT NULL,  
            FOREIGN KEY ("cpf") REFERENCES clientes(cpf),
            FOREIGN KEY ("placa") REFERENCES Veiculos(placa),  -- Referência a 'placa'
            FOREIGN KEY ("cnpj_seguradora") REFERENCES Seguradora(cnpj)
        );
    ''')
    conexao.commit()
    conexao.close()

def criar_tabela_seguros():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Seguros" (
            "apolice" INTEGER NOT NULL,
            "id_cotacao" INTEGER NOT NULL,
            "valor_total" REAL NOT NULL,
            "data_inicio" TEXT NOT NULL,
            "data_termino" TEXT NOT NULL,
            "pagamento" TEXT NOT NULL,  
            PRIMARY KEY("apolice"),
            FOREIGN KEY ("id_cotacao") REFERENCES Cotacoes(id_cotacao)  -- Referência a 'Cotacoes'
        );
    ''')
    conexao.commit()
    conexao.close()

def criar_tabela_cliente():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            cpf INTEGER PRIMARY KEY CHECK (LENGTH(cpf) = 11) NOT NULL,
            nome TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            telefone TEXT NOT NULL,
            profissao TEXT NOT NULL,
            faixa_salarial Real NOT NULL,
            condutor_principal INTEGER CHECK (condutor_principal IN (0, 1)) NOT NULL,
            proprietario INTEGER CHECK (proprietario IN (0, 1)) NOT NULL,
            estado_civil TEXT CHECK (estado_civil IN ('solteiro', 'viuvo', 'casado', 'divorciado')) NOT NULL
        );
    ''')
    conexao.commit()
    conexao.close()