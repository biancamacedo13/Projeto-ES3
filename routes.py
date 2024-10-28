from app import app
from flask import render_template,request, redirect, url_for,flash,jsonify
import sqlite3
import models
import json


USERNAME = "adm"
PASSWORD = "adm4321"

@app.route('/')
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('telaInicio'))  # Corrigido aqui
        elif username == USERNAME and password != PASSWORD:
            return render_template('login.html', erro="Senha incorreta. Tente novamente")
        elif username != USERNAME and password == PASSWORD:
            return render_template('login.html', erro="Usuário incorreto. Tente novamente")
        else:
            return render_template('login.html', erro="Login incorreto. Tente novamente")
    
    return render_template('login.html')

# Telas inicia
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

############################
#CADASTRAR
#######################
#CADASTRAR CLIENTE
@app.route('/cadastrar_cliente.html', methods=['POST', 'GET'])
def cadastrar_cliente():
    # Criar a tabela apenas uma vez no início da aplicação
    models.criar_tabela_cliente()  

    if request.method == 'POST':
        nome = request.form.get('nome_cadastrar_cliente')
        cpf = request.form.get('cpf_cadastrar_cliente')
        email = request.form.get('email_cadastrar_cliente')
        data_nascimento = request.form.get('dt_nasc_cadastrar_cliente')
        endereco = request.form.get('endereco_cadastrar_cliente')
        telefone = str(request.form.get('tel_cadastrar_cliente'))
        profissao = request.form.get('prof_cadastrar_cliente')
        faixa_salarial = float(request.form.get('sal_cadastrar_cliente'))
        condutor_principal = int(request.form.get('condutor_principal_cadastrar_cliente'))
        proprietario = int(request.form.get('proprietario_cadastrar_cliente'))
        estado_civil = request.form.get('civil_cadastrar_cliente')

        if not validar_cpf(cpf):
            erro = "O CPF deve ter exatamente 11 dígitos numéricos."
            return render_template('cadastrar_cliente.html', erro=erro)

        # Convertendo CPF para inteiro após validação
        cpf = int(cpf)

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
        
        except Exception as e:
            return render_template('cadastrar_cliente.html', erro="Ocorreu um erro ao tentar cadastrar o cliente: " + str(e))
            
        finally:
            banco.close()  

    return render_template('cadastrar_cliente.html')

#CADASTRAR VEICULO
@app.route("/cadastrar_veiculo.html", methods=['POST', 'GET'])
def cadastrar_veiculo():
    
    models.criar_tabela_veiculos()

    
    banco = models.criar_conexao()
    cursor = banco.cursor()

        
    cursor.execute("SELECT cpf FROM clientes")
    cpfs = cursor.fetchall() 
    cpfs = [cpf[0] for cpf in cpfs]   

    banco.close()

    if request.method == 'POST':
        cpf_proprietario = request.form.get('cpf_cadastrar_veículo')
        modelo = request.form.get('modelo_cadastrar_veiculo')
        ano = str(request.form.get('ano_cadastrar_veiculo'))   
        cor = request.form.get('cor_cadastrar_veiculo')
        combustivel = request.form.get('combustivel_cadastrar_veiculo')  
        placa = request.form.get('placa_cadastrar_veiculo').strip().upper()
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
            return render_template('cadastrar_veiculo.html', erro="CPF não encontrado no banco de clientes.", cpfs = cpfs)

        # Verificar se a placa já está cadastrada
        cursor.execute("SELECT placa FROM Veiculos WHERE placa = ?", (placa,))
        veiculo_existente = cursor.fetchone()
        if veiculo_existente:
            banco.close()
            return render_template('cadastrar_veiculo.html', erro="Veículo com essa placa já cadastrado.", cpfs=cpfs)

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
            return render_template('cadastrar_veiculo.html', erro="Erro ao cadastrar veículo: " + str(e), cpfs = cpfs)

        finally:
            banco.close()

    return render_template('cadastrar_veiculo.html', cpfs=cpfs)


#CADASTRAR SEGURADORA
@app.route('/cadastrar_seguradora.html', methods=['POST', 'GET'])
def cadastrarSeguradora():
    
    models.criar_tabela_seguradora()  
    
    if request.method == 'POST':
        nome = request.form.get('nome_cadastrar_seguradora')
        cnpj = request.form.get('cnpj_cadastrar_seguradora')
        email = request.form.get('email_cadastrar_seguradora')
        endereco = request.form.get('endereco_cadastrar_seguradora')
        tel = request.form.get('tel_cadastrar_seguradora')

        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:
            cursor.execute("INSERT INTO Seguradora (nome, cnpj, email, endereco, telefone) VALUES (?, ?, ?, ?, ?)", (nome, cnpj, email, endereco, tel))
            banco.commit()
            return render_template('sucesso.html', sucesso="Cadastro Feito com Sucesso!")
        except sqlite3.IntegrityError:
            return render_template('cadastrar_seguradora.html',erro ="O CNPJ já existe no banco de dados.")
        finally:
            banco.close()

    return render_template('cadastrar_seguradora.html')

#CADASTRAR SEGUROS
@app.route('/cadastrar_seguros.html', methods=['POST', 'GET'])
def cadastrarSeguros():
    
    models.criar_tabela_seguros()

    banco = models.criar_conexao()
    cursor = banco.cursor()

    cursor.execute("SELECT cpf FROM clientes")
    cpfs_clientes = cursor.fetchall()     
    cpfs_clientes = [cpf[0] for cpf in cpfs_clientes]  
      
    cursor.execute("SELECT cpf, placa FROM veiculos")
    veiculos_por_cliente = cursor.fetchall()

    # Organizar as placas por CPF em um dicionário
    placas_por_cliente = {}
    for cpf, placa in veiculos_por_cliente:
        if cpf not in placas_por_cliente:
            placas_por_cliente[cpf] = []
        placas_por_cliente[cpf].append(placa)
    
    banco.close()

    if request.method == 'POST':
        cpf = request.form.get('cpf_cadastrar_seguros')
        placa = request.form.get('placa_cadastrar_seguros')
        data_inicio = request.form.get('dt_contratacao_cadastrar_seguros')
        data_termino = request.form.get('dt_vencimento_cadastrar_seguros')
        pagamento = request.form.get('fm_paga_cadastrar_seguros')
        apolice = request.form.get('apolice_cadastrar_seguros')

        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:
            # Verificar se a placa está associada ao CPF fornecido
            cursor.execute("SELECT placa FROM veiculos WHERE cpf = ? AND placa = ?", (cpf, placa))
            placa_associada = cursor.fetchone()

            if not placa_associada:
                return render_template(
                    'cadastrar_seguros.html',
                    erro="Placa não vinculada ao CPF informado.",
                    cpfs_clientes=cpfs_clientes,
                    placas_por_cliente=placas_por_cliente
                )

            # Obter o id_cotacao para a placa selecionada
            cursor.execute("SELECT id_cotacao FROM Cotacoes WHERE placa = ?", (placa,))
            cotacao = cursor.fetchone()

            if not cotacao:
                return render_template(
                    'cadastrar_seguros.html',
                    erro= "Cotação não encontrada para a placa fornecida. Cadastre uma cotação primeiro",
                    cpfs_clientes=cpfs_clientes,
                    placas_por_cliente=placas_por_cliente
                )

            id_cotacao = cotacao[0]

            # Obter o valor total da cotação
            cursor.execute("SELECT valor FROM Cotacoes WHERE id_cotacao = ?", (id_cotacao,))
            valor_total = cursor.fetchone()[0]

            # Inserir o seguro na tabela Seguros
            cursor.execute("""
                INSERT INTO Seguros (apolice, id_cotacao, valor_total, data_inicio, data_termino, pagamento) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (apolice, id_cotacao, valor_total, data_inicio, data_termino, pagamento))

            banco.commit()
            return render_template('sucesso.html', sucesso="Seguro cadastrado com sucesso!")

        except sqlite3.IntegrityError:
            return render_template(
                'cadastrar_seguros.html',
                erro="Erro ao cadastrar: verifique os dados e tente novamente.",
                cpfs_clientes=cpfs_clientes,
                placas_por_cliente=placas_por_cliente
            )

        finally:
            banco.close()  # Fechar a conexão com o banco

    placas_por_cliente_json = json.dumps(placas_por_cliente)#Conexão com JavaScript

    return render_template(
        'cadastrar_seguros.html',
        cpfs_clientes=cpfs_clientes,
        placas_por_cliente=placas_por_cliente_json
    )

#CADASTRAR COTACOES
@app.route('/cadastrar_cotação.html', methods=['POST', 'GET']) 
def cadastrarCotacao():
    cpfs_clientes = []  # Inicializa a variável antes do uso
    seguradoras = []  

    if request.method == 'GET':
        models.criar_tabela_cotacoes()

        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:
            # Obtém os nomes das seguradoras
            cursor.execute("SELECT nome FROM Seguradora")
            seguradoras = cursor.fetchall()    

            # Obtém os CPFs dos clientes
            cursor.execute("SELECT cpf FROM clientes")
            cpfs_clientes = cursor.fetchall()     
            cpfs_clientes = [cpf[0] for cpf in cpfs_clientes]  
        
        finally:
            banco.close()  # Fecha a conexão independentemente de ter ocorrido um erro


        return render_template('cadastrar_cotação.html', seguradoras=[s[0] for s in seguradoras], cpfs_clientes=cpfs_clientes)

    if request.method == 'POST':        
        cpf = int(request.form.get('cpf_cadastrar_cotacao'))
        placa = request.form.get('placa_cadastrar_cotacao')
        nome_seguradora = request.form.get('seguradora_cadastrar_cotacao')
        data_cotacao = request.form.get('dt_cot_cadastrar_cotacao')
        valor = float(request.form.get('valor_cadastrar_cotacao'))

        print(f"CPF: {cpf}, Placa: {placa}, Seguradora: {nome_seguradora}, Data Cotação: {data_cotacao}, Valor: {valor}")

        banco = None  # Inicializa como None
        try:
            banco = models.criar_conexao()
            cursor = banco.cursor()

            # Verifica se o CPF do cliente existe no banco
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
            count_cliente = cursor.fetchone()[0]

            if count_cliente == 0:
                return render_template('cadastrar_cotação.html', erro="O CPF informado não existe no banco de dados.", cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])

            # Verifica se a seguradora existe no banco pelo nome e obtém o CNPJ
            cursor.execute("SELECT cnpj FROM Seguradora WHERE nome = ?", (nome_seguradora,))
            resultado = cursor.fetchone()

            if resultado is None:
                return render_template('cadastrar_cotação.html', erro='Seguradora não encontrada.', cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])
            
            cnpj_seguradora = resultado[0]  # Obtém o CNPJ da seguradora

            # Verifica se a placa existe no banco
            cursor.execute("SELECT COUNT(*) FROM veiculos WHERE placa = ?", (placa,))
            count_placa = cursor.fetchone()[0]

            if count_placa == 0:
                return render_template('cadastrar_cotação.html', erro="A placa informada não existe no banco de dados.", cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])

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
                    return render_template('cadastrar_cotação.html', erro="O CPF informado não existe no banco de dados.", cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])
                elif 'veiculos' in str(e):
                    return render_template('cadastrar_cotação.html', erro="A placa informada não existe no banco de dados.", cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])
            else:
                return render_template('cadastrar_cotação.html', erro="Erro de integridade desconhecido.", cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])

        except Exception as e:
            return render_template('cadastrar_cotação.html', erro=str(e), cpfs_clientes=cpfs_clientes, seguradoras=[s[0] for s in seguradoras])

        finally:
            if banco:  # Verifica se a conexão foi criada antes de tentar fechá-la
                banco.close()

    return render_template('cadastrar_cotação.html', cpfs_clientes=cpfs_clientes, seguradoras=seguradoras)  # Adicione as variáveis ao final para o método GET

#consultar1

@app.route('/consultar_cliente1.html', methods=['POST', 'GET'])
def consultarCliente1():

    banco = models.criar_conexao()
    cursor = banco.cursor()

        
    cursor.execute("SELECT cpf FROM clientes")
    cpfs = cursor.fetchall() 
    cpfs = [cpf[0] for cpf in cpfs]   

    banco.close()

    if request.method == 'POST':
        nome = request.form.get('nome_consultar_cliente1')
        cpf = request.form.get('cpf_consultar_cliente1')
        email = request.form.get('email_consultar_cliente1')

        banco = None  # Inicializa como None

        try:
            banco = models.criar_conexao()
            cursor = banco.cursor()

            # Busca pelo nome
            if nome:
                cursor.execute("SELECT * FROM clientes WHERE nome = ?", (nome,))
                cliente = cursor.fetchone()
                if cliente:
                    return render_template('visualizar_cliente.html', cliente=cliente)

            # Se não encontrou pelo nome, busca pelo CPF
            if cpf:
                cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
                cliente = cursor.fetchone()
                if cliente:
                    return render_template('visualizar_cliente.html', cliente=cliente)

            # Se não encontrou pelo CPF, busca pelo email
            if email:
                cursor.execute("SELECT * FROM clientes WHERE email = ?", (email,))
                cliente = cursor.fetchone()
                if cliente:
                    return render_template('visualizar_cliente.html', cliente=cliente)

            # Se não encontrou nenhum cliente
            return render_template('consultar_cliente1.html', erro="Cliente não encontrado.")

        except Exception as e:
            return render_template('consultar_cliente1.html', erro=str(e))

        finally:
            if banco:  # Verifica se a conexão foi criada antes de tentar fechá-la
                banco.close()

    return render_template('consultar_cliente1.html', cpfs=cpfs)


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

#EXTRAS
@app.route('/buscar_placas', methods=['GET'])
def buscar_placas():
    cpf = request.args.get('cpf')  # Obter o CPF dos parâmetros da URL
    banco = models.criar_conexao()
    cursor = banco.cursor()

    cursor.execute("SELECT placa FROM veiculos WHERE cpf = ?", (cpf,))
    placas = cursor.fetchall()
    banco.close()

    # Retornar as placas em formato JSON
    return json.dumps([placa[0] for placa in placas])

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11