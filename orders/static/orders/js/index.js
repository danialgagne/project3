document.addEventListener('DOMContentLoaded', () => {
    let cart = localStorage.getItem('cart') ?
        JSON.parse(localStorage.getItem('cart')) : []
    
    if (cart.length > 0) {
        document.getElementById('cart-icon').style.display = 'initial'
    }

    document.addEventListener('click', event => {
        const element = event.target;

        if (element.classList.contains('item')) {
            const item = create_cart_item(element)
            cart.push(item);
            localStorage.setItem('cart', JSON.stringify(cart));
            document.getElementById('cart-icon').style.display = 'initial'
        }

        const reset = ['Log out', 'Sign in', 'Sign up']
        if (reset.includes(element.textContent)) {
            cart = []
            localStorage.clear()
        }

        if (element.id == 'cart-icon') {toggle_cart()}
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
