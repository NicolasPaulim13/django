document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('cpf').addEventListener('input', function (e) {
        this.value = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (this.value.length > 11) {
            this.value = this.value.slice(0, 11); // Limita a entrada a 11 dígitos
        }
    });
});
