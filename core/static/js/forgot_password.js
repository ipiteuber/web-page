document.getElementById("ForgotPasswordForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const username = document.getElementById("forgotPassword").value;

    // Valida que no este vacio
    if (username.trim() === "") {
        alert("Please enter your username.");
        return;
    }

    // Simulacion de verificacion
    alert("A recovery code has been sent to your email.");

    // Redirige a pagina de ingreso codigo
    window.location.href = "./code_password.html";
});
