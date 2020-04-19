document.addEventListener('DOMContentLoaded', () => {
    // if (localStorage.getItem('cart') === null) {
    //     const cart = [];
    //     localStorage.setItem('cart', JSON.stringify(cart));
    // } else {
    //     const cart = JSON.parse(localStorage.getItem('cart'));
    // }
    const cart = localStorage.getItem('cart') ?
        JSON.parse(localStorage.getItem('cart')) : []

    document.addEventListener('click', event => {
        const element = event.target;

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
    })  
})