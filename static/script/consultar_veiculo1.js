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
    if (placa === '') {
        valido = false;
    } else if (!/^[A-Za-z]{4}\d{3}$/.test(placa)) {
        alertaplaca.textContent = 'Formato inválido! Deve ser 4 letras seguidas de 3 números.';
        valido = false;
    } else {
        algumCampoPreenchido = true; // Se a placa for válida, consideramos um campo preenchido
    }

    // Validação do Chassi (sem restrições, mas consideramos se foi preenchido)
    if (chassi !== '') {
        algumCampoPreenchido = true;
    }

    // Verificação se pelo menos um campo está preenchido
    if (!algumCampoPreenchido) {
        alertageral.textContent = 'Preencha pelo menos um campo.';
        valido = false;
    }

    // Se tudo estiver válido, submete o formulário
    if (valido) {
        document.getElementById('form_consultar_veiculo').submit();
    }
};
