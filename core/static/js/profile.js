document.addEventListener("DOMContentLoaded", function () {

    // Rellena campos del formulario con los datos guardados
    document.getElementById("fullname").value = fullname;
    document.getElementById("username").value = username;
    document.getElementById("email").value = email;
    document.getElementById("datebirth").value = datebirth;
    document.getElementById("phone").value = phone;
});

// Manejar la actualizacion del perfil
document.getElementById("SignUpForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Previene el envio automatico del formulario

    // Obtener los valores de los inputs
    const fullname = document.getElementById("fullname").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const datebirth = document.getElementById("datebirth").value;
    const phone = document.getElementById("phone").value;

    // Mensaje de exito
    alert("Profile updated successfully!");

    // Recarga pagina
    window.location.href = "./profile.html";
});
