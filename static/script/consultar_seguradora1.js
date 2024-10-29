document.getElementsByName('label_consultar_seguradora')[0].onclick = function validar() { 
        const geral = document.getElementById('geral_consultar_seguradora');

        const nome = document.getElementsByName('nome_consultar_seguradora')[0].value.trim();
        const alertanome = document.getElementById('span_nome_consultar_seguradora');

        const cnpj = document.getElementsByName('cnpj_consultar_seguradora')[0].value.trim();
        const alertacnpj = document.getElementById('span_cnpj_consultar_seguradora');

        // Limpar mensagens de erro anteriores
        geral.textContent = '';
        alertanome.textContent = '';
        alertacnpj.textContent = '';

        let algumCampoPreenchido = false;
        let valido = true;

        // Validação para o campo Nome
        if (nome !== '') {
            algumCampoPreenchido = true;
            if (!/^[a-zA-Z\s]+$/.test(nome)) {
                alertanome.textContent = 'Apenas letras!';
                valido = false;
            }
        }

        // Validação para o campo CNPJ
        if (cnpj !== '') {
            algumCampoPreenchido = true;
            if (!/^\d{14}$/.test(cnpj)) {
                alertacnpj.textContent = 'CNPJ deve ter 14 dígitos!';
                valido = false;
            }
        }

        // Verificar se nenhum campo foi preenchido
        if (!algumCampoPreenchido) {
            geral.textContent = 'Preencha pelo menos um campo.';
            valido = false;
        }

        if (valido) {
            // Se pelo menos um campo estiver preenchido e válido, exibe mensagem de sucesso
            document.getElementById('form_consultar_seguradora').submit();
        }
};