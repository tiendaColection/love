const carrito = document.getElementById('carrito');
const elemento1 = document.getElementById('lista-1');
const lista = document.querySelector('#listaCarrito tbody');
const vaciarCarrito = document.getElementById('vaciar-carrito');

cargarEventListeners();

function cargarEventListeners(){
    elemento1.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);

    vaciarCarrito.addEventListener('click', vaciarCarrito);
}

function comprarElemento(e){
    e.preventDeafault();
    if(e.target.ClassList.constainss('agregar-carrito')){
        const elemento = e.target.parentElement.parentElement;
        leerDatosElemento(elemento);
    }
}
function leerDatosElemento(elemento){
    const infoElememto = {
        imagen: elemento.querySelector('img').src,
        titulo: elemento.querySelector('h3').textContent,
        precio: elemento.querySelector('.precio').textContent,
        id:elemento.querySelector('a').getAttribute('data-id')
    }
    insertarCarrito(infoElememto);
}
function insertarCarrito(elemento){
    const row= document.createElement('tr');
    row.innerHTML=`
        <td>
            <img src="${elemento.imagen}" whidth=100 height=150px>
        </td>
        <td>
            ${elemento.titulo}
        </td>
        <td>
            ${elemento.precio}
        </td>
        <td>
            <a herf="#" class="borrar" data-id="${elemento.id}"></a>
        </td>
    `;
    lista.appendChild(row);
}
function eliminarElemento(e){
    e.preventDeafault();
    let elemento,
        elemtoId;

    if (e.target.ClassList.contains('borrar')){
        e.target.parentElement.parentElement.remove();
        elemento = e.target.parentElement.parentElement;
        elemtoId = elemento.querySelector('a'.getAttribute('data-id'));
    }
}
function vaciarCarrito(){
    while(lista.firstChild){
        lista.removeChild(lista.firstChild);
    }
    return false;
}