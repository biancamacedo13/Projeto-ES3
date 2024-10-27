import sqlite3

def validar_cpf(cpf):
    # Conectar ao banco de dados
    conn = sqlite3.connect('projetoES3.db')  # Altere para o caminho do seu banco de dados
    cursor = conn.cursor()

    # Verificar se o CPF existe na tabela de clientes
    cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
    count = cursor.fetchone()[0]

    # Fechar a conexão
    conn.close()

    # Retornar True se o CPF existir, caso contrário False
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
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "cpf" INTEGER NOT NULL,  -- Adicionei esta linha
        "modelo" TEXT NOT NULL,
        "ano" TEXT NOT NULL,
        "cor" TEXT NOT NULL,
        "combustivel" TEXT CHECK(combustivel IN ('gasolina', 'alcool', 'flex', 'eletrico')),
        "placa" TEXT NOT NULL UNIQUE,  -- Para evitar duplicatas
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