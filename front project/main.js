// HTML elements
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const productsGrid = document.getElementById("productsGrid"); // <– Add this div to your HTML page

// Fetch products from DummyJSON
async function fetchProducts(query = '') {
  try {
    const endpoint = query
      ? `https://dummyjson.com/products/search?q=${encodeURIComponent(query)}`
      : 'https://dummyjson.com/products';

    const response = await fetch(endpoint);
    if (!response.ok) throw new Error('Failed to fetch products');

    const data = await response.json();
    return data.products; // ✅ This is the correct array
  } catch (error) {
    console.error('Error fetching products:', error);
    return [];
  }
}

// Display products
function displayProducts(products, container) {
  container.innerHTML = '';

  products.forEach(product => {
    const productsCard = document.createElement('div');
    productsCard.className = 'products-card';
  productsCard.innerHTML = `
  <div class="product-card">
    <a href="product.html?id=${JSON.stringify(product.id)}">
      <div class="product-tumb">
        <img src="${product.thumbnail}" alt="${product.title}">
      </div>
    </a>
    <div class="product-details">
      <span class="product-catagory">${product.category}</span>
      <h4><a href="product.html?id=${product.id}">${product.title}</a></h4>
      <p>${product.description}</p>
      <div class="product-bottom-details">
        <div class="product-price">
          <small>$${product.price + 50}</small> $${product.price}
        </div>
        <div class="product-links">
          <a href="#"><i class="fa-regular fa-heart"></i></a>
          <a href="#"><i class="fa-solid fa-cart-shopping"></i></a>
        </div>
      </div>
    </div>
  </div>
`;
    container.appendChild(productsCard);
  });
  
}
// Search button click event
searchBtn.addEventListener('click', async () => {
  const query = searchInput.value.trim();
  if (query) {
    const products = await fetchProducts(query);
    displayProducts(products, productsGrid);
  }
});

// Enter key event
searchInput.addEventListener('keypress', async (e) => {
  if (e.key === 'Enter') {
    const query = searchInput.value.trim();
    if (query) {
      const products = await fetchProducts(query);
      displayProducts(products, productsGrid);
    }
  }
});

// Initial load
async function init() {
  const products = await fetchProducts(); // ← no query means fetch all
  displayProducts(products, productsGrid);
}

init();
