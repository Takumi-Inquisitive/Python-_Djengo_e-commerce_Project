    document.addEventListener("DOMContentLoaded", function () {
        
            function removeFromCart(productId) {
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                fetch(`/remove_from_cart/${productId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({ product_id: productId })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Item removed from cart');
                        
                        document.getElementById(`cart-item-${productid}`).remove();
                    } else {
                        alert('Error: ' + data.message);
                    }
                })
                .catch(error => console.log('Error:', error));
            }
        
    });



