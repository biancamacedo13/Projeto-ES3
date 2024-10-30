//BUSCAR PLACA
document.getElementById('cpf_consultar_cotacao1').addEventListener('change', function() {
    const cpfSelecionado = this.value;
    const placaSelect = document.getElementById('placa_consultar_cotacao1');
    const spanPlaca = document.getElementById('span_placa_consultar_cotacao1');
    
    // Limpa as opções de placa e a mensagem do span ao selecionar um novo CPF
    placaSelect.innerHTML = '<option value="">Selecione uma placa</option>';
    spanPlaca.textContent = "";  // Limpar mensagem anterior

    if (!cpfSelecionado) return;  // Se nenhum CPF foi selecionado, encerra a execução

    // Fazer a requisição para buscar as placas associadas ao CPF selecionado
    fetch(`/buscar_placas?cpf=${cpfSelecionado}`)
        .then(response => response.json())
        .then(placas => {
            if (placas.length === 0) {
                // Adiciona a mensagem "Sem veículos vinculados" no span se não houver placas
                spanPlaca.textContent = "Sem veículos vinculados";
            } else {
                // Adiciona cada placa como uma nova opção no select e limpa o span
                spanPlaca.textContent = "";  // Limpa mensagem do span se houver placas
                placas.forEach(placa => {
                    const option = document.createElement('option');
                    option.value = placa;
                    option.textContent = placa;
                    placaSelect.appendChild(option);
                });
            }
        })
        .catch(error => {
            console.error('Erro ao buscar placas:', error);
            spanPlaca.textContent = "Erro ao buscar veículos.";  // Mensagem de erro caso haja falha na requisição
        });
});


document.getElementsByName('label_consultar_cotacao')[0].onclick = function() {

    const alertageral = document.getElementById('geral_consultar_cotacao');
    const cpf = document.getElementsByName('cpf_consultar_cotacao1')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_consultar_cotacao1');

    const seguradora = document.getElementsByName('seguradora_cadastrar_cotacao')[0].value.trim();
    const alertaseguradora = document.getElementById('span_seguradora_consultar_cotacao1');

    const placa = document.getElementsByName('placa_consultar_cotacao1')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_consultar_cotacao1');

    const dtcot = document.getElementsByName('dt_sol_consultar_cotacao1')[0].value.trim();
    const alertadtcot = document.getElementById('span_dt_sol_consultar_cotacao1');

    // Limpar mensagens de alerta
    alertageral.textContent = '';
    alertacpf.textContent = '';
    alertaseguradora.textContent = '';
    alertadtcot.textContent = '';
    alertaplaca.textContent = '';

    let algumCampoPreenchido = false;

    // Verificar se pelo menos um campo está preenchido
    if (cpf !== '' && cpf !== 'Selecione um CPF') {
        algumCampoPreenchido = true;
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

    // Se nenhum campo foi preenchido, mostrar mensagem de erro
    if (!algumCampoPreenchido) {
        alertageral.textContent = 'Preencha 1 campo!';
        return; // Interrompe a execução se nenhum campo foi preenchido
    }

    // Validar formato da placa
    if (placa !== '' && !/^[A-Z]{3}\d{4}$/.test(placa)) {
        alertaplaca.textContent = 'Formato de placa inválido! Use o formato ABC1234.';
        return; // Interrompe a execução se a placa estiver no formato incorreto
    }

    // Se pelo menos um campo estiver preenchido e a placa for válida (se fornecida), continuar com a ação
    document.getElementById('form_consultar_cotacao1').submit();
};
