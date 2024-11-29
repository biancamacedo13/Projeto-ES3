// Espera o DOM carregar completamente
document.addEventListener("DOMContentLoaded", function() {
    // Adicionando o evento onclick ao elemento com name="label_consultar_seguros1"
    document.getElementsByName('label_consultar_seguros1')[0].onclick = function validar() {

        // Selecionando os elementos do formulário
        const alertageral = document.getElementById('geral_consultar_seguros');
        const alertacpf = document.getElementById('span_cpf_consultar_seguros'); // Adicionei esta linha
        const alertaplaca = document.getElementById('span_placa_consultar_seguros');
        const alertadtVencimento = document.getElementById('span_dt_vencimenento_consultar_seguros');

        const cpf = document.getElementsByName('cpf_seguros')[0].value.trim();
        const seguradora = document.getElementsByName('seguradora_seguros')[0].value.trim();
        const placa = document.getElementsByName('placa_seguros')[0].value.trim();
        const dtVencimento = document.getElementsByName('dt_vencimenento_consultar_seguros')[0].value.trim();

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
            // Adicione sua lógica de validação de CPF aqui, se necessário
        }

        // Validação da Placa
        if (placa !== '') {
            algumCampoPreenchido = true;
            if (!/^[A-Z]{4}\d{3}$/.test(placa)) {
                alertaplaca.textContent = 'Formato de placa inválido! Use o formato ABC1234.';
                valido = false;
            }
        }
        
        // Validação da Seguradora
        if (seguradora !== '') {
            algumCampoPreenchido = true;
        }

        // Validação da Data de Vencimento
        if (dtVencimento !== '') {
            algumCampoPreenchido = true;
            // Adicione sua lógica de validação da data aqui, se necessário
        }

        // Verificação se pelo menos um campo está preenchido
        if (!algumCampoPreenchido) {
            alertageral.textContent = 'Preencha 1 campo!';
            valido = false;
        }

        // Mensagem de sucesso se pelo menos um campo estiver válido
        if (valido) {
            document.getElementById('form_consultar_seguros').submit();
        }
    };
});
