window.onload = function() {
    const banner = document.getElementById("nav-banner");
    banner.style.display = "block";

    // Desaparecer después de 5 segundos (5000 ms)
    setTimeout(function() {
        banner.style.display = "none";
    }, 5000);
};