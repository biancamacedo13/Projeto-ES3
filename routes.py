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
@app.route("/")
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
     models.criar_tabela_seguros()  
     if request.method == 'POST':
        apolice = int(request.form.get('apolice'))
        id_cotacao = int(request.form.get('id_cotacao'))
        cpf = int(request.form.get('cpf'))
        data_inicio = request.form.get('data_inicio')
        data_vencimento = request.form.get('data_vencimento')
        forma_pagamento = request.form.get('forma_pagamento')

      banco = models.criar_conexao()
      cursor = banco.cursor()

      try:
            cursor.execute('''
                INSERT INTO Seguros (
                    apolice, id_cotacao, cpf, data_inicio, data_vencimento, forma_pagamento
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (apolice, id_cotacao, cpf, data_inicio, data_vencimento, forma_pagamento))
            
            banco.commit()
            return render_template('sucesso.html', sucesso="Seguro cadastrado com sucesso!")

        except sqlite3.IntegrityError as e:            
            if 'UNIQUE constraint failed: Seguros.apolice' in str(e):
                return render_template('cadastrar_seguros.html', erro="O número da apólice já existe no banco de dados.")
            elif 'FOREIGN KEY constraint failed' in str(e):
                return render_template('cadastrar_seguros.html', erro="O ID da cotação não existe no banco de dados.")
            else:
                return render_template('cadastrar_seguros.html', erro="Erro de integridade desconhecido.")

        finally:
            banco.close()      

    return render_template('/cadastrar_seguros.html')

# Função para cadastrar Cotações
@app.route('/cadastrar_cotação.html', methods=['POST', 'GET'])
def cadastrarCotacao():    
    models.criar_tabela_cotacoes()

    if request.method == 'POST':        
        placa = request.form.get('placa')
        cpf = request.form.get('cpf')
        data_inicio = request.form.get('data_inicio')
        data_termino = request.form.get('data_termino')
        vencimento = request.form.get('vencimento')
        valor = float(request.form.get('valor'))

        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:
            cursor.execute('''
                INSERT INTO Cotacoes (
                    placa, cpf, data_inicio, data_termino, vencimento, valor
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (placa, cpf, data_inicio, data_termino, vencimento, valor))

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

        finally:
            banco.close()
        return render_template('/cadastrar_cotação.html')

#consultar1
@app.route('/consultar_cliente1.html', methods=['POST', 'GET'])
def consultarCliente1():
    if request.method == 'POST':
        #get filtros
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        email = request.form.get('email')

        
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM clientes WHERE cpf = ? OR nome = ? OR email = ?"
            cursor.execute(query, (cpf, nome))
            cliente = cursor.fetchone()  # busca primeira linha
           
            if cliente:
                cliente_data = {
                    'cpf': cliente[0],
                    'nome': cliente[1],
                    'email': cliente[2],
                    'data_nascimento': cliente[3],
                    'endereco': cliente[4],
                    'telefone': cliente[5],
                    'profissao': cliente[6],
                    'faixa_salarial': cliente[7],
                    'condutor_principal': 'Sim' if cliente[8] == 1 else 'Não',
                    'proprietario': 'Sim' if cliente[9] == 1 else 'Não',
                    'estado_civil': cliente[10]
                }
                return render_template('consultar_cliente1.html', cliente=cliente_data)
            else:
                return render_template('consultar_cliente1.html', erro="Cliente não encontrado.")

        except sqlite3.Error as e:
            return render_template('consultar_cliente1.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()
    
    return render_template('/consultar_cliente1.html')

@app.route('/consultar_veículo.html', methods=['POST', 'GET'])
def consultarVeiculo1():
    if request.method == 'POST':        
        cpf = request.form.get('cpf_consultar_veiculo')
        placa = request.form.get('placa_consultar_veiculo')
        chassi = request.form.get('chassi_consultar_veiculo')
       
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM Veiculos WHERE cpf = ? OR placa = ? OR chassi = ?"
            cursor.execute(query, (placa,))
            veiculo = cursor.fetchone()  
            
            if veiculo:
                veiculo_data = {
                    'cpf': veiculo[0],
                    'modelo': veiculo[1],
                    'ano': veiculo[2],
                    'cor': veiculo[3],
                    'chassi': veiculo[4],
                    'combustivel': veiculo[5],
                    'placa': veiculo[6],
                    'pernoite': 'Sim' if veiculo[7] == 1 else 'Não',,
                    'cep_pernoite': veiculo[8],
                    'garagem': 'Sim' if veiculo[9] == 1 else 'Não',,
                    'rastreador': 'Sim' if veiculo[10] == 1 else 'Não',
                    'remunerada': 'Sim' if veiculo[11] == 1 else 'Não',,
                    'ir_trabalho_estudo': 'Sim' if veiculo[12] == 1 else 'Não',
                    'estacionamento': 'Sim' if veiculo[13] == 1 else 'Não'
                }
                return render_template('consultar_veículo.html', veiculo=veiculo_data)
            else:
                return render_template('consultar_veículo.html', erro="Veículo não encontrado.")

        except Exception as e:
            return render_template('consultar_veículo.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close()            
    return render_template('/consultar_veículo.html')

@app.route('/consultar_seguradora.html', methods=['POST', 'GET'])
def consultarSeguradora1():
    if request.method == 'POST':
        # get filtros
        nome = request.form.get('nome')
        cnpj = request.form.get('cnpj')

        # conexao
        banco = models.criar_conexao()
        cursor = banco.cursor()

       
        try:
            query = "SELECT * FROM Seguradora WHERE nome = ? OR cnpj = ?"
            cursor.execute(query, (cnpj, nome))
            seguradora = cursor.fetchone()  # busca primeira linha

            
            if seguradora:
                seguradora_data = {
                    'nome': seguradora[0],
                    'cnpj': seguradora[1],
                    'endereco': seguradora[2],
                    'telefone': seguradora[3],
                    'email': seguradora[4]
                }
                return render_template('consultar_seguradora.html', seguradora=seguradora_data)
            else:
                return render_template('consultar_seguradora.html', erro="Seguradora não encontrada.")

        except sqlite3.Error as e:
            return render_template('consultar_seguradora.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()
    
    return render_template('/consultar_seguradora.html')

@app.route('/consultar_seguros.html', methods=['POST', 'GET'])
def consultarSeguros1():
    if request.method == 'POST':
        # get filtros
        cnpj = request.form.get('cnpj')
        placa = request.form.get('placa')
        data_vencimento = request.form.get('data_vencimento')

        # conexao
        banco = models.criar_conexao()
        cursor = banco.cursor()

       
        try:
            query = "SELECT * FROM Seguros WHERE cnpj = ? OR placa = ? OR data_vencimento = ?"
            cursor.execute(query, (apolice, id_cotacao))
            seguro = cursor.fetchone()  # busca primeiro resultado

            
            if seguro:
                seguro_data = {
                    'apolice': seguro[0],
                    'id_cotacao': seguro[1],
                    'cpf': seguro[3],
                    'nome': seguro[4],                    
                    'data_inicio': seguro[5],
                    'data_vencimento': seguro[6],
                    'forma_pagamento': seguro[7]
                }
                return render_template('consultar_seguros.html', seguro=seguro_data)
            else:
                return render_template('consultar_seguros.html', erro="Seguro não encontrado.")

        except sqlite3.Error as e:
            return render_template('consultar_seguros.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()
    
    return render_template('/consultar_seguros.html')

@app.route('/consultar_cotação1.html', methods=['POST', 'GET'])
def consultarCotacoes1():
    if request.method == 'POST': 
        # get filtro
        id_cotacao = request.form.get('id_cotacao')
        cpf = request.form.get('cpf')
        placa = request.form.get('placa')
       # conexao
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM Cotacoes WHERE id_cotacao = ? OR cpf = ? OR placa = ?"
            cursor.execute(query, (id_cotacao, cpf, placa))
            cotacao = cursor.fetchone()  # busca primeira linha 

            # verifica
            if cotacao:
                cotacao_data = {
                    'id_cotacao': cotacao[0],
                    'placa': cotacao[1],
                    'cpf': cotacao[2],
                    'data_inicio': cotacao[3],
                    'data_termino': cotacao[4],
                    'vencimento': cotacao[5],
                    'valor': cotacao[6]
                }
                return render_template('consultar_cotação1.html', cotacao=cotacao_data)
            else:
                return render_template('consultar_cotação1.html', erro="Cotação não encontrada.")

        except sqlite3.Error as e:
            return render_template('consultar_cotação1.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()
   
    return render_template('/consultar_cotação1.html')

#consultar2
@app.route('/consultar_cliente2.html', methods=['POST', 'GET'])
def consultarCliente2():
    if request.method == 'POST':        
        cliente1 = request.form.get('cliente_1')
        cliente2 = request.form.get('cliente_2')
        cliente3 = request.form.get('cliente_3')
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:            
            clientes_encontrados = []
            
            if cliente1:
                cursor.execute("SELECT * FROM clientes WHERE cpf = ? OR nome = ? OR email = ?", (cliente1, cliente1))
                cliente_data = cursor.fetchone()
                if cliente_data:
                    cliente_encontrados.append(cliente_data)

            if cliente2:
                cursor.execute("SELECT * FROM clientes WHERE cpf = ? OR nome = ? OR email = ?", (cliente2, cliente2))
                cliente_data = cursor.fetchone()
                if cliente_data:
                    clientes_encontrados.append(cliente_data)

            if veiculo3:
                cursor.execute("SELECT * FROM clientes WHERE cpf = ? OR nome = ? OR email = ?", (cliente3, cliente3))
                cliente_data = cursor.fetchone()
                if cliente_data:
                    clientes_encontrados.append(cliente_data)
           
            if cliente_encontrados:
                return render_template('consultar_cliente2.html', clientes=clientes_encontrados)
            else:
                return render_template('consultar_cliente2.html', erro="Nenhum cliente encontrado.")

        except Exception as e:
            return render_template('consultar_cliente2.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close()    
    return render_template('/consultar_cliente2.html')

@app.route('/consultar_veículo2.html', methods=['POST', 'GET'])
def consultarVeiculo2():
    if request.method == 'POST':        
        veiculo1 = request.form.get('veiculo_1')
        veiculo2 = request.form.get('veiculo_2')
        veiculo3 = request.form.get('veiculo_3')
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:            
            veiculos_encontrados = []
            
            if veiculo1:
                cursor.execute("SELECT * FROM Veiculos WHERE cpf = ? OR placa = ? OR chassi = ?", (veiculo1, veiculo1))
                veiculo_data = cursor.fetchone()
                if veiculo_data:
                    veiculos_encontrados.append(veiculo_data)

            if veiculo2:
                cursor.execute("SELECT * FROM Veiculos WHERE cpf = ? OR placa = ? OR chassi = ?", (veiculo2, veiculo2))
                veiculo_data = cursor.fetchone()
                if veiculo_data:
                    veiculos_encontrados.append(veiculo_data)

            if veiculo3:
                cursor.execute("SELECT * FROM Veiculos WHERE cpf = ? OR placa = ? OR chassi = ?", (veiculo3, veiculo3))
                veiculo_data = cursor.fetchone()
                if veiculo_data:
                    veiculos_encontrados.append(veiculo_data)
           
            if veiculos_encontrados:
                return render_template('consultar_veículo2.html', veiculos=veiculos_encontrados)
            else:
                return render_template('consultar_veículo2.html', erro="Nenhum veículo encontrado.")

        except Exception as e:
            return render_template('consultar_veículo2.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close()    
    
    return render_template('/consultar_veículo2.html')

@app.route('/consultar_seguradora2.html', methods=['POST', 'GET'])
def consultarSeguradora2():
        if request.method == 'POST':        
        seguradora1 = request.form.get('seguradora_1')
        seguradora2 = request.form.get('seguradora_2')
        seguradora3 = request.form.get('seguradora_3')
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:            
            seguradoras_encontradas = []
            
            if seguradora1:
                cursor.execute("SELECT * FROM Seguradora WHERE nome = ? OR cnpj = ?", (seguradora1, seguradora1))
                seguradora_data = cursor.fetchone()
                if seguradora_data:
                    seguradoras_encontradas.append(seguradora_data)

            if seguradora2:
                cursor.execute("SELECT * FROM Seguradora WHERE nome = ? OR cnpj = ?", (seguradora2, seguradora2))
                seguradora_data = cursor.fetchone()
                if seguradora_data:
                    seguradoras_encontradas.append(seguradora_data)

            if seguradora3:
                cursor.execute("SELECT * FROM Seguradora WHERE nome = ? OR cnpj = ?", (seguradora3, seguradora3))
                seguradora_data = cursor.fetchone()
                if seguradora_data:
                    seguradoras_encontradas.append(seguradora_data)
           
            if seguradoras_encontradas:
                return render_template('consultar_seguradora2.html', seguradoras=seguradoras_encontradas)
            else:
                return render_template('consultar_seguradora2.html', erro="Nenhuma seguradora encontrada.")

        except Exception as e:
            return render_template('consultar_seguradora2.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close() 
            
    return render_template('/consultar_seguradora2.html')

@app.route('/consultar_seguros2.html', methods=['POST', 'GET'])
def consultarSeguros2():
    if request.method == 'POST':        
        seguro1 = request.form.get('seguro1')
        seguro2 = request.form.get('seguro2')
        seguro3 = request.form.get('seguro3')
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:            
            seguros_encontrados = []
            
            if seguro1:
                cursor.execute("SELECT * FROM Seguros WHERE cnpj = ? OR placa = ? OR data_vencimento = ?", (seguro1, seguro1))
                seguro_data = cursor.fetchone()
                if seguro_data:
                    seguros_encontrados.append(seguro_data)

            if seguro2:
                cursor.execute("SELECT * FROM Seguros WHERE cnpj = ? OR placa = ? OR data_vencimento = ?", (seguro2, seguro2))
                seguro_data = cursor.fetchone()
                if seguro_data:
                    seguros_encontrados.append(seguro_data)

            if seguro3:
                cursor.execute("SELECT * FROM Seguros WHERE cnpj = ? OR placa = ? OR data_vencimento = ?", (seguro3, seguro3))
                seguro_data = cursor.fetchone()
                if seguro_data:
                    seguros_encontrados.append(seguro_data)
           
            if seguros_encontrados:
                return render_template('consultar_seguros2.html', seguros=seguros_encontrados)
            else:
                return render_template('consultar_seguros2.html', erro="Nenhum seguro encontrado.")

        except Exception as e:
            return render_template('consultar_seguros2.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close() 
    return render_template('/consultar_seguros2.html')

@app.route('/consultar_cotações2.html')
def consultarCotacoes2():
    if request.method == 'POST':        
        cotacao1 = request.form.get('cotacao1')
        cotacao2 = request.form.get('cotacao2')
        cotacao3 = request.form.get('cotacao3')
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        try:            
            cotacoes_encontradas = []
            
            if cotacao1:
                cursor.execute("SELECT * FROM Cotacoes WHERE id_cotacao = ? OR cpf = ? OR placa = ?", (cotacao1, cotacao1))
                cotacao_data = cursor.fetchone()
                if cotacao_data:
                    cotacoes_encontradas.append(cotacao_data)

            if cotacao2:
                cursor.execute("SELECT * FROM Cotacoes WHERE id_cotacao = ? OR cpf = ? OR placa = ?", (cotacao2, cotacao2))
                cotacao_data = cursor.fetchone()
                if cotacao_data:
                    cotacoes_encontradas.append(cotacao_data)

            if cotacao3:
                cursor.execute("SELECT * FROM Cotacoes WHERE id_cotacao = ? OR cpf = ? OR placa = ?", (cotacao3, cotacao3))
                cotacao_data = cursor.fetchone()
                if cotacao_data:
                    cotacoes_encontradas.append(cotacao_data)
           
            if cotacoes_encontradas:
                return render_template('consultar_cotações2.html', cotacoes=cotacoes_encontradas)
            else:
                return render_template('consultar_cotações2.html', erro="Nenhuma cotação encontrado.")

        except Exception as e:
            return render_template('consultar_cotações2.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close() 

    return render_template('/consultar_cotações2.html')

#visualizar
@app.route('/visualizar_cliente.html', methods=['POST', 'GET'])
def visualizarCliente():
    if request.method == 'POST':       
        cpf = request.form.get('cpf')

       
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM clientes WHERE cpf = ?"
            cursor.execute(query, (cpf,))
            cliente = cursor.fetchone()  
            
            if cliente:
                cliente_data = {
                    'cpf': cliente[0],
                    'nome': cliente[1],
                    'email': cliente[2],
                    'data_nascimento': cliente[3],
                    'endereco': cliente[4],
                    'telefone': cliente[5],
                    'profissao': cliente[6],
                    'faixa_salarial': cliente[7],
                    'condutor_principal': 'Sim' if cliente[8] == 1 else 'Não',
                    'proprietario': 'Sim' if cliente[9] == 1 else 'Não',
                    'estado_civil': cliente[10]
                }
                return render_template('visualizar_cliente.html', cliente=cliente_data)
            else:
                return render_template('visualizar_cliente.html', erro="Cliente não encontrado.")

        except sqlite3.Error as e:
            return render_template('visualizar_cliente.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()    
    
    return render_template('/visualizar_cliente.html')

@app.route('/visualizar_veículo.html', methods=['POST', 'GET'])
def visualizarVeiculo():
    if request.method == 'POST':       
        placa = request.form.get('placa_veiculo')
        
        banco = models.criar_conexao()
        cursor = banco.cursor()

        
        try:
            query = "SELECT * FROM Veiculos WHERE placa = ?"
            cursor.execute(query, (placa,))
            veiculo = cursor.fetchone()  
            
            if veiculo:
                veiculo_data = {
                    'cpf': veiculo[0],
                    'modelo': veiculo[1],
                    'ano': veiculo[2],
                    'cor': veiculo[3],
                    'chassi': veiculo[4],
                    'combustivel': veiculo[5],
                    'placa': veiculo[6],
                    'pernoite': 'Sim' if veiculo[7] == 1 else 'Não',,
                    'cep_pernoite': veiculo[8],
                    'garagem': 'Sim' if veiculo[9] == 1 else 'Não',,
                    'rastreador': 'Sim' if veiculo[10] == 1 else 'Não',
                    'remunerada': 'Sim' if veiculo[11] == 1 else 'Não',,
                    'ir_trabalho_estudo': 'Sim' if veiculo[12] == 1 else 'Não',
                    'estacionamento': 'Sim' if veiculo[13] == 1 else 'Não'
                }
                return render_template('visualizar_veículo.html', veiculo=veiculo_data)
            else:
                return render_template('visualizar_veículo.html', erro="Veículo não encontrado.")

        except Exception as e:
            return render_template('visualizar_veículo.html', erro="Erro ao consultar o banco de dados: " + str(e))

        finally:
            banco.close()            
    return render_template('/visualizar_veículo.html')

@app.route('/visualizar_seguradora.html', methods=['POST', 'GET'])
def visualizarSeguradora():
    if request.method == 'POST':        
        seguradora = request.form.get('cnpj')

        #conexao
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM Seguradora WHERE cnpj = ?"
            cursor.execute(query, (cnpj,))
            seguradora = cursor.fetchone()  
            
            if seguradora:
                seguradora_data = {
                    'nome': seguradora[0],
                    'cnpj': seguradora[1],
                    'endereco': seguradora[2],
                    'telefone': seguradora[3],
                    'email': seguradora[4]
                }
                return render_template('visualizar_seguradora.html', seguradora=seguradora_data)
            else:
                return render_template('visualizar_seguradora.html', erro="Seguradora não encontrado.")

        except sqlite3.Error as e:
            return render_template('visualizar_seguradora.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()
    return render_template('/visualizar_seguradora.html')

@app.route('/visualizar_seguros.html', methods=['POST', 'GET'])
def visualizarSeguros():
    if request.method == 'POST':        
        apolice = request.form.get('apolice')

        #conexao
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM Seguros WHERE apolice = ?"
            cursor.execute(query, (apolice,))
            seguros = cursor.fetchone()  
            
            if seguros:
                seguros_data = {
                    'apolice': seguro[0],
                    'id_cotacao': seguro[1],
                    'cpf': seguro[3],
                    'nome': seguro[4],                    
                    'data_inicio': seguro[5],
                    'data_vencimento': seguro[6],
                    'forma_pagamento': seguro[7]
                }
                return render_template('visualizar_seguros.html', seguros=seguros_data)
            else:
                return render_template('visualizar_seguros.html', erro="Seguro não encontrado.")

        except sqlite3.Error as e:
            return render_template('visualizar_seguros.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()
    return render_template('/visualizar_seguros.html')

@app.route('/visualizar_cotacao.html', methods=['POST', 'GET'])
def visualizarCotacao():
    if request.method == 'POST':        
        id_cotacao = request.form.get('id_cotacao')

        #conexao
        banco = models.criar_conexao()
        cursor = banco.cursor()
        
        try:
            query = "SELECT * FROM Cotacoes WHERE id_cotacao = ?"
            cursor.execute(query, (id_cotacao,))
            cotacao = cursor.fetchone()  
            
            if cotacao:
                cotacao_data = {
                    'id_cotacao': cotacao[0],
                    'placa': cotacao[1],
                    'cpf': cotacao[2],
                    'data_inicio': cotacao[3],
                    'data_termino': cotacao[4],
                    'vencimento': cotacao[5],
                    'valor': cotacao[6]
                }
                return render_template('visualizar_cotações.html', cotacao=cotacao_data)
            else:
                return render_template('visualizar_cotações.html', erro="Cotação não encontrada.")

        except sqlite3.Error as e:
            return render_template('visualizar_cotações.html', erro="Erro ao consultar o banco de dados.")

        finally:
            banco.close()   

    return render_template('/visualizar_cotações.html')

#Sucesso
@app.route('/sucesso.html')
def sucesso():
    return render_template('/sucesso.html')
