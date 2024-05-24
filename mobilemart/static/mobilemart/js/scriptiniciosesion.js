document.addEventListener('DOMContentLoaded', function () {
    // Obtener el formulario
    const form = document.getElementById('login-form');

    // Validacion del email
    const emailInput = document.getElementById('idemail');
    emailInput.addEventListener('input', function () {
        if (emailInput.validity.typeMismatch) {
            emailInput.setCustomValidity('El formato del correo electrónico es incorrecto. Ej: ejemplo@gmail.com');
        } else {
            emailInput.setCustomValidity('');
        }
    });

    // Validacion del password
    const passwordInput = document.getElementById('idpassword');
    passwordInput.addEventListener('input', function () {
        if (passwordInput.value.length < 5) {
            passwordInput.setCustomValidity('La contraseña debe tener al menos 5 caracteres.');
        } else {
            passwordInput.setCustomValidity('');
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
            alert('¡Sesion iniciada con éxito!');
        }
    }, false);
});