document.addEventListener('DOMContentLoaded', function () {
    // Obtener el formulario
    const form = document.getElementById('form-recuperarcontra');

    // Validacion del email
    const emailInput = document.getElementById('email');
    emailInput.addEventListener('input', function () {
        if (emailInput.validity.typeMismatch) {
            emailInput.setCustomValidity('El formato del correo electrónico es incorrecto. Ej: ejemplo@gmail.com');
        } else {
            emailInput.setCustomValidity('');
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
            alert('¡Por favor revisa tu correo electrónico!');
        }
    }, false);
});