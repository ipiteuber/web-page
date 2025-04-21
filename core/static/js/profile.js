document.addEventListener("DOMContentLoaded", function () {
    // Obtener datos de las variables desde localStorage
    const fullname = localStorage.getItem("fullname") || "";
    const username = localStorage.getItem("username") || "";
    const email = localStorage.getItem("email") || "";
    const datebirth = localStorage.getItem("datebirth") || "";
    const phone = localStorage.getItem("phone") || "";

    // Rellena campos del formulario con los datos guardados
    document.getElementById("fullname").value = fullname;
    document.getElementById("username").value = username;
    document.getElementById("email").value = email;
    document.getElementById("datebirth").value = datebirth;
    document.getElementById("phone").value = phone;
});

// Manejar la actualizacion del perfil
document.getElementById("SignupForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Obtener los valores de los inputs
    const fullname = document.getElementById("fullname").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const datebirth = document.getElementById("datebirth").value;
    const phone = document.getElementById("phone").value;

    // Guardar en localStorage (simulacion de base de datos)
    localStorage.setItem("fullname", fullname);
    localStorage.setItem("username", username);
    localStorage.setItem("email", email);
    localStorage.setItem("datebirth", datebirth);
    localStorage.setItem("phone", phone);

    // Mensaje de exito
    alert("Profile updated successfully!");

    // Recarga pagina
    window.location.href = "./profile.html";
});
