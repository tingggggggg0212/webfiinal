// Basic interactivity
document.addEventListener('DOMContentLoaded', () => {
    // Add active class to current nav item
    const currentPath = window.location.pathname.split('/').pop();
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath || (currentPath === '' && link.getAttribute('href') === 'index.html')) {
            link.classList.add('active');
        }
    });

    // Size selector functionality
    const sizeBtns = document.querySelectorAll('.size-btn');
    sizeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            sizeBtns.forEach(b => b.classList.remove('selected'));
            btn.classList.add('selected');
        });
    });

    // Add to cart animation
    const addToCartBtn = document.querySelector('.add-to-cart');
    if (addToCartBtn) {
        addToCartBtn.addEventListener('click', function() {
            const originalText = this.innerText;
            this.innerText = 'Added to Cart!';
            this.style.backgroundColor = '#4CAF50';
            this.style.borderColor = '#4CAF50';
            this.style.color = '#fff';
            
            setTimeout(() => {
                this.innerText = originalText;
                this.style.backgroundColor = '';
                this.style.borderColor = '';
                this.style.color = '';
            }, 2000);
        });
    }
});
