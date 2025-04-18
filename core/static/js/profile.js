document.addEventListener("DOMContentLoaded", function () {
    // Obtener datos de las variables desde localStorage
    const fullName = localStorage.getItem("fullName") || "";
    const username = localStorage.getItem("username") || "";
    const email = localStorage.getItem("email") || "";
    const dob = localStorage.getItem("dob") || "";
    const phone = localStorage.getItem("phone") || "";

    // Rellena campos del formulario con los datos guardados
    document.getElementById("fullName").value = fullName;
    document.getElementById("signupUser").value = username;
    document.getElementById("signupEmail").value = email;
    document.getElementById("dob").value = dob;
    document.getElementById("phone").value = phone;
});

// Manejar la actualizacion del perfil
document.getElementById("signupForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Obtener los valores de los inputs
    const fullName = document.getElementById("fullName").value;
    const username = document.getElementById("signupUser").value;
    const email = document.getElementById("signupEmail").value;
    const dob = document.getElementById("dob").value;
    const phone = document.getElementById("phone").value;

    // Guardar en localStorage (simulacion de base de datos)
    localStorage.setItem("fullName", fullName);
    localStorage.setItem("username", username);
    localStorage.setItem("email", email);
    localStorage.setItem("dob", dob);
    localStorage.setItem("phone", phone);

    // Mensaje de exito
    alert("Profile updated successfully!");

    // Recarga pagina
    window.location.href = "./profile.html";
});
