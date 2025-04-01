document.getElementById("codeForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const code = document.getElementById("codePassword").value;

    // Simulacion de validacion de codigo
    if (code.trim() === "" || code.length < 6) {
        alert("Please enter a valid code.");
        return;
    }

    // Redirige pagina a creacion de contrasena nueva
    window.location.href = "./new_password.html";
});
