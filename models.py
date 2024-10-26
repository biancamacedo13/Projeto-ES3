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


   #  CREATE TABLE "Cliente" (
#    "cpf" TEXT NOT NULL,
#    "nome" TEXT NOT NULL,
#    "email" TEXT,
 #   "dt_nascimento" TEXT,
  #  "estado_civil" TEXT,
  #  "endereco" TEXT,
   # "telefone" INTEGER,
   # "profissao" TEXT,
    #"faixa_salarial" NUMERIC,
    #"condutor_principal" INTEGER NOT NULL,
    #"proprietario" INTEGER NOT NULL,
    #PRIMARY KEY("cpf"),
    #CHECK(LENGTH(cpf) = 11),
    #CHECK(condutor_principal IN (0, 1)),
    #CHECK(proprietario IN (0, 1))
#)
#"""