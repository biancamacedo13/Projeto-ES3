document.getElementsByName('label_cadastrar_seguros')[0].onclick = function validar() {

    const cpf = document.getElementsByName('cpf_cadastrar_seguros')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_cadastrar_seguros');

    const placa = document.getElementsByName('placa_cadastrar_seguros')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_cadastrar_seguros');

    const seguradora = document.getElementsByName('seguradora_cadastrar_seguros')[0].value.trim();
    const alertaseguradora = document.getElementById('span_seguradora_cadastrar_seguros');

    const dtcontrata = document.getElementsByName('dt_contratacao_cadastrar_seguros')[0].value.trim();
    const alertadtcontrata = document.getElementById('span_dt_contratacao_cadastrar_seguros');

    const dtvencimento = document.getElementsByName('dt_vencimento_cadastrar_seguros')[0].value.trim();
    const alertavencimento = document.getElementById('span_dt_vencimento_cadastrar_seguros');

    const apolice = document.getElementsByName('apolice_cadastrar_seguros')[0].value.trim();
    const alertaapolice = document.getElementById('span_apolice_cadastrar_seguros');

    alertacpf.textContent = '';
    alertaplaca.textContent = '';
    alertaseguradora.textContent = '';
    alertadtcontrata.textContent = '';
    alertavencimento.textContent = '';
    alertaapolice.textContent = '';

    //Validações
    if (cpf === '') {
        alertacpf.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{11}$/.test(cpf)) {
        alertacpf.textContent = '11 dígitos!';
        valido = false;
    }

    if (placa === '') {
        alertaplaca.textContent = 'Campo vazio!';
        valido = false;
    }

    if (seguradora === '') {
        alertaseguradora.textContent = 'Campo vazio!';
        valido = false;
    }

    if (dtcontrata === '') {
        alertadtcontrata.textContent = 'Campo vazio!';
        valido = false;
    }

    if (dtvencimento === '') {
        alertavencimento.textContent = 'Campo vazio!';
        valido = false;
    }

    if (apolice === '') {
        alertaapolice.textContent = 'campo vazio!';
        valido = false;
    } 
    else if (isNaN(apolice)) {
        alertaapolice.textContent = 'apenas números!';
        valido = false;
    }
}