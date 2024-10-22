document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registration-form');
    const senhaInput = document.getElementById('senha_paciente');
    const requisitosContainer = document.getElementById('senha-requisitos');

    const requisitoMinLength = document.querySelector('.requisito-min-length');
    const requisitoNumber = document.querySelector('.requisito-number');
    const requisitoSpecialChar = document.querySelector('.requisito-special-char');

    // Função para verificar requisitos em tempo real
    function verificarRequisitos() {
        const senha = senhaInput.value;

        // Verifica cada requisito e atualiza a cor
        if (senha.length >= 8) {
            requisitoMinLength.style.color = 'green';
        } else {
            requisitoMinLength.style.color = 'red';
        }

        if (/\d/.test(senha)) {
            requisitoNumber.style.color = 'green';
        } else {
            requisitoNumber.style.color = 'red';
        }

        if (/[!@#$%^&*(),.?":{}|<>]/.test(senha)) {
            requisitoSpecialChar.style.color = 'green';
        } else {
            requisitoSpecialChar.style.color = 'red';
        }
    }

    // Mostra os requisitos apenas após a primeira tentativa de envio
    form.addEventListener('submit', function(event) {
        const senha = senhaInput.value;
        let valid = true;

        if (senha.length < 8) {
            valid = false;
        }

        if (!/\d/.test(senha)) {
            valid = false;
        }

        if (!/[!@#$%^&*(),.?":{}|<>]/.test(senha)) {
            valid = false;
        }

        // Se a senha não for válida, mostre os requisitos e impeça o envio
        if (!valid) {
            requisitosContainer.classList.remove('hidden');
            event.preventDefault();
        }
    });

    // Verifica os requisitos em tempo real enquanto o usuário digita
    senhaInput.addEventListener('input', verificarRequisitos);
});
