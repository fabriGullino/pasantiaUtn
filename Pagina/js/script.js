//Ejecutar función en el evento click
document.getElementById("btn_open").addEventListener("click", open_close_menu);

//Declaramos variables
var side_menu = document.getElementById("menu_side");
var btn_open = document.getElementById("btn_open");
var body = document.getElementById("body");

//Evento para mostrar y ocultar menú
    function open_close_menu(){
        body.classList.toggle("body_move");
        side_menu.classList.toggle("menu__side_move");
    }

//Si el ancho de la página es menor a 760px, ocultará el menú al recargar la página

if (window.innerWidth < 760){

    body.classList.add("body_move");
    side_menu.classList.add("menu__side_move");
}

//Haciendo el menú responsive(adaptable)

window.addEventListener("resize", function(){

    if (window.innerWidth > 760){

        body.classList.remove("body_move");
        side_menu.classList.remove("menu__side_move");
    }

    if (window.innerWidth < 760){

        body.classList.add("body_move");
        side_menu.classList.add("menu__side_move");
    }

});

// flecha
let listElements = document.querySelectorAll('.list__button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{
        
        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;
        if(menu.clientHeight == "0"){
            height=menu.scrollHeight;
        }

        menu.style.height = `${height}px`;

    })
});




//Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar Buscar
// Aquí implementarías la lógica de búsqueda y actualización de la tabla
document.getElementById('searchButton').addEventListener('click', function() {
    // Lógica de búsqueda y actualización de la tabla
});



//Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar Editar
function loadElement() {
    const ID = document.getElementById('ID').value;
    const Entry = document.getElementById("Entry");
    const Reviewed = document.getElementById("Reviewed");
    const Entry_name = document.getElementById("Entry_name");
    const Protein_names = document.getElementById("Protein_names");
    const Genes_names = document.getElementById("Genes_names");
    const Organism = document.getElementById("Organism");
    const Length = document.getElementById("Length");
    
    // Aquí debes enviar una solicitud al servidor para cargar los datos del elemento con el ID proporcionado.
    // Debes implementar esta parte en tu servidor y manejar la respuesta aquí.
    // Puedes usar AJAX, Fetch API, o cualquier otro método para realizar la solicitud al servidor.

    // Supongamos que el servidor devuelve los datos en formato JSON.
    // Debes llenar los campos del formulario con los datos del elemento.
    const elementData = {
        Entry: "Nombre del Elemento",
        Reviewed: "Descripción del Elemento",
        Entry_name: "Nombre del Elemento",
        Protein_names: "Descripción del Elemento", 
        Genes_names: "Nombre del Elemento",
        Organism: "Descripción del Elemento", 
        Length: "Nombre del Elemento", 
    };

    document.getElementById('Entry').value = elementData.Entry;
    document.getElementById('Reviewed').value = elementData.Reviewed;
    document.getElementById('Entry_name').value = elementData.Entry_name;
    document.getElementById('Protein_names').value = elementData.Protein_names;
    document.getElementById('Genes_names').value = elementData.Genes_names;
    document.getElementById('Organism').value = elementData.Organism;
    document.getElementById('Length').value = elementData.Length;

    // Mostrar el formulario de edición.
    editContainer.style.display = 'block';
    resultDiv.innerHTML = '';
}

document.getElementById('update-form').addEventListener('submit', function (e) {
    e.preventDefault();
    
    // Obtener los datos editados del formulario y enviarlos al servidor para guardar los cambios.
    // Debes implementar esta parte en tu servidor y manejar la respuesta aquí.
    // Puedes usar AJAX, Fetch API, o cualquier otro método para realizar la solicitud al servidor.

    // Mostrar el resultado de la operación en el área de resultados.
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = 'Guardando cambios...'; // Cambia este mensaje según tu lógica de edición.
});



//Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar Agregar 
document.addEventListener("DOMContentLoaded", function () {
    const registroForm = document.getElementById("registroForm");
    const mensaje = document.getElementById("mensaje");

    registroForm.addEventListener("submit", function (e) {
        e.preventDefault();
        
        const Entry = document.getElementById("Entry").value;
        const Reviewed = document.getElementById("Reviewed").value;
        const Entry_name = document.getElementById("Entry_name").value;
        const Protein_names = document.getElementById("Protein_names").value;
        const Genes_names = document.getElementById("Genes_names").value;
        const Organism = document.getElementById("Organism").value;
        const Length = document.getElementById("Length").value;
        

        // Envía los datos al servidor para ser guardados en la base de datos
        fetch("guardar_registro.php", {
            method: "POST",
            body: JSON.stringify({ Entry, Reviewed, Entry_name, Protein_names, Genes_names, Organism, Length}),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                mensaje.innerHTML = "Registro exitoso";
                registroForm.reset();
            } else {
                mensaje.innerHTML = "Error al registrar";
            }
        })
        .catch(error => {
            mensaje.innerHTML = "Error en la solicitud";
            console.error(error);
        });
    });
});



// Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar Eliminar
document.getElementById('delete-form').addEventListener('submit', function (e) {
    e.preventDefault();
    
    const elementId = document.getElementById('element-id').value;
    
    // Envía la solicitud al servidor para eliminar el elemento con el ID proporcionado.
    // Debes implementar esta parte en tu servidor y manejar la respuesta aquí.
    // Puedes usar AJAX, Fetch API, o cualquier otro método para realizar la solicitud al servidor.

    // Muestra el resultado de la operación en el área de resultados.
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `Eliminando elemento con ID ${elementId}...`; // Cambia este mensaje según tu lógica de eliminación.
});
