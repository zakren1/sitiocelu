document.addEventListener('DOMContentLoaded', function () {
    // Obtener el formulario
    const form = document.getElementById('registro-form');

    // Validacion del rut
    const rutInput = document.getElementById('rutusuario');
    rutInput.addEventListener('input', function () {
        if (!/^\d{1,8}-[\dkK]$/.test(rutInput.value)) {
            rutInput.setCustomValidity('El formato del Rut es incorrecto. Ej: 12345678-9');
        } else {
            rutInput.setCustomValidity('');
        }
    });

    // Validacion del nombre
    const nombreInput = document.getElementById('nombre');
    nombreInput.addEventListener('input', function () {
        if (nombreInput.value.length < 2) {
            nombreInput.setCustomValidity('El nombre debe tener al menos 2 caracteres.');
        } else {
            nombreInput.setCustomValidity('');
        }
    });

    // Validacion del apellido
    const apellidoInput = document.getElementById('apellido');
    apellidoInput.addEventListener('input', function () {
        if (apellidoInput.value.length < 2) {
            apellidoInput.setCustomValidity('El nombre de usuario debe tener al menos 2 caracteres.');
        } else {
            apellidoInput.setCustomValidity('');
        }
    });

    // Validacion del usuario
    const usernameInput = document.getElementById('username');
    usernameInput.addEventListener('input', function () {
        if (usernameInput.value.length < 3) {
            usernameInput.setCustomValidity('El nombre de usuario debe tener al menos 3 caracteres.');
        } else {
            usernameInput.setCustomValidity('');
        }
    });

    // Validacion del email
    const emailInput = document.getElementById('email');
    emailInput.addEventListener('input', function () {
        if (emailInput.validity.typeMismatch) {
            emailInput.setCustomValidity('El formato del correo electrónico es incorrecto. Ej: ejemplo@gmail.com');
        } else {
            emailInput.setCustomValidity('');
        }
    });

    // Validacion del password
    const passwordInput = document.getElementById('password');
    passwordInput.addEventListener('input', function () {
        if (passwordInput.value.length < 5) {
            passwordInput.setCustomValidity('La contraseña debe tener al menos 5 caracteres.');
        } else {
            passwordInput.setCustomValidity('');
            // Verificar si la contraseña coincide con la confirmación
            if (confirmPasswordInput.value !== passwordInput.value) {
                confirmPasswordInput.setCustomValidity('Las contraseñas no coinciden.');
            } else {
                confirmPasswordInput.setCustomValidity('');
            }
        }
    });

    // Validacion confimar passord
    const confirmPasswordInput = document.getElementById('confirm-password');
    confirmPasswordInput.addEventListener('input', function () {
        if (confirmPasswordInput.value !== passwordInput.value) {
            confirmPasswordInput.setCustomValidity('Las contraseñas no coinciden.');
        } else {
            confirmPasswordInput.setCustomValidity('');
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
            alert('¡Registro exitoso!');
        }
    }, false);
});