document.getElementById("LoginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Autenticacion con roles (usuario normal y vendedor)
    if (username === "user123" && password === "password123") {
        window.location.href = "welcome_log.html"; // Redirige a pagina de usuario
    } else if (username === "vendedor" && password === "passwordVendedor") {
        window.location.href = "welcome_role.html"; // Redirige a pagina de vendedor
    } else { // Mensaje en caso de error
        alert("Invalid username or password. Please try again.");
    }
});