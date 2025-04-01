document.getElementById("signupForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene que se produzca la accion predeterminada de un elemento

    // Se declaran variables
    const fullName = document.getElementById("fullName").value;
    const username = document.getElementById("signupUser").value;
    const email = document.getElementById("signupEmail").value;
    const dob = document.getElementById("dob").value;
    const password = document.getElementById("signupPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Valida que contrasenas sean identicas
    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    // Guarda en localStorage (simula base de datos)
    localStorage.setItem("user", username);
    localStorage.setItem("email", email);
    
    // Redirige a pagina success en caso de que funcione
    window.location.href = "success.html";
});
