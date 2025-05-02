document.getElementById("SignUpForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Se declaran variables obteniendo input de usuario
    const fullname = document.getElementById("fullname").value.trim();
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const datebirth = document.getElementById("datebirth").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirm_password = document.getElementById("confirm_password").value.trim();

    // Validar que no hayan campos vacios
    if (!fullname || !username || !email || !datebirth || !password || !confirm_password) {
        alert("All required fields must be filled!");
        return;
    }

    // Validacion formato de email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    // Validacion de telefono
    if (phone && !/^\d{7,8}$/.test(phone)) {
        alert("Phone number must be 7 or 8 digits long.");
        return;
    }
    // Valida que contrasenas sean identicas
    if (password !== confirm_password) {
        alert("Passwords do not match!");
        return;
    }

    // Valida que contrasena cumpla con condiciones
    // 8 a 12 caracteres
    // Al menos una mayuscula
    // Al menos un numero
    // Al menos un caracter especial
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[<>@$!%*?&])[A-Za-z\d<>@$!%*?&]{8,12}$/;

    if (!passwordRegex.test(password)) {
        alert("Password must be 8-12 characters long, include at least one uppercase letter, one number, and one special character.");
        return;
    }
    
    // Redirige a pagina success
    window.location.href = "./success.html";
});
