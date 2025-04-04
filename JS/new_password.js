document.getElementById("passwordForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const password = document.getElementById("signupPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Valida que contrasenas sean identicas
    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    // Valida que contrasena cumpla con condiciones
    // 8 a 12 caracteres
    // Al menos una mayuscula
    // Al menos un numero
    // Al menos un caracter especial
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$/;

    if (!passwordRegex.test(password)) {
        alert("Password must be 8-12 characters long, include at least one uppercase letter, one number, and one special character.");
        return;
    }

    // Simula guardado de contrasena
    alert("Your password has been successfully changed.");

    // Redirige a pagina para confirmar cambio
    window.location.href = "./success_password.html";
});
