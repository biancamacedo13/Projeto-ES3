document.getElementsByName("label_atualizar_cadastro_seguros")[0].onclick = function validarCadastroSeguro() {
    const cpf = document.getElementsByName("cpf_atualizar_cadastro_seguros")[0].value.trim();
    const alertaCPF = document.getElementById("span_cpf_atualizar_cadastro_seguros");

    const placa = document.getElementsByName("placa_atualizar_cadastro_seguros")[0].value.trim();
    const alertaPlaca = document.getElementById("span_placa_atualizar_cadastro_seguros");

    const seguradora = document.getElementsByName("seguradora_atualizar_cadastro_seguros")[0].value.trim();
    const alertaSeguradora = document.getElementById("span_seguradora_atualizar_cadastro_seguros");

    const dtContratacao = document.getElementsByName("dt_contratacao_atualizar_cadastro_seguros")[0].value.trim();
    const alertaDtContratacao = document.getElementById("span_dt_contratacao_atualizar_cadastro_seguros");

    const dtVencimento = document.getElementsByName("dt_vencimento_atualizar_cadastro_seguros")[0].value.trim();
    const alertaDtVencimento = document.getElementById("span_dt_vencimento_atualizar_cadastro_seguros");

    const apolice = document.getElementsByName("apolice_atualizar_cadastro_seguros")[0].value.trim();
    const alertaApolice = document.getElementById("span_apolice_atualizar_cadastro_seguros");

    const cpfRegex = /^\d{11}$/;
    

    // Limpa alertas anteriores
    alertaCPF.textContent = "";
    alertaPlaca.textContent = "";
    alertaSeguradora.textContent = "";
    alertaDtContratacao.textContent = "";
    alertaDtVencimento.textContent = "";
    alertaApolice.textContent = "";

    let valido = true;

    if (cpf === '') {
        alertaCPF.textContent = "Campo vazio!";
        valido = false;
    } else if (!cpfRegex.test(cpf)) {
        alertaCPF.textContent = "CPF inválido! Use apenas números (11 dígitos).";
        valido = false;
    }

    if (placa === '') {
        alertaPlaca.textContent = "Campo vazio!";
        valido = false;
    }

    if (seguradora === '') {
        alertaSeguradora.textContent = "Campo vazio!";
        valido = false;
    }

    if (dtContratacao === '') {
        alertaDtContratacao.textContent = "Campo vazio!";
        valido = false;
    }

    if (dtVencimento ==='') {
        alertaDtVencimento.textContent = "Campo vazio!";
        valido = false;
    }

    if (apolice === '') {
        alertaApolice.textContent = "Campo vazio!";
        valido = false;
    }

    if (valido) {
        window.alert()
        document.getElementById('form_cadastrar_seguros').submit();
        
    }
};
