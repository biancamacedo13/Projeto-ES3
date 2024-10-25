document.getElementsByName('label_consultar_cliente1')[0].onclick = function validar() {

    const geral = document.getElementById('geral_consultar_cliente1');

    const nome = document.getElementsByName('nome_consultar_cliente1')[0].value.trim();
    const alertanome = document.getElementById('span_nome_consultar_cliente1');

    const cpf = document.getElementsByName('cpf_consultar_cliente1')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_consultar_cliente1');

    const email = document.getElementsByName('email_consultar_cliente1')[0].value.trim();
    const alertaemail = document.getElementById('span_email_consultar_cliente1');

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

     geral.textContent = '';
    alertanome.textContent = '';
    alertacpf.textContent = '';
    alertaemail.textContent = '';

    let algumCampoPreenchido = false;
    let valido = true;

    
    if (nome !== '') {
        algumCampoPreenchido = true;
        if (!/^[a-zA-Z\s]+$/.test(nome)) {
            alertanome.textContent = 'Apenas letras!';
            valido = false;
        }
    }

    
    if (cpf !== '') {
        algumCampoPreenchido = true;
        if (!/^\d{11}$/.test(cpf)) {
            alertacpf.textContent = 'CPF deve ter 11 dígitos!';
            valido = false;
        }
    }

    
    if (email !== '') {
        algumCampoPreenchido = true;
        if (!emailRegex.test(email)) {
            alertaemail.textContent = 'Formato inválido: xxx@xmail.com';
            valido = false;
        }
    }

    
    if (!algumCampoPreenchido) {
        geral.textContent = 'Preencha pelo menos um campo.';
        valido = false;
    }

    if (valido) {
        
        window.alert('Pelo menos um campo válido foi preenchido.');
    }
}