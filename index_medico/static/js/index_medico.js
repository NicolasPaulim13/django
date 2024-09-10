// JavaScript para alternar a exibição das respostas nas perguntas frequentes
function toggleResposta(element) {
    const resposta = element.nextElementSibling;
    const icon = element.querySelector('.icon');
    resposta.classList.toggle('active');
    icon.classList.toggle('rotate');
}

// JavaScript para alternar a exibição do menu em dispositivos móveis
const hamburgerMenu = document.querySelector('.hamburger-menu');
const nav = document.querySelector('.nav');

hamburgerMenu.addEventListener('click', () => {
    nav.classList.toggle('active');
});

