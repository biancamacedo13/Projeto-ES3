import sqlite3

def criar_conexao(db_file):
    """ Cria uma conexão com o banco de dados SQLite especificado. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexão com o banco de dados estabelecida.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def atualizar_tabela_seguradora(conn):
    """ Atualiza a tabela Seguradora. """
    try:
        cursor = conn.cursor()
        
        # 1. Criar tabela temporária para armazenar dados existentes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Seguradora_temp" (
                "nome" TEXT NOT NULL,
                "cnpj" TEXT NOT NULL CHECK (LENGTH(cnpj) = 14),
                "email" TEXT NOT NULL,
                "endereco" TEXT NOT NULL,
                "telefone" TEXT NOT NULL,
                PRIMARY KEY("cnpj")
            );
        ''')
        
        # 2. Inserir dados da tabela Seguradora na tabela temporária
        cursor.execute('''
            INSERT INTO "Seguradora_temp" (nome, cnpj, email, endereco, telefone)
            SELECT nome, cnpj, email, endereco, telefone FROM "Seguradora";
        ''')

        # 3. Excluir a tabela Seguradora
        cursor.execute('DROP TABLE IF EXISTS "Seguradora";')

        # 4. Criar nova tabela Seguradora com o nome UNIQUE
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Seguradora" (
                "nome" TEXT UNIQUE NOT NULL,
                "cnpj" TEXT NOT NULL CHECK (LENGTH(cnpj) = 14),
                "email" TEXT NOT NULL,
                "endereco" TEXT NOT NULL,
                "telefone" TEXT NOT NULL,
                PRIMARY KEY("cnpj")
            );
        ''')

        # 5. Inserir dados da tabela temporária na nova tabela Seguradora
        cursor.execute('''
            INSERT INTO "Seguradora" (nome, cnpj, email, endereco, telefone)
            SELECT nome, cnpj, email, endereco, telefone FROM "Seguradora_temp";
        ''')

        # 6. Excluir a tabela temporária
        cursor.execute('DROP TABLE IF EXISTS "Seguradora_temp";')

        # Commit das mudanças
        conn.commit()
        print("Tabela Seguradora atualizada com sucesso.")
    
    except sqlite3.Error as e:
        print(f"Erro ao atualizar a tabela Seguradora: {e}")

def main():
    database = "projetoES3.db"  # O nome do seu banco de dados

    # Criar uma conexão com o banco de dados
    conn = criar_conexao(database)

    if conn:
        # Atualizar a tabela Seguradora
        atualizar_tabela_seguradora(conn)

        # Fechar a conexão
        conn.close()

if __name__ == "__main__":
    main()
