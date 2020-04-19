document.addEventListener('DOMContentLoaded', () => {
    let cart = localStorage.getItem('cart') ?
        JSON.parse(localStorage.getItem('cart')) : []

    document.addEventListener('click', event => {
        const element = event.target;
        const reset = ['Log out', 'Sign in', 'Sign up']

        if (element.classList.contains('item')) {
            const row = element.closest('tr');
            let item = {
                'id': row.dataset.id,
                'name': row.dataset.name,
                'category': row.dataset.category,
                'size': element.dataset.size,
                'price': element.innerText
            };
            cart.push(item);
            localStorage.setItem('cart', JSON.stringify(cart));
        }

        if (reset.includes(element.textContent)) {
            cart = []
            localStorage.clear()
        }
    })  
})