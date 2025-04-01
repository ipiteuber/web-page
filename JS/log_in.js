document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const username = document.getElementById("loginUser").value;
    const password = document.getElementById("loginPassword").value;

    // Autenticacion
    if (username === "user123" && password === "password123") {
        localStorage.setItem("user", username); // Guarda sesion en localStorage
        window.location.href = "success.html"; // Redirige a la pagina success
    } else { // Mensaje en caso de error
        alert("Invalid username or password. Please try again."); 
    }
});
