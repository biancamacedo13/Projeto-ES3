document.getElementsByName('label_cadastrar_cotacao')[0].onclick = function() {
           
    const cpf = document.getElementsByName('cpf_cadastrar_cotacao')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_cadastrar_cotacao');

    const seguradora = document.getElementsByName('seguradora_cadastrar_cotacao')[0].value.trim();
    const alertaseguradora = document.getElementById('span_seguradora_cadastrar_cotacao');

    const dtcot = document.getElementsByName('dt_cot_cadastrar_cotacao')[0].value.trim();
    const alertadtcot = document.getElementById('span_dt_cot_cadastrar_cotacao');

    const placa = document.getElementsByName('placa_cadastrar_cotacao')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_cadastrar_cotacao');

    const valor = document.getElementsByName('valor_cadastrar_cotacao')[0].value.trim();
    const alertavalor = document.getElementById('span_valor_cadastrar_cotacao');

    // Limpa mensagens de erro
    alertacpf.textContent = '';
    alertaseguradora.textContent = '';
    alertadtcot.textContent = '';
    alertaplaca.textContent = '';
    alertavalor.textContent = '';

    let valido = true; 


    if (cpf === '') {
        alertacpf.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{11}$/.test(cpf)) {
        alertacpf.textContent = '11 dígitos!';
        valido = false;
    }


  if (seguradora === '') {
        alertaseguradora.textContent = 'Campo vazio!';
        valido = false;
    }


    if (placa === '') {
        alertaplaca.textContent = 'Campo vazio!';
        valido = false;
    }


    if (dtcot === '') {
        alertadtcot.textContent = 'Campo vazio!';
        valido = false;
    }


    if (valor === '') {
        alertavalor.textContent = 'Campo vazio!';
        valido = false;
    } else if (isNaN(parseFloat(valor))) {
        alertavalor.textContent = 'Apenas números!';
        valido = false;
    }

    // Se todas as validações passarem
    if (valido) {
        document.getElementById('form_cadastrar_cotacao').submit();
    }
};