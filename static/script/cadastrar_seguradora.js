document.getElementsByName('label_cadastrar_seguradora')[0].onclick = function() {

    const nome = document.getElementsByName('nome_cadastrar_seguradora')[0].value.trim();
    const alertanome = document.getElementById('span_nome_cadastrar_seguradora');
           
    const cnpj = document.getElementsByName('cnpj_cadastrar_seguradora')[0].value.trim();
    const alertacnpj = document.getElementById('span_cnpj_cadastrar_seguradora');

    const email = document.getElementsByName('email_cadastrar_seguradora')[0].value.trim();
    const alertaemail = document.getElementById('span_email_cadastrar_seguradora');

    const endereco = document.getElementsByName('endereco_cadastrar_seguradora')[0].value.trim();
    const alertaenderco = document.getElementById('span_endereco_cadastrar_seguradora');

    const tel = document.getElementsByName('tel_cadastrar_seguradora')[0].value.trim();
    const alertatel = document.getElementById('span_tel_cadastrar_seguradora');

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Limpa mensagens de erro
    alertacnpj.textContent = '';
    alertanome.textContent = '';
    alertaemail.textContent = '';
    alertaenderco.textContent = '';
    alertatel.textContent = '';

    let valido = true; 

    //Validações
    if (nome === '') {
        alertanome.textContent = 'campo vazio!';
        valido = false;
    } 
    else if (!/^[a-zA-Z\s]+$/.test(nome)) {
        alertanome.textContent = 'apenas letras!';
        valido = false;
    }

    if (cnpj === '') {
        alertacnpj.textContent = 'Campo vazio!';
        valido = false;
    } else if (!/^\d{14}$/.test(cnpj)) {
        alertacnpj.textContent = 'O CNPJ deve conter exatamente 14 dígitos!';
        valido = false;
    }

    if (email === '') {
        alertaemail.textContent = 'campo vazio!';
        valido = false;
    } 
    else if (!emailRegex.test(email)) {
        alertaemail.textContent = 'xxx@xmail.com';
        valido = false;
    }
    
    if (endereco === '') {
        alertaenderco.textContent = 'Campo vazio!';
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