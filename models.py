import sqlite3

banco = sqlite3.connect('projeto.db')

cursor = banco.cursor()

cursor.execute('''
CREATE TABLE "Cliente" (
    "cpf" TEXT NOT NULL,
    "nome" TEXT NOT NULL,
    "email" TEXT,
    "dt_nascimento" TEXT,
    "estado_civil" TEXT,
    "endereco" TEXT,
    "telefone" INTEGER,
    "profissao" TEXT,
    "faixa_salarial" NUMERIC,
    "condutor_principal" INTEGER NOT NULL,
    "proprietario" INTEGER NOT NULL,
    PRIMARY KEY("cpf"),
    CHECK(LENGTH(cpf) = 11),
    CHECK(condutor_principal IN (0, 1)),
    CHECK(proprietario IN (0, 1))
)
''')

banco.commit()
banco.close()