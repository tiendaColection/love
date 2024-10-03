function mostrarBotonVolver() {
    // Verifica si la URL actual es diferente de la URL principal
    if (window.location.pathname !== "/") {
      // Si no es la URL principal, muestra el botón
        document.getElementById("botonVolver").style.display = "block";
    } else {
      // Si es la URL principal, oculta el botón
        document.getElementById("botonVolver").style.display = "none";
    }
}

  // Llama a la función al cargar la página
window.onload = mostrarBotonVolver;