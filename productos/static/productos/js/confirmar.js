function mostrarVistaPrevia(entrada) {
    const vistaPrevia = document.getElementById('vista-previa');
    if (entrada.files && entrada.files[0]) {
        const lector = new FileReader();
        lector.onload = function (evento) {
            vistaPrevia.src = evento.target.result;
            vistaPrevia.style.display = 'block';
        };
        lector.readAsDataURL(entrada.files[0]);
    }
}