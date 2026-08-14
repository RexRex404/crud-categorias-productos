function confirmarEliminacion(evento, nombre) {
    const seguro = confirm('¿Seguro que deseas eliminar la categoría "' + nombre + '"?');
    if (!seguro) {
        evento.preventDefault();
    }
}