import sqlite3

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
            "modelo" TEXT NOT NULL,
            "ano" INTEGER NOT NULL,
            "cor" TEXT NOT NULL,
            "placa" TEXT NOT NULL,
            "chassi" TEXT NOT NULL,
            "cpf" INTEGER NOT NULL,
            PRIMARY KEY("placa"),
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
            "id_cotacao" INTEGER ,
            "placa" TEXT NOT NULL CHECK (LENGTH(placa)=7),
            "cpf" TEXT NOT NULL,
            "data_inicio" DATE NOT NULL,
            "data_termino" DATE NOT NULL,
            "vencimento" DATE NOT NULL,
            "valor" REAL NOT NULL,            
            PRIMARY KEY("id_cotacao"),
            FOREIGN KEY ("cpf") REFERENCES clientes(cpf),
            FOREIGN KEY ("placa") REFERENCES veiculos(placa)
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
            "data_inicio" DATE NOT NULL,
            "data_termino" DATE NOT NULL,
            "vencimento" DATE NOT NULL,  
            PRIMARY KEY("apolice"),
            FOREIGN KEY ("id_cotacao") REFERENCES cotacoes(id_cotacao)
        );
    ''')
    conexao.commit()
    conexao.close()

def criar_tabela_cliente():

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE clientes (
            cpf INTEGER PRIMARY KEY CHECK (LENGTH(cpf) = 11) NOT NULL,
            nome TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            telefone TEXT NOT NULL,
            profissao TEXT NOT NULL,
            faixa_salarial NUMERIC NOT NULL,
            condutor_principal INTEGER CHECK (condutor_principal IN (0, 1)) NOT NULL,
            proprietario INTEGER CHECK (proprietario IN (0, 1)) NOT NULL,
            estado_civil TEXT CHECK (estado_civil IN ('solteiro', 'viuvo', 'casado', 'divorciado')) NOT NULL
    );
    ''')
