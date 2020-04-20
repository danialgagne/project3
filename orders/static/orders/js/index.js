document.addEventListener('DOMContentLoaded', () => {
    let cart = localStorage.getItem('cart') ?
        JSON.parse(localStorage.getItem('cart')) : []

    document.addEventListener('click', event => {
        const element = event.target;
        const reset = ['Log out', 'Sign in', 'Sign up']

        if (element.classList.contains('item')) {
            const item = create_cart_item(element)
            cart.push(item);
            localStorage.setItem('cart', JSON.stringify(cart));
        }

        if (reset.includes(element.textContent)) {
            cart = []
            localStorage.clear()
        }
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