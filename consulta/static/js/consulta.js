function generateTimeOptions() {
    const selectElement = document.getElementById('time-selector');
    selectElement.innerHTML = ''; // Clear existing options

    // Define start and end time
    const start = new Date();
    start.setHours(8, 0, 0, 0); // Start at midnight
    const end = new Date();
    end.setHours(20, 0, 0, 0); // End at 23:30

    // Create options in 30-minute intervals
    for (let time = start; time <= end; time.setMinutes(time.getMinutes() + 30)) {
        const hours = time.getHours().toString().padStart(2, '0');
        const minutes = time.getMinutes().toString().padStart(2, '0');
        const option = document.createElement('option');
        option.value = `${hours}:${minutes}`;
        option.textContent = `${hours}:${minutes}`;
        selectElement.appendChild(option);
    }
}

window.onload = generateTimeOptions;

function definirIntervaloData() {
    const hoje = new Date();
    const umAnoDepois = new Date();
    umAnoDepois.setFullYear(hoje.getFullYear() + 1);

    // Define a data mínima (hoje)
    const anoMin = hoje.getFullYear();
    const mesMin = String(hoje.getMonth() + 1).padStart(2, '0');
    const diaMin = String(hoje.getDate()).padStart(2, '0');
    const dataMinima = `${anoMin}-${mesMin}-${diaMin}`;

    // Define a data máxima (um ano a partir de hoje)
    const anoMax = umAnoDepois.getFullYear();
    const mesMax = String(umAnoDepois.getMonth() + 1).padStart(2, '0');
    const diaMax = String(umAnoDepois.getDate()).padStart(2, '0');
    const dataMaxima = `${anoMax}-${mesMax}-${diaMax}`;

    // Atualiza os atributos min e max do input
    document.getElementById('data').setAttribute('min', dataMinima);
    document.getElementById('data').setAttribute('max', dataMaxima);

}

definirIntervaloData();

