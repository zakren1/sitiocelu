document.addEventListener('DOMContentLoaded', function () {
    // Obtener el formulario
    const form = document.getElementById('editarproducto-form');

    // Validacion del precio
    const priceInput = document.getElementById('new-price');
    priceInput.addEventListener('input', function () {
        let price = priceInput.value.trim(); // Eliminar espacios en blanco al principio y al final
        // Verificar si el precio es un número no negativo y no comienza con cero
        if (!/^\d+(\.\d+)?$/.test(price) || parseFloat(price) <= 0 || price.startsWith('0')) {
            priceInput.setCustomValidity('El precio debe ser un valor numérico no negativo y no puede empezar con cero.');
        } else {
            priceInput.setCustomValidity('');
        }
    });

    // Validacion de la imagen
    const imageInput = document.getElementById('product-image');
    imageInput.addEventListener('change', function () {
        const file = imageInput.files[0];
        const validImageTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp', 'image/svg+xml'];

        if (!file || !validImageTypes.includes(file.type)) {
            imageInput.setCustomValidity('Por favor, seleccione un archivo de imagen válido (JPEG, PNG, GIF, BMP, WebP o SVG).');
        } else {
            imageInput.setCustomValidity('');
        }
    });

    // Agregar un listener para el evento 'submit'
    form.addEventListener('submit', function (event) {
        // Verificar si el formulario es válido
        if (!form.checkValidity()) {
            event.preventDefault(); // Evitar que se envíe el formulario si no es válido
            event.stopPropagation(); // Detener la propagación del evento
        } else {
            // Marcar los campos como válidos/inválidos
            form.classList.add('was-validated');

            // Mostrar la alerta
            alert('¡El producto se ha editado con éxito!');
        }
    }, false);
});