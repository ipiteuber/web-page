document.getElementById("passwordForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const password = document.getElementById("signupPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Validacion contrasenas identicas
    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    // Simula guardado de contrasena
    alert("Your password has been successfully changed.");

    // Redirige a pagina para confirmar cambio
    window.location.href = "./success_password.html";
});
