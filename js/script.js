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
    // Similar to agregarLibro, send a PUT request to update an existing libro
    // You can retrieve form data and send it to the Flask endpoint
}

// Function to delete an existing libro
function eliminarLibro() {
    // Similar to agregarLibro, send a DELETE request to remove an existing libro
    // You can retrieve form data and send it to the Flask endpoint
}

// Function to fetch and display all libros
function mostrarLibros() {
    // Send a GET request to fetch all libros from the Flask endpoint
    fetch('http://localhost:5000/productos')
    .then(response => response.json())
    .then(data => {
        console.log('Libros:', data);
        // Optionally, update the UI to display the libros
    })
    .catch(error => console.error('Error fetching libros:', error));
}
