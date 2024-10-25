document.getElementsByName('label_consultar_cotacao')[0].onclick = function validar() { 

    const alertageral = document.getElementById('geral_consultar_cotacao');

    const cpf = document.getElementsByName('cpf_consultar_cotacao1')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_consultar_cotacao1');

    const seguradora = document.getElementsByName('seguradora_consultar_cotacao1')[0].value.trim();
    const alertaseguradora = document.getElementById('span_seguradora_consultar_cotacao1');

    const placa = document.getElementsByName('placa_consultar_cotacao1')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_consultar_cotacao1');

    const dtcot = document.getElementsByName('dt_sol_consultar_cotacao1')[0].value.trim();
    const alertadtcot = document.getElementById('span_dt_sol_consultar_cotacao1');

    alertageral.textContent = '';
    alertacpf.textContent = '';
    alertaseguradora.textContent = '';
    alertadtcot.textContent = '';
    alertaplaca.textContent = '';

    let algumCampoPreenchido = false;
    let valido = true;

    if (cpf !== '') {
        algumCampoPreenchido = true;
        if (!/^\d{11}$/.test(cpf)) {
            alertacpf.textContent = 'CPF deve ter 11 dígitos!';
            valido = false;
        }
    }

    if (seguradora !== '') {
        algumCampoPreenchido = true;
    }

    if (placa !== '') {
        algumCampoPreenchido = true;
    }

    if (dtcot !== '') {
        algumCampoPreenchido = true;
    }

    if (!algumCampoPreenchido) {
        alertageral.textContent = 'Preencha pelo menos um campo.';
        valido = false;
    }

    if (valido) {
        
        window.alert('Pelo menos um campo válido foi preenchido.');
    }

}