let carrito = [];

// Función para agregar un producto al carrito
function agregarAlCarrito(id, nombre, precio) {
  // Verificar si el producto ya está en el carrito
  const productoExistente = carrito.find(producto => producto.id === id);

  if (productoExistente) {
    // El producto ya existe en el carrito, se actualiza la cantidad
    productoExistente.cantidad++;
  } else {
    // El producto no existe en el carrito, se agrega con cantidad 1
    const nuevoProducto = {
      id,
      nombre,
      precio,
      cantidad: 1
    };
    carrito.push(nuevoProducto);
  }   // Actualizar el carrito en la página
  mostrarCarrito();
}

// Función para vaciar el carrito
function vaciarCarrito() {
  carrito = [];

  // Actualizar el carrito en la página
  mostrarCarrito();
}

// Función para mostrar el carrito en la página
function mostrarCarrito() {
  const carritoElemento = document.getElementById('carrito');
  const totalElemento = document.getElementById('total');

  // Limpiar el carrito anterior
  carritoElemento.innerHTML = '';

  // Mostrar los productos en el carrito
  carrito.forEach(producto => {
    const { id, nombre, precio, cantidad } = producto;

    const productoHTML = `
      <li>Nombre: ${nombre} | Precio: $${precio} | Cantidad: ${cantidad}</li>
    `;

    carritoElemento.innerHTML += productoHTML;
  });

  // Calcular el total del carrito
  const total = carrito.reduce((suma, producto) => suma + producto.precio * producto.cantidad, 0);
  totalElemento.textContent = total.toFixed(2);
}

// Manejar el evento de carga de la página
window.addEventListener('DOMContentLoaded', () => {
  // Mostrar el carrito al cargar la página
  mostrarCarrito();
});

// Función para eliminar un producto del carrito
function eliminarDelCarrito(id) {
  // Encontrar el índice del producto en el carrito
  const indiceProducto = carrito.findIndex(producto => producto.id === id);

  if (indiceProducto !== -1) {
    // Eliminar el producto del carrito
    carrito.splice(indiceProducto, 1);
  }

  // Actualizar el carrito en la página
  mostrarCarrito();
}

function pagarCarrito() {
  if (carrito.length === 0) {
    alert("El carrito está vacío. No se puede proceder al pago.");
    return;
  }

  var montoAPagarElement = document.getElementById("total");
  var monto = parseInt(montoAPagarElement.textContent);
  montoAPagarElement.textContent = monto;

  // Almacenar el resultado en localStorage
  localStorage.setItem('monto', monto);

  // Redirigir a la página de pago
  window.location.href = '{% url 'pago' %}';
}
