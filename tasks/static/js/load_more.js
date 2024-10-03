document.getElementById('load-more').addEventListener('click', function() {
    const button = this;
    const offset = parseInt(button.getAttribute('data-offset'));

    fetch(`/load-more/?offset=${offset}`)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('lista-1');
            data.figurines.forEach(figurine => {
                if (figurine.imagen_url) { // Solo añade si hay imagen
                    const div = document.createElement('div');
                    div.classList.add('box');
                    div.innerHTML = `
                        <a href="/figurine/${figurine.pk}/">
                            <img src="${figurine.imagen_url}" class="fixed-size-img">
                            <h5>${figurine.name}</h5>
                            <p class="precio">$${figurine.price}</p>
                            <a href="https://wa.me/59173917621?text=Hola,%20me%20interesa%20esta%20figurita:%0A%0ANombre:%20${figurine.name}%0APrecio:%20${figurine.price}" class="btn-2">
                                <img src="${staticUrl}img/whatsapp.png" width="22" height="22" alt=""> Me interesa
                            </a>
                            <a href="#" class="agregar-carrito btn-3" data-id="${figurine.pk}">
                                <img src="${staticUrl}img/car.svg" alt=""> Agregar
                            </a>
                        </a>
                    `;
                    container.appendChild(div);
                }
            });
            button.setAttribute('data-offset', offset + 12);
        });
});