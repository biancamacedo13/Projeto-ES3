document.getElementsByName("label_atualizar_cadastro_cliente")[0].onclick = function validarCadastro() {
    
    const geral = document.getElementById("geral_consultar_veiculo");
    
    const nome = document.getElementsByName("nome_atualizar_cadastro_cliente")[0].value.trim();
    const alertanome = document.getElementById("span_nome_atualizar_cadastro_cliente");

    const cpf = document.getElementsByName("cpf_atualizar_cadastro_cliente")[0].value.trim();
    const alertacpf = document.getElementById("span_cpf_atualizar_cadastro_cliente");

    const email = document.getElementsByName("email_atualizar_cadastro_cliente")[0].value.trim();
    const alertaemail = document.getElementById("span_email_atualizar_cadastro_cliente");

    const dtnasc = document.getElementsByName("dt_nasc_atualizar_cadastro_cliente")[0].value;
    const alertadtnasc = document.getElementById("span_dt_nasc_atualizar_cadastro_cliente");

    const endereco = document.getElementsByName("endereco_atualizar_cadastro_cliente")[0].value.trim();
    const alertaendereco = document.getElementById("span_atualizar_cadastro_cliente");

    const tel = document.getElementsByName("tel_atualizar_cadastro_cliente")[0].value.trim();
    const alertatel = document.getElementById("span_tel_atualizar_cadastro_cliente");

    const prof = document.getElementsByName("prof_atualizar_cadastro_cliente")[0].value.trim();
    const alertaprof = document.getElementById("span_prof_atualizar_cadastro_cliente");

    const sal = document.getElementsByName("sal_atualizar_cadastro_cliente")[0].value.trim();
    const alertasal = document.getElementById("span_sal_atualizar_cadastro_cliente");

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const cpfRegex = /^\d{11}$/;
    const telRegex = /^\d{10,11}$/;

    // Limpa alertas anteriores
    alertanome.textContent = "";
    alertacpf.textContent = "";
    alertaemail.textContent = "";
    alertadtnasc.textContent = "";
    alertaendereco.textContent = "";
    alertatel.textContent = "";
    alertaprof.textContent = "";
    alertasal.textContent = "";

    let valido = true;

    if (!nome) {
        alertanome.textContent = "Campo vazio!";
        valido = false;
    }

    if (!cpf) {
        alertacpf.textContent = "Campo vazio!";
        valido = false;
    } else if (!cpfRegex.test(cpf)) {
        alertacpf.textContent = "CPF deve ter 11 dígitos numéricos.";
        valido = false;
    }

    if (!email) {
        alertaemail.textContent = "Campo vazio!";
        valido = false;
    } else if (!emailRegex.test(email)) {
        alertaemail.textContent = "E-mail inválido.";
        valido = false;
    }

    if (!dtnasc) {
        alertadtnasc.textContent = "Campo vazio!";
        valido = false;
    }

    if (!endereco) {
        alertaendereco.textContent = "Campo vazio!";
        valido = false;
    }

    if (!tel) {
        alertatel.textContent = "Campo vazio!";
        valido = false;
    } else if (!telRegex.test(tel)) {
        alertatel.textContent = "Telefone deve ter entre 10 e 11 dígitos.";
        valido = false;
    }

    if (!prof) {
        alertaprof.textContent = "Campo vazio!";
        valido = false;
    }

    if (!sal) {
        alertasal.textContent = "Campo vazio!";
        valido = false;
    }

    
    if (valido) {
        geral.textContent = "Cadastro atualizado com sucesso!";
    } else {
        geral.textContent = "Por favor, corrija os erros antes de enviar.";
    }
};
