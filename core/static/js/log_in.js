document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const username = document.getElementById("loginUser").value;
    const password = document.getElementById("loginPassword").value;

    // Autenticacion con roles (usuario normal y vendedor)
    if (username === "user123" && password === "password123") {
        localStorage.setItem("user", username);
        localStorage.setItem("role", "user"); // Asigna el rol de usuario
        window.location.href = "welcome_log.html"; // Redirige a pagina de usuario
    } else if (username === "vendedor" && password === "passwordVendedor") {
        localStorage.setItem("user", username);
        localStorage.setItem("role", "vendedor"); // Asigna el rol de vendedor
        window.location.href = "welcome_role.html"; // Redirige a pagina de vendedor
    } else { // Mensaje en caso de error
        alert("Invalid username or password. Please try again.");
    }
});