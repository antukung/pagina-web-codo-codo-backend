// File: script.js

// Function to add a new libro
function agregarLibro() {
    // Get form data
    const nombre = document.getElementById('nombre').value;
    const linkDescarga = document.getElementById('link_descarga').value;
    const grupo = document.getElementById('grupo').value;
    const imagen = document.getElementById('imagen').files[0];

    // Create FormData object to send data as a multipart/form-data
    const formData = new FormData();
    formData.append('nombre', nombre);
    formData.append('link_descarga', linkDescarga);
    formData.append('grupo', grupo);
    formData.append('imagen', imagen);

    // Send a POST request to Flask endpoint
    fetch('http://localhost:5000/productos', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Libro added:', data);
        // Optionally, update the UI or perform other actions
    })
    .catch(error => console.error('Error adding libro:', error));
}

// Function to edit an existing libro
function editarLibro() {
    // Retrieve form data
    const id = document.getElementById('id').value;
    const nombre = document.getElementById('nombre_2').value;
    const linkDescarga = document.getElementById('link_descarga_2').value;
    const grupo = document.getElementById('grupo_2').value;
    const imagen = document.getElementById('imagen_2').files[0];

    // Create FormData object to send data as a multipart/form-data
    const formData = new FormData();
    formData.append('id', id); // Include the ID for editing
    formData.append('nombre', nombre);
    formData.append('link_descarga', linkDescarga);
    formData.append('grupo', grupo);
    formData.append('imagen', imagen);

    // Send a PUT request to Flask endpoint for editing
    fetch(`http://localhost:5000/productos/${id}`, {
        method: 'PUT',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Libro edited:', data);
        // Optionally, update the UI or perform other actions
    })
    .catch(error => console.error('Error editing libro:', error));
}

// Function to delete an existing libro
function eliminarLibro() {
    // Retrieve form data
    const id = document.getElementById('id_2').value;

    // Create FormData object to send data as a multipart/form-data
    const formData = new FormData();
    formData.append('id', id);

    // Send a DELETE request to Flask endpoint for deletion
    fetch(`http://localhost:5000/productos/${id}`, {
        method: 'DELETE',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Libro deleted:', data);
        // Optionally, update the UI or perform other actions
    })
    .catch(error => console.error('Error deleting libro:', error));
}

