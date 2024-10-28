function gerarApolice() {
    var apoliceGerada = Math.floor(10000000 + Math.random() * 90000000); // Gera um número de 8 dígitos
    var apoliceInput = document.getElementsByName('apolice_cadastrar_seguros')[0];
    apoliceInput.value = apoliceGerada; // Define o valor gerado no campo de apólice

    // Exibe a apólice gerada no HTML
    document.getElementById('apolice_exibida').textContent = `Apólice gerada: ${apoliceGerada}`;
}

// Gera a apólice ao carregar a página
window.onload = function() {
    gerarApolice();
}
//CONFERIR PLACA
document.getElementById('cpf_cadastrar_seguros').addEventListener('change', function() {
    const cpfSelecionado = this.value;
    const placaSelect = document.getElementById('placa_cadastrar_seguros');
    const spanPlaca = document.getElementById('span_placa_cadastrar_seguros');
    
    // Limpa as opções de placa e a mensagem do span ao selecionar um novo CPF
    placaSelect.innerHTML = '<option value="">Selecione Placa</option>';
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



//CADASTRAR
document.getElementById('buttom_cadastrar_seguros').onclick = function() {  
    const cpf = document.getElementsByName('cpf_cadastrar_seguros')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_cadastrar_seguros');

    const placa = document.getElementsByName('placa_cadastrar_seguros')[0].value.trim();
    const alertaplaca = document.getElementById('span_placa_cadastrar_seguros');

    const dtcontrata = document.getElementsByName('dt_contratacao_cadastrar_seguros')[0].value.trim();
    const alertadtcontrata = document.getElementById('span_dt_contratacao_cadastrar_seguros');

    const dtvencimento = document.getElementsByName('dt_vencimento_cadastrar_seguros')[0].value.trim();
    const alertavencimento = document.getElementById('span_dt_vencimento_cadastrar_seguros');

    const apolice = document.getElementsByName('apolice_cadastrar_seguros')[0].value.trim();
    const alertaapolice = document.getElementById('span_apolice_cadastrar_seguros');

    // Limpa mensagens de erro anteriores
    alertacpf.textContent = '';
    alertaplaca.textContent = '';
    alertadtcontrata.textContent = '';
    alertavencimento.textContent = '';
    alertaapolice.textContent = '';

    let valido = true;

    // Validações
    if (cpf === '') {
        alertacpf.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{11}$/.test(cpf)) {
        alertacpf.textContent = 'O CPF deve ter 11 dígitos!';
        valido = false;
    }

    if (placa === '') {
        alertaplaca.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^[A-Za-z]{4}\d{3}$/.test(placa)) {
        alertaplaca.textContent = 'Formato inválido! Deve ser 4 letras seguidas de 3 números.';
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
        alertaapolice.textContent = 'Campo vazio!';
        valido = false;
    } else if (isNaN(apolice)) {
        alertaapolice.textContent = 'A apólice deve conter apenas números!';
        valido = false;
    }

    // Se tudo estiver válido, submete o formulário
    if (valido) {
        document.getElementById('form_cadastrar_seguros').submit();
    }
};