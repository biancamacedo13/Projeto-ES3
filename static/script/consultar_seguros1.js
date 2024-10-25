// Adicionando o evento onclick ao elemento com name="label_consultar_seguros1"
document.getElementsByName('label_consultar_seguros1')[0].onclick = function validar() {

    // Selecionando os elementos do formulário
    const alertageral = document.getElementById('geral_consultar_seguros');

    const cpf = document.getElementsByName('cpf_seguros')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_consultar_seguros');

    const placa = document.getElementsByName('placa_seguros')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_consultar_seguros');

    const dtVencimento = document.getElementsByName('dt_vencimenento_consultar_seguros')[0].value.trim();
    const alertadtVencimento = document.getElementById('span_dt_vencimenento_consultar_seguros');

    // Resetando as mensagens de erro
    alertageral.textContent = '';
    alertacpf.textContent = '';
    alertaplaca.textContent = '';
    alertadtVencimento.textContent = '';

    let algumCampoPreenchido = false;
    let valido = true;

    // Validação do CPF
    if (cpf !== '') {
        algumCampoPreenchido = true;
        if (!/^\d{11}$/.test(cpf)) {
            alertacpf.textContent = 'O CPF deve ter 11 dígitos.';
            valido = false;
        }
    }

    // Validação da Placa
    if (placa !== '') {
        algumCampoPreenchido = true;
        if (!/^[A-Z]{3}\d{4}$/.test(placa)) {
            alertaplaca.textContent = 'Formato de placa inválido! Use o formato ABC1234.';
            valido = false;
        }
    }

    // Validação da Data de Vencimento
    if (dtVencimento !== '') {
        algumCampoPreenchido = true;
    }

    // Verificação se pelo menos um campo está preenchido
    if (!algumCampoPreenchido) {
        alertageral.textContent = 'Preencha pelo menos um campo.';
        valido = false;
    }

    // Mensagem de sucesso se pelo menos um campo estiver válido
    if (valido) {
        window.alert('Pelo menos um campo válido foi preenchido.');
    }
};
