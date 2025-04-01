// Funcion para cargar el carrito desde localStorage y mostrar los productos
function loadCart() {
  // Se obtiene el carrito desde localStorage
  var cart = localStorage.getItem('cart'); 

  // Si no hay carrito, se inicializa array vacio
  var cartItems = cart ? cart.split(',') : [];

  // Se obtiene el contenedor donde se mostraran los productos
  var cartContainer = document.getElementById('cart-items');
  
  // Se obtiene el contenedor donde se mostrara el total
  var cartTotal = document.getElementById('cart-total');
  
  // Se inicializa el precio total en 0
  var totalPrice = 0;

  // Limpia el contenido previo del carrito
  cartContainer.innerHTML = '';

  // Se itera sobre los productos en el carrito
  cartItems.forEach(function(item, index) {
    // Creamos un nuevo elemento div para cada producto
    var itemElement = document.createElement('div');
    itemElement.classList.add('cart-item');
    
    // Extraemos el precio de cada producto desde el string
    var price = parseFloat(item.split('$')[1]);  // Toma la parte despues del simbolo "$"

    // Suma precio total
    totalPrice += price;

    // Define contenido HTML para mostrar el nombre y el precio de cada producto
    itemElement.innerHTML = `
      <p>${item}</p>
      <button onclick="removeFromCart(${index})" class="btn btn-sm btn-danger">Remove</button>
      <hr>
    `;


    // Se anade el producto al contenedor del carrito
    cartContainer.appendChild(itemElement);
  });

  // Se muestra el total en el contenedor
  cartTotal.innerHTML = `Total: $${totalPrice.toFixed(2)}`;
}

// Funcion para eliminar un producto del carrito
function removeFromCart(index) {
  // Se obtiene el carrito desde localStorage
  var cart = localStorage.getItem('cart'); 

  // Comprobar si hay carrito
  if (!cart) return;

  // Se convierte carrito a un array
  var cartItems = cart.split(',');

  // Se elimina el producto en el indice indicado
  cartItems.splice(index, 1);

  // Guarda el carrito actualizado en localStorage
  localStorage.setItem('cart', cartItems.join(','));

  // Recarga el carrito para actualizar la vista
  loadCart();
}

// Funcion para agregar un producto al carrito
function addToCart(productName, productPrice) {
  // Se obtiene el carrito actual desde localStorage
  var cart = localStorage.getItem('cart'); 

  // Si no hay carrito, inicializa un array vacio
  var cartItems = cart ? cart.split(',') : [];

  // Anade nuevo producto al carrito
  cartItems.push(`${productName} - $${productPrice}`);

  // Guarda carrito actualizado en localStorage
  localStorage.setItem('cart', cartItems.join(','));

  // Alerta producto agregado
  alert(`${productName} ha sido agregado al carrito.`);
}
