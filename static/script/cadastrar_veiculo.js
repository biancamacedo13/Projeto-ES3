document.getElementsByName('label_cadastrar_veiculo')[0].onclick = function(){

    const cpf = document.getElementsByName('cpf_cadastrar_veículo')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_cadastrar_veículo');

    const modelo = document.getElementsByName('modelo_cadastrar_veiculo')[0].value.trim();
    const alertamodelo = document.getElementById('span_modelo_cadastrar_veiculo');

    const ano = document.getElementsByName('ano_cadastrar_veiculo')[0].value.trim();
    const alertaano = document.getElementById('span_ano_cadastrar_veiculo');

    const cor = document.getElementsByName('cor_cadastrar_veiculo')[0].value.trim();
    const alertacor = document.getElementById('span_cor_cadastrar_veiculo');

    const placa = document.getElementsByName('placa_cadastrar_veiculo')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_cadastrar_veiculo');

    const chassi = document.getElementsByName('chassi_cadastrar_veiculo')[0].value.trim();
    const alertachassi = document.getElementById('span_chassi_cadastrar_veiculo');

    const cep = document.getElementsByName('cep_pernoite_cadastrar_veiculo')[0].value.trim();
    const alertacep = document.getElementById('span_cep_cadastrar_veiculo');

    alertacpf.textContent ='';
    alertamodelo.textContent = '';
    alertaano.textContent = '';
    alertacor.textContent = '';
    alertaplaca.textContent = '';
    alertachassi.textContent = '';
    alertacep.textContent = '';

    let valido = true;

    if (cpf === '') {
        alertacpf.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{11}$/.test(cpf)) {
        alertacpf.textContent = '11 dígitos!';
        valido = false;
    }

    if (modelo === '') {
        alertamodelo.textContent = 'Campo vazio!';
        valido = false;
    }

    if (ano === '') {
        alertaano.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{4}$/.test(ano)) {
        alertaano.textContent = 'Formato inválido! Deve ser um ano com 4 dígitos.';
        valido = false;
    } else {
        const anoInt = parseInt(ano, 10);
        if (anoInt < 1930 || anoInt > 2100) {
            alertaano.textContent = 'Ano deve estar entre 1900 e 2100!';
            valido = false;
        }
    }

    if (cor === '') {
        alertacor.textContent = 'Campo vazio!';
        valido = false;
    }

    if (placa === '') {
        alertaplaca.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^[A-Za-z]{4}\d{3}$/.test(placa)) {
        alertaplaca.textContent = 'Formato inválido! Deve ser 4 letras seguidas de 3 números.';
        valido = false;
    }

    if (chassi === '') {
        alertachassi.textContent = 'Campo vazio!';
        valido = false;
    }

    if (cep === '') {
        alertacep.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{8}$/.test(cep)) {
        alertacep.textContent = '8 dígitos!';
        valido = false;
    }

    if (valido) {
        document.getElementById('form_cadastrar_veiculo').submit();
    }

}