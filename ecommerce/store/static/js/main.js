// Utility function for smooth animations
const animate = (element, keyframes, options) => {
    return element.animate(keyframes, {
        duration: options.duration || 300,
        easing: options.easing || 'ease',
        fill: options.fill || 'forwards'
    });
};

// Add to cart animation
const addToCartAnimation = (button) => {
    const cart = document.querySelector('.cart-icon');
    if (!cart) return;

    const buttonRect = button.getBoundingClientRect();
    const cartRect = cart.getBoundingClientRect();

    const clone = button.cloneNode(true);
    clone.style.position = 'fixed';
    clone.style.top = `${buttonRect.top}px`;
    clone.style.left = `${buttonRect.left}px`;
    clone.style.zIndex = '1000';
    document.body.appendChild(clone);

    const animation = animate(clone, [
        { transform: 'scale(1)', opacity: 1 },
        { transform: 'scale(0.5)', opacity: 0.5 },
        { transform: 'scale(0.2)', opacity: 0 }
    ], {
        duration: 800,
        easing: 'cubic-bezier(0.4, 0, 0.2, 1)'
    });

    animation.onfinish = () => {
        clone.remove();
        cart.classList.add('bounce');
        setTimeout(() => cart.classList.remove('bounce'), 1000);
    };
};

// Product card hover effects
const initProductCards = () => {
    const cards = document.querySelectorAll('.product-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
};

// Cart item removal animation
const removeCartItem = (item) => {
    const animation = animate(item, [
        { transform: 'translateX(0)', opacity: 1 },
        { transform: 'translateX(-100%)', opacity: 0 }
    ], {
        duration: 300,
        easing: 'ease-out'
    });

    animation.onfinish = () => {
        item.remove();
    };
};

// Form validation with visual feedback
const initFormValidation = () => {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('invalid', (e) => {
                e.preventDefault();
                input.classList.add('error');
                const animation = animate(input, [
                    { transform: 'translateX(0)' },
                    { transform: 'translateX(-5px)' },
                    { transform: 'translateX(5px)' },
                    { transform: 'translateX(0)' }
                ], {
                    duration: 400,
                    easing: 'ease-in-out'
                });
            });

            input.addEventListener('input', () => {
                input.classList.remove('error');
            });
        });
    });
};

// Smooth scroll for navigation
const initSmoothScroll = () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
};

// Initialize all features
document.addEventListener('DOMContentLoaded', function() {
    initProductCards();
    initFormValidation();
    initSmoothScroll();

    // Add to cart button listeners
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Don't prevent form submission
            const button = this;
            button.classList.add('bounce');
            
            // Remove the animation class after animation completes
            setTimeout(() => {
                button.classList.remove('bounce');
            }, 500);
        });
    });
    
    // Mobile menu toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            this.classList.toggle('active');
        });
    }
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();
            
            if (email) {
                // In a real application, you would send this to your backend
                // For now, we'll just show a success message
                const formContainer = this.parentElement;
                formContainer.innerHTML = `
                    <h2 class="text-gradient">Thank You!</h2>
                    <p>You've been successfully subscribed to our newsletter.</p>
                `;
            }
        });
    }

    // Remove from cart button listeners
    document.querySelectorAll('.remove-from-cart-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            const item = e.target.closest('.cart-item');
            if (item) {
                removeCartItem(item);
            }
        });
    });
}); 