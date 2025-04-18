function addToCart(productName, productPrice) {
    // Se recupera carrito actual desde localStorage
    let cart = localStorage.getItem('cart');
    
    // Si no hay carrito, se inicializa como array vacio
    if (!cart) {
      cart = [];
    } else {
      cart = cart.split(','); // Se convierte string del carrito en un array de productos
    }
    
    // Anade producto a carrito
    cart.push(`${productName} - $${productPrice}`);
    
    // Se guarda carrito en localStorage como string
    localStorage.setItem('cart', cart.join(','));
  
    // Alerta producto agregado
    alert(`${productName} has been added to your cart!`);
  }