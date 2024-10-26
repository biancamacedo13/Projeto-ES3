document.getElementsByName("label_atualizar_cadastro_veiculo")[0].onclick = function validarCadastroVeiculo() {
    const modelo = document.getElementsByName("modelo_atualizar_cadastro_veiculo")[0].value.trim();
    const alertamodelo = document.getElementById("span_modelo_atualizar_cadastro_veiculo");

    const ano = document.getElementsByName("ano_atualizar_cadastro_veiculo")[0].value.trim();
    const alertaano = document.getElementById("span_ano_atualizar_cadastro_veiculo");

    const cor = document.getElementsByName("cor_atualizar_cadastro_veiculo")[0].value.trim();
    const alertacor = document.getElementById("span_cor_atualizar_cadastro_veiculo");

    const placa = document.getElementsByName("placa_atualizar_cadastro_veiculo")[0].value.trim();
    const alertaplaca = document.getElementById("span_placa_atualizar_cadastro_veiculo");

    const chassi = document.getElementsByName("chassi_atualizar_cadastro_veiculo")[0].value.trim();
    const alertachassi = document.getElementById("span_chassi_atualizar_cadastro_veiculo");

    const cepPernoite = document.getElementsByName("cep_pernoite_atualizar_cadastro_veiculo")[0].value.trim();
    const alertacepPernoite = document.getElementById("span_cep_atualizar_cadastro_veiculo");

    const placaRegex = /^[A-Z]{3}\d{4}$/;
    const cepRegex = /^\d{8}$/;

    // Limpa alertas anteriores
    alertamodelo.textContent = "";
    alertaano.textContent = "";
    alertacor.textContent = "";
    alertaplaca.textContent = "";
    alertachassi.textContent = "";
    alertacepPernoite.textContent = "";

    let valido = true;

    if (!modelo) {
        alertamodelo.textContent = "Campo vazio!";
        valido = false;
    }

    if (!ano) {
        alertaano.textContent = "Campo vazio!";
        valido = false;
    }

    if (!cor) {
        alertacor.textContent = "Campo vazio!";
        valido = false;
    }

    if (!placa) {
        alertaplaca.textContent = "Campo vazio!";
        valido = false;
    } else if (!placaRegex.test(placa)) {
        alertaplaca.textContent = "Placa inválida! Formato esperado: ABC1234";
        valido = false;
    }

    if (!chassi) {
        alertachassi.textContent = "Campo vazio!";
        valido = false;
    }

    if (!cepPernoite) {
        alertacepPernoite.textContent = "Campo vazio!";
        valido = false;
    } else if (!cepRegex.test(cepPernoite)) {
        alertacepPernoite.textContent = "8 dígitos.";
        valido = false;
    }

    if (valido) {
        alert("Cadastro de veículo atualizado com sucesso!");
    }
};
