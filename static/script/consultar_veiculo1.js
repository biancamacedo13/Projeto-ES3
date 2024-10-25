document.getElementsByName('label_consultar_veiculo')[0].onclick = function validar() {

    // Selecionando os elementos do formulário
    const alertageral = document.getElementById('geral_consultar_veiculo');

    const cpf = document.getElementsByName('cpf_consultar_veiculo')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_consultar_veiculo');

    const placa = document.getElementsByName('placa_consultar_veiculo')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_consultar_veiculo');

    const chassi = document.getElementsByName('chassi_consultar_veiculo')[0].value.trim();
    const alertachassi = document.getElementById('span_chassi_consultar_veiculo');

    // Resetando as mensagens de erro
    alertageral.textContent = '';
    alertacpf.textContent = '';
    alertaplaca.textContent = '';
    alertachassi.textContent = '';

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

    // Validação do Chassi
    if (chassi !== '') {
        algumCampoPreenchido = true;
        if (!/^[A-Z0-9]{17}$/.test(chassi)) {
            alertachassi.textContent = 'O chassi deve ter 17 caracteres alfanuméricos.';
            valido = false;
        }
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