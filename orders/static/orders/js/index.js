document.addEventListener("DOMContentLoaded", () => {
  let cart = localStorage.getItem("cart")
    ? JSON.parse(localStorage.getItem("cart"))
    : [];

  if (cart.length > 0) {
    document.getElementById("cart-icon").style.display = "initial";
    cart.forEach(add_cart_item);
  }

  document.addEventListener("click", (event) => {
    const element = event.target;

    if (element.classList.contains("item")) {
      const item = create_cart_item(element);
      cart.push(item);
      localStorage.setItem("cart", JSON.stringify(cart));
      document.getElementById("cart-icon").style.display = "initial";
      add_cart_item(item);
    }

    const reset = ["Log out", "Sign in", "Sign up"];
    if (reset.includes(element.textContent)) {
      cart = [];
      localStorage.clear();
    }

    if (element.id == "cart-icon") {
      toggle_cart();
    }
  });
});

function create_cart_item(el) {
  const row = el.closest("tr");
  let item = {
    id: row.dataset.id,
    name: row.dataset.name,
    category: row.dataset.category,
    size: el.dataset.size,
    price: el.innerText,
  };
  return item;
}

function toggle_cart() {
  document.getElementById("shopping-cart").style.width == ""
    ? (document.getElementById("shopping-cart").style.width = "20em")
    : (document.getElementById("shopping-cart").style.width = "");
}

const cart_item_template = Handlebars.compile(
  document.getElementById("cart-item").innerHTML
);

function add_cart_item(contents) {
  const item = cart_item_template(contents);
  document.getElementById("shopping-cart").innerHTML += item;
}

const topping_modal_template = Handlebars.compile(document.getElementById('topping-select').innerHTML);

function add_toppings(toppings, qty) {
    const content = { 'topping': [] }
    for (let i = 1; i <= qty; i++) {
        const selector = {
            'id': 'topping' + i,
            'name': 'Topping ' + i,
            'toppings': JSON.parse(toppings)
        }
        content.topping.push(selector)
    }
    const toppings_selector = topping_modal_template(content)
    document.getElementById('toppings-modal-content').innerHTML = toppings_selector
}