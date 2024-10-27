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
        faixa_salarial = float(request.form.get('sal_cadastrar_cliente'))
        condutor_principal = int(request.form.get('condutor_principal_cadastrar_cliente'))
        proprietario = int(request.form.get('proprietario_cadastrar_cliente'))
        estado_civil = request.form.get('civil_cadastrar_cliente')

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
            error_message = str(e)

            if 'UNIQUE constraint failed: clientes.nome' in error_message:
                return render_template('cadastrar_cliente.html', erro="O nome já existe no banco de dados.")
            elif 'UNIQUE constraint failed: clientes.cpf' in error_message:
                return render_template('cadastrar_cliente.html', erro="O CPF já existe no banco de dados.")
            else:
                return render_template('cadastrar_cliente.html', erro="Erro de integridade desconhecido.")
        
        except Exception as e:
            return render_template('cadastrar_cliente.html', erro="Ocorreu um erro ao tentar cadastrar o cliente: " + str(e))
            
        finally:
            banco.close()  

    return render_template('cadastrar_cliente.html')

#CADASTRAR VEICULO

@app.route("/cadastrar_veiculo.html", methods=['POST', 'GET'])
def cadastrar_veiculo():
    
    models.criar_tabela_veiculos()

    if request.method == 'POST':
        cpf_proprietario = request.form.get('cpf_cadastrar_veículo')
        modelo = request.form.get('modelo_cadastrar_veiculo')
        ano = request.form.get('ano_cadastrar_veiculo')  
        cor = request.form.get('cor_cadastrar_veiculo')
        combustivel = request.form.get('combustivel_cadastrar_veiculo')  
        placa = request.form.get('placa_cadastrar_veiculo')
        chassi = request.form.get('chassi_cadastrar_veiculo')
        pernoite = request.form.get('pernoite_cadastrar_veiculo')  
        cep_pernoite = int(request.form.get('cep_pernoite_cadastrar_veiculo'))  
        garagem = int(request.form.get('garagem_cadastrar_veiculo'))  
        rastreador = int(request.form.get('rastreador_cadastrar_veiculo'))  
        remunerada = int(request.form.get('remunerada_cadastrar_veiculo'))  
        ir_trabalho_estudo = int(request.form.get('ir_cadastrar_veiculo'))  
        estacionamento = int(request.form.get('estacionamento_cadastrar_veiculo'))  
        

        # Verificar se o CPF é válido e se o cliente existe no banco
        if not models.validar_cpf(cpf_proprietario):
            return render_template('cadastrar_veiculo.html', erro="CPF inválido.")
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        # Verificar se o CPF existe na tabela clientes
        cursor.execute("SELECT cpf FROM clientes WHERE cpf = ?", (cpf_proprietario,))
        cliente = cursor.fetchone()
        if not cliente:
            banco.close()
            return render_template('cadastrar_veiculo.html', erro="CPF não encontrado no banco de clientes.")

        try:
            # Inserir os dados do veículo
            cursor.execute('''
                INSERT INTO Veiculos (
                    cpf, modelo, ano, cor, chassi, combustivel, placa, pernoite, cep_pernoite, 
                    garagem, rastreador, remunerada, ir_trabalho_estudo, estacionamento
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (cpf_proprietario, modelo, ano, cor, chassi, combustivel, placa, pernoite, cep_pernoite, 
                  garagem, rastreador, remunerada, ir_trabalho_estudo, estacionamento))
            banco.commit()
            return render_template('sucesso.html', sucesso="Veículo cadastrado com sucesso!")

        except Exception as e:
            return render_template('cadastrar_veiculo.html', erro="Erro ao cadastrar veículo: " + str(e))

        finally:
            banco.close()

    return render_template('cadastrar_veiculo.html')


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


@app.route('/cadastrar_seguros.html', methods=['POST', 'GET'])
def cadastrarSeguros():

    return render_template('/cadastrar_seguros.html')

@app.route("/")
@app.route('/cadastrar_cotação.html', methods=['POST', 'GET'])
def cadastrarCotacao():    
    
    models.criar_tabela_cotacoes()  

    if request.method == 'POST':        
        cpf = int(request.form.get('cpf_cadastrar_cotacao'))
        placa = request.form.get('placa_cadastrar_cotacao')
        nome_seguradora = request.form.get('seguradora_cadastrar_cotacao')
        data_cotacao = request.form.get('dt_cot_cadastrar_cotacao')
        valor = float(request.form.get('valor_cadastrar_cotacao'))

        banco = None  # Inicializa como None
        try:
            banco = models.criar_conexao()
            cursor = banco.cursor()

            # Verifica se o CPF do cliente existe no banco
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
            count_cliente = cursor.fetchone()[0]

            if count_cliente == 0:
                return render_template('cadastrar_cotação.html', erro="O CPF informado não existe no banco de dados.")

            # Verifica se a seguradora existe no banco pelo nome e obtém o CNPJ
            cursor.execute("SELECT cnpj FROM Seguradora WHERE nome = ?", (nome_seguradora,))
            resultado = cursor.fetchone()

            if resultado is None:
                return render_template('cadastrar_cotação.html', erro="Seguradora não encontrada.")
            
            cnpj_seguradora = resultado[0]  # Obtém o CNPJ da seguradora

            # Insere a cotação
            cursor.execute('''INSERT INTO Cotacoes (
                cpf, placa, cnpj_seguradora, data_inicio, valor
            ) VALUES (?, ?, ?, ?, ?)''', (cpf, placa, cnpj_seguradora, data_cotacao, valor))

            banco.commit()
            return render_template('sucesso.html', sucesso="Cotação cadastrada com sucesso!")

        except sqlite3.IntegrityError as e:
            # Verifica qual campo causou o erro
            if 'FOREIGN KEY constraint failed' in str(e):
                if 'clientes' in str(e):
                    return render_template('cadastrar_cotação.html', erro="O CPF informado não existe no banco de dados.")
                elif 'veiculos' in str(e):
                    return render_template('cadastrar_cotação.html', erro="A placa informada não existe no banco de dados.")
            else:
                return render_template('cadastrar_cotação.html', erro="Erro de integridade desconhecido.")

        except Exception as e:
            return render_template('cadastrar_cotação.html', erro=str(e))

        finally:
            if banco:  # Verifica se a conexão foi criada antes de tentar fechá-la
                banco.close()

    return render_template('cadastrar_cotação.html')

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