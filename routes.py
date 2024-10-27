from app import app
from flask import render_template,request, redirect, url_for
import sqlite3
import models

@app.route("/login.html")
def login():
    return render_template('login.html')

#telas_iniciais

@app.route("/tela_inicial.html")
def telaInicio():
    return render_template('tela_inicial.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/clientes.html')
def clientes():
    return render_template('clientes.html')

@app.route('/seguradoras.html')
def seguradoras():
    return render_template('seguradoras.html')

@app.route('/seguros.html')
def seguros():
    return render_template('seguros.html')

@app.route('/cotações.html')
def cotacoes():
    return render_template('cotações.html')

#TELAS CADASTRAR
#CADASTRAR CLIENTE
@app.route("/")
@app.route('/cadastrar_cliente.html', methods=['POST', 'GET'])
def cadastrar_cliente():
    # Criar a tabela apenas uma vez no início da aplicação
    models.criar_tabela_cliente()  

    if request.method == 'POST':
        nome = request.form.get('nome_cadastrar_cliente')
        cpf = int(request.form.get('cpf_cadastrar_cliente'))
        email = request.form.get('email_cadastrar_cliente')
        data_nascimento = request.form.get('dt_nasc_cadastrar_cliente')
        endereco = request.form.get('endereco_cadastrar_cliente')
        telefone = request.form.get('tel_cadastrar_cliente')
        profissao = request.form.get('prof_cadastrar_cliente')
        faixa_salarial = request.form.get('sal_cadastrar_cliente')
        condutor_principal = request.form['condutor_principal_cadastrar_cliente']
        proprietario = request.form.get('proprietario_cadastrar_cliente')
        estado_civil = request.form.get('civil_cadastrar_cliente')

        print("Nome:", nome)
        print("CPF:", cpf)
        print("Email:", email)
        print("Data de Nascimento:", data_nascimento)
        print("Endereço:", endereco)
        print("Telefone:", telefone)
        print("Profissão:", profissao)
        print("Faixa Salarial:", faixa_salarial)
        print("Condutor Principal", condutor_principal)
        print("Proprietario", proprietario)
        print("Estado Civil:", estado_civil)
        
        if condutor_principal is None:
            condutor_principal = 1  
        else:
            condutor_principal = int(condutor_principal)

        if proprietario is None:
            proprietario = 1
        else:
            proprietario = int(proprietario)

        
        campos_vazios = []

        # Verificando quais campos estão vazios
        if not nome:
            campos_vazios.append('Nome')
        if not cpf:
            campos_vazios.append('CPF')
        if not email:
            campos_vazios.append('E-mail')
        if not data_nascimento:
            campos_vazios.append('Data de Nascimento')
        if not endereco:
            campos_vazios.append('Endereço')
        if not telefone:
            campos_vazios.append('Telefone')
        if not profissao:
            campos_vazios.append('Profissão')
        if not faixa_salarial:
            campos_vazios.append('Faixa Salarial')
        if not estado_civil:
            campos_vazios.append('Estado Civil')

        # Se houver campos vazios, cria a mensagem de erro
        if campos_vazios:
            campos_faltando = ', '.join(campos_vazios)
            return render_template('cadastrar_cliente.html', erro=f"Por favor, preencha os seguintes campos: {campos_faltando}.")

        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:
            cursor.execute('''
                INSERT INTO clientes (
                    cpf, nome, email, data_nascimento, endereco,
                    telefone, profissao, faixa_salarial,
                    condutor_principal, proprietario, estado_civil
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (cpf, nome, email, data_nascimento, endereco,
                  telefone, profissao, faixa_salarial,
                  condutor_principal, proprietario, estado_civil))
            banco.commit()
            return render_template('sucesso.html', sucesso="Cliente cadastrado com sucesso!")  
        
        except sqlite3.IntegrityError as e:
            # Verifica qual campo causou o erro
            if 'UNIQUE constraint failed: clientes.nome' in str(e):
                return render_template('cadastrar_cliente.html', erro="O nome já existe no banco de dados.")
            elif 'UNIQUE constraint failed: clientes.cpf' in str(e):
                return render_template('cadastrar_cliente.html', erro="O CPF já existe no banco de dados.")
            else:
                return render_template('cadastrar_cliente.html', erro="Erro de integridade desconhecido.")
            
        finally:
            banco.close()  

    return render_template('cadastrar_cliente.html')

@app.route('/cadastrar_veiculo.html')
def cadastrarVeiculo():
    return render_template('/cadastrar_veiculo.html')


#CADASTRAR SEGURADORA
@app.route('/cadastrar_seguradora.html', methods=['POST', 'GET'])
def cadastrarSeguradora():
    # Criar a tabela apenas uma vez no início da aplicação
    models.criar_tabela_seguradora()  
    
    if request.method == 'POST':
        nome = request.form.get('nome_cadastrar_seguradora')
        cnpj = request.form.get('cnpj_cadastrar_seguradora')
        email = request.form.get('email_cadastrar_seguradora')
        endereco = request.form.get('endereco_cadastrar_seguradora')
        tel = request.form.get('tel_cadastrar_seguradora')

        # Estabelecer a conexão com o banco de dados aqui
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:
            cursor.execute("INSERT INTO Seguradora (nome, cnpj, email, endereco, telefone) VALUES (?, ?, ?, ?, ?)", (nome, cnpj, email, endereco, tel))
            banco.commit()
            return render_template('sucesso.html', sucesso="Cadastro Feito com Sucesso!")
        except sqlite3.IntegrityError:
            return render_template('cadastrar_seguradora.html',erro ="O CNPJ já existe no banco de dados.")
        finally:
            banco.close()  # Sempre feche a conexão, independentemente do resultado

    return render_template('cadastrar_seguradora.html')

@app.route('/cadastrar_seguros.html')
def cadastrarSeguros():
    return render_template('/cadastrar_seguros.html')

@app.route('/cadastrar_cotação.html')
def cadastrarCotacao():
    return render_template('/cadastrar_cotação.html')

#consultar1
@app.route('/consultar_cliente1.html')
def consultarCliente1():
    return render_template('/consultar_cliente1.html')

@app.route('/consultar_veículo.html')
def consultarVeiculo1():
    return render_template('/consultar_veículo.html')

@app.route('/consultar_seguradora.html')
def consultarSeguradora1():
    return render_template('/consultar_seguradora.html')

@app.route('/consultar_seguros.html')
def consultarSeguros1():
    return render_template('/consultar_seguros.html')

@app.route('/consultar_cotação1.html')
def consultarCotacoes1():
    return render_template('/consultar_cotação1.html')

#consultar2
@app.route('/consultar_cliente2.html')
def consultarCliente2():
    return render_template('/consultar_cliente2.html')

@app.route('/consultar_veículo2.html')
def consultarVeiculo2():
    return render_template('/consultar_veículo2.html')

@app.route('/consultar_seguradora2.html')
def consultarSeguradora2():
    return render_template('/consultar_seguradora2.html')

@app.route('/consultar_seguros2.html')
def consultarSeguros2():
    return render_template('/consultar_seguros2.html')

@app.route('/consultar_cotações2.html')
def consultarCotacoes2():
    return render_template('/consultar_cotações2.html')

#visualizar
@app.route('/visualizar_cliente.html')
def visualizarCliente():
    return render_template('/visualizar_cliente.html')

@app.route('/visualizar_veículo.html')
def visualizarVeiculo():
    return render_template('/visualizar_veículo.html')

@app.route('/visualizar_seguradora.html')
def visualizarSeguradora():
    return render_template('/visualizar_seguradora.html')

@app.route('/visualizar_seguros.html')
def visualizarSeguros():
    return render_template('/visualizar_seguros.html')

@app.route('/visualizar_cotações.html')
def visualizarCotacoes():
    return render_template('/visualizar_cotações.html')

#Sucesso
@app.route('/sucesso.html')
def sucesso():
    return render_template('/sucesso.html')