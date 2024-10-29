import sqlite3

# Conectando ao banco de dados
banco = sqlite3.connect('projetoES3.db')  # Substitua pelo caminho do seu banco de dados
cursor = banco.cursor()

# Dados das seguradoras
seguradoras = [
    ("Bradesco Seguros", "60746948000111", "atendimento@bradescoseguros.com.br", "Av. Brig. Faria Lima, 3200 - São Paulo, SP", "0800570570"),
    ("Mapfre Seguros", "60252211000122", "contato@mapfre.com.br", "Rua das Figueiras, 123 - São Paulo, SP", "1130784400"),
    ("Allianz Seguros", "44242729000167", "contato@allianz.com.br", "Rua São Bento, 100 - São Paulo, SP", "08007770200"),
    ("SulAmérica Seguros", "28855144000100", "atendimento@sulamericaseguros.com.br", "Av. das Américas, 3500 - Rio de Janeiro, RJ", "08007231212"),
    ("Tokio Marine", "67051512000112", "atendimento@tokio.com.br", "Av. Prestes Maia, 100 - São Paulo, SP", "1130039262"),
    ("HDI Seguros", "76307816000130", "atendimento@hdi.com.br", "Av. Barão do Rio Branco, 123 - São Paulo, SP", "0800400400")
]


# Inserir as seguradoras no banco de dados
try:
    cursor.executemany("INSERT INTO Seguradora (nome, cnpj, email, endereco, telefone) VALUES (?, ?, ?, ?, ?)", seguradoras)
    banco.commit()
    print("Seguradoras inseridas com sucesso.")
except sqlite3.IntegrityError as e:
    print(f"Erro de integridade: {e}")
finally:
    banco.close()
