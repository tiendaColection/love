window.onload = function() {
    const banner = document.getElementById("nav-banner");
    banner.style.display = "block";

    // Desaparecer al hacer clic
    banner.onclick = function() {
        banner.style.display = "none";
    };
};