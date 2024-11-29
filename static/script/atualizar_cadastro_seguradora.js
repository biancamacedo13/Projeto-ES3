document.getElementById("label_atualizar_cadastro_seguradora").onclick = function validarCadastroSeguradora() {
    const nome = document.getElementsByName("nome_atualizar_cadastro_seguradora")[0].value.trim();
    const alertanome = document.getElementById("span_nome_atualizar_cadastro_seguradora");

    const cnpj = document.getElementsByName("cnpj_atualizar_cadastro_seguradora")[0].value.trim();
    const alertacnpj = document.getElementById("span_cnpj_atualizar_cadastro_seguradora");

    const email = document.getElementsByName("email_atualizar_cadastro_seguradora")[0].value.trim();
    const alertaemail = document.getElementById("span_email_atualizar_cadastro_seguradora");

    const endereco = document.getElementsByName("endereco_atualizar_cadastro_seguradora")[0].value.trim();
    const alertaendereco = document.getElementById("span_endereco_atualizar_cadastro_seguradora");

    const tel = document.getElementsByName("tel_atualizar_cadastro_seguradora")[0].value.trim();
    const alertatel = document.getElementById("span_tel_atualizar_cadastro_seguradora");

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const cnpjRegex = /^\d{14}$/;

    
    alertanome.textContent = "";
    alertacnpj.textContent = "";
    alertaemail.textContent = "";
    alertaendereco.textContent = "";
    alertatel.textContent = "";

    let valido = true;

    if (!nome) {
        alertanome.textContent = "Campo vazio!";
        valido = false;
    }

    if (!cnpj) {
        alertacnpj.textContent = "Campo vazio!";
        valido = false;
    } else if (!cnpjRegex.test(cnpj)) {
        alertacnpj.textContent = "CNPJ deve ter 14 dígitos numéricos.";
        valido = false;
    }

    if (!email) {
        alertaemail.textContent = "Campo vazio!";
        valido = false;
    } else if (!emailRegex.test(email)) {
        alertaemail.textContent = "E-mail inválido.";
        valido = false;
    }

    if (!endereco) {
        alertaendereco.textContent = "Campo vazio!";
        valido = false;
    }

    if (tel === '') {
        alertatel.textContent = 'campo vazio!';
        valido = false;
    } 
    else if (isNaN(tel)) {
        alertatel.textContent = 'apenas números!';
        valido = false;
    }

    if (valido) {
        document.getElementById('form_cadastrar_seguradora').submit();
    }
};
