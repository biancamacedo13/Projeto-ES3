function verificarGrupoRadio(grupoNome, alertaId) {
    const radios = document.getElementsByName(grupoNome);
    let selecionado = false;

    for (let i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            selecionado = true;
            break;
        }
    }

    document.getElementById(alertaId).textContent = '';

    return selecionado;
}

document.getElementsByName('label_cadastrar_cliente')[0].onclick = function validar() {        
    
    const nome = document.getElementsByName('nome_cadastrar_cliente')[0].value.trim();
    const alertanome = document.getElementById('span_nome_cadastrar_cliente');

    const cpf = document.getElementsByName('cpf_cadastrar_cliente')[0].value.trim();
    const alertacpf = document.getElementById('span_cpf_cadastrar_cliente');

    const email = document.getElementsByName('email_cadastrar_cliente')[0].value.trim();
    const alertaemail = document.getElementById('span_email_cadastrar_cliente');

    const dtnasc = document.getElementsByName('dt_nasc_cadastrar_cliente')[0].value.trim();
    const alertadtnasc = document.getElementById('span_dt_nasc_cadastrar_cliente');

    const endereco = document.getElementsByName('endereco_cadastrar_cliente')[0].value.trim();
    const alertaenderco = document.getElementById('span_endereco_cadastrar_cliente');

    const tel = document.getElementsByName('tel_cadastrar_cliente')[0].value.trim();
    const alertatel = document.getElementById('span_tel_cadastrar_cliente');

    const prof = document.getElementsByName('prof_cadastrar_cliente')[0].value.trim();
    const alertaprof = document.getElementById('span_prof_cadastrar_cliente');

    const sal = document.getElementsByName('sal_cadastrar_cliente')[0].value.trim();
    const alertasal = document.getElementById('span_sal_cadastrar_cliente');

    

    const principal = verificarGrupoRadio('condutor_principal_cadastrar_cliente', 'span_condutor_principal_cadastrar_cliente_cadastrar_cliente');
    const alertaprincipal = document.getElementById('span_condutor_principal_cadastrar_cliente_cadastrar_cliente');

    const proprietario = verificarGrupoRadio('proprietario_cadastrar_cliente', 'span_proprietario_cadastrar_cliente');
    const alertaproprietario = document.getElementById('span_proprietario_cadastrar_cliente');

    const civil = verificarGrupoRadio('seletor_cadastrar_cliente', 'span_seletor_cadastrar_cliente');
    const alertacivil = document.getElementById('span_seletor_cadastrar_cliente');
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    
    alertanome.textContent = '';
    alertacpf.textContent = '';
    alertaemail.textContent = '';
    alertadtnasc.textContent = '';
    alertaenderco.textContent = '';
    alertatel.textContent = '';
    alertaprof.textContent = '';
    alertasal.textContent = '';

    let valido = true; 

    /*Validações*/
    if (nome === '') {
        alertanome.textContent = 'campo vazio!';
        valido = false;
    } 
    
    else if (!/^[a-zA-Z\s]+$/.test(nome)) {
        alertanome.textContent = 'apenas letras!';
        valido = false;
    }

    
    if (cpf === '') {
        alertacpf.textContent = 'campo vazio!';
        valido = false;
    } 
    
    else if (isNaN(cpf)) {
        alertacpf.textContent = 'apenas números!';
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

    if (dtnasc === ''){
        alertadtnasc.textContent = 'campo vazio!';
        valido = false;
    }

    if(endereco === ''){
        alertaenderco.textContent = 'campo vazio!';
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

    if(prof === ''){
        alertaprof.textContent = 'campo vazio!';
        valido = false;
    }

    if (sal === '') {
        alertasal.textContent = 'campo vazio!';
        valido = false;
    } 
    
    else if (isNaN(sal)) {
        alertasal.textContent = 'apenas números!';
        valido = false;
    }

    if (!principal) {
        alertaprincipal.textContent = 'selecione!';
        valido = false;
    }

    if (!proprietario) {
        alertaproprietario.textContent = 'selecione!';
        valido = false;
    }

    if (!civil) {
        alertacivil.textContent = 'selecione!';
        valido = false;
    }


    
    if (valido) {
        window.alert('Enviado');
    }
};