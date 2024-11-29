//Buscar placas por CPF
document.getElementById('cpf_cadastrar_cotacao').addEventListener('change', function() {
    const cpf = this.value;
    const placaSelect = document.getElementById('placa_cadastrar_cotacao');
    const spanPlaca = document.getElementById('span_placa_cadastrar_cotacao');

    // Limpa as opções anteriores
    placaSelect.innerHTML = '<option value="">Selecione uma placa</option>';
    spanPlaca.textContent = ''; // Limpa qualquer mensagem anterior

    // Se o CPF estiver vazio, não faz a requisição
    if (!cpf) return;

    // Faz a requisição para obter as placas associadas ao CPF selecionado
    fetch(`/buscar_placas?cpf=${cpf}`)
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                spanPlaca.textContent = "Sem veículos vinculados."; // Mostra mensagem no span se não houver placas
            } else {
                // Adiciona cada placa como uma nova opção no select de placas
                data.forEach(placa => {
                    const option = document.createElement('option');
                    option.value = placa;
                    option.textContent = placa;
                    placaSelect.appendChild(option);
                });
            }
        })
        .catch(error => {
            console.error('Erro ao buscar placas:', error);
            spanPlaca.textContent = "Erro ao buscar placas.";
        });
});

//Cadastrar
document.getElementsByName('label_cadastrar_cotacao')[0].onclick = function() {
           
    const cpf = document.getElementsByName('cpf_cadastrar_cotacao')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_cadastrar_cotacao');

    const dtcot = document.getElementsByName('dt_cot_cadastrar_cotacao')[0].value.trim();
    const alertadtcot = document.getElementById('span_dt_cot_cadastrar_cotacao');

    const placa = document.getElementsByName('placa_cadastrar_cotacao')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_cadastrar_cotacao');

    const valor = document.getElementsByName('valor_cadastrar_cotacao')[0].value.trim();
    const alertavalor = document.getElementById('span_valor_cadastrar_cotacao');

    // Limpa mensagens de erro
    alertacpf.textContent = '';
    alertadtcot.textContent = '';
    alertaplaca.textContent = '';
    alertavalor.textContent = '';

    let valido = true; 


    if (cpf === '') {
        alertacpf.textContent = 'Campo vazio!';
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
    } else if (isNaN(parseFloat(valor)) || valor.includes('-')) {
        alertavalor.textContent = 'Apenas números e valores positivos!';
        valido = false;
    }
    // Se todas as validações passarem
    if (valido) {
        document.getElementById('form_cadastrar_cotacao').submit();
    }
};