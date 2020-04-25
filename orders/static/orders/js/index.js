document.addEventListener('DOMContentLoaded', () => {
    let cart = localStorage.getItem('cart') ?
        JSON.parse(localStorage.getItem('cart')) : []
    
    if (cart.length > 0) {
        document.getElementById('cart-icon').style.display = 'initial';
        cart.forEach(add_cart_item);
    }

    document.addEventListener('click', event => {
        const element = event.target;
        const modal = document.getElementById('toppings-modal');

        if (element.classList.contains('item')) {
            if (element.closest('tr').dataset.toppings == "True" ) {
                modal.style.display = 'block';
            }
            const item = create_cart_item(element);
            cart.push(item);
            localStorage.setItem('cart', JSON.stringify(cart));
            document.getElementById('cart-icon').style.display = 'initial';
            add_cart_item(item)
        }

        const reset = ['Log out', 'Sign in', 'Sign up']
        if (reset.includes(element.textContent)) {
            cart = [];
            localStorage.clear();
        }

        if (element.id == 'cart-icon') {toggle_cart()}
        if (element == modal) {modal.style.display = 'none'}
    })
})

function create_cart_item (el) {
    const row = el.closest('tr');
    let item = {
        'id': row.dataset.id,
        'name': row.dataset.name,
        'category': row.dataset.category,
        'size': el.dataset.size,
        'price': el.innerText
    };
    return item
}

function toggle_cart () {
    // document.getElementById('shopping-cart').style.width = '20em'
    document.getElementById('shopping-cart').style.width == '' ?
        document.getElementById('shopping-cart').style.width = '20em' :
        document.getElementById('shopping-cart').style.width = ''
}

const cart_item_template = Handlebars.compile(document.getElementById('cart-item').innerHTML);

function add_cart_item(contents) {
    const item = cart_item_template(contents)
    document.getElementById('shopping-cart').innerHTML += item
}

function add_toppings(toppings, quantity) {

}