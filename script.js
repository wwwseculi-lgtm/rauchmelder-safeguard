// Secu.li Europe - JavaScript
document.addEventListener('DOMContentLoaded', function () {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileNav = document.getElementById('mobileNav');

    if (mobileMenuBtn && mobileNav) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileNav.classList.toggle('active');
            this.classList.toggle('active');
        });

        // Close menu when clicking on a link
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileNav.classList.remove('active');
                mobileMenuBtn.classList.remove('active');
            });
        });
    }

    // Header scroll effect
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Contact Form Handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);

            // Simple validation
            const requiredFields = ['firstName', 'lastName', 'email', 'country', 'subject', 'message', 'privacy'];
            let isValid = true;

            requiredFields.forEach(field => {
                const input = document.getElementById(field);
                if (!input) return;

                if (field === 'privacy') {
                    if (!input.checked) {
                        isValid = false;
                        input.parentElement.style.color = '#EF4444';
                    } else {
                        input.parentElement.style.color = '';
                    }
                } else if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#EF4444';
                } else {
                    input.style.borderColor = '';
                }
            });

            // Email validation
            const emailInput = document.getElementById('email');
            if (emailInput && emailInput.value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(emailInput.value)) {
                    isValid = false;
                    emailInput.style.borderColor = '#EF4444';
                }
            }

            if (isValid) {
                // Show success message
                const btn = contactForm.querySelector('button[type="submit"]');
                const originalText = btn.textContent;
                btn.textContent = 'Wird gesendet...';
                btn.disabled = true;

                // Simulate form submission
                setTimeout(() => {
                    btn.textContent = '✓ Erfolgreich gesendet!';
                    btn.style.background = '#10B981';

                    // Reset form after delay
                    setTimeout(() => {
                        contactForm.reset();
                        btn.textContent = originalText;
                        btn.style.background = '';
                        btn.disabled = false;
                    }, 3000);
                }, 1500);
            }
        });

        // Remove error styling on input
        contactForm.querySelectorAll('input, select, textarea').forEach(input => {
            input.addEventListener('input', function () {
                this.style.borderColor = '';
            });
        });
    }

    // Animate elements on scroll
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.feature-card, .product-card, .testimonial-card, .country-card, .team-card, .stat-item');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        elements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    };

    animateOnScroll();

    // Stats counter animation
    const animateStats = () => {
        const statNumbers = document.querySelectorAll('.stat-number');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');
                    const text = entry.target.textContent;
                    const number = parseInt(text.replace(/[^\d]/g, ''));

                    if (!isNaN(number) && number > 0) {
                        let current = 0;
                        const increment = number / 50;
                        const suffix = text.replace(/[\d.,]/g, '');

                        const timer = setInterval(() => {
                            current += increment;
                            if (current >= number) {
                                current = number;
                                clearInterval(timer);
                            }

                            // Format number with dots for thousands
                            const formatted = Math.floor(current).toLocaleString('de-DE');
                            entry.target.textContent = formatted + suffix;
                        }, 30);
                    }
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(stat => observer.observe(stat));
    };

    animateStats();

    // Add loading placeholder for images
    document.querySelectorAll('img').forEach(img => {
        if (!img.complete) {
            img.style.background = '#E2E8F0';
        }

        img.addEventListener('load', function () {
            this.style.background = '';
        });

        img.addEventListener('error', function () {
            // Create placeholder for missing images
            this.style.display = 'flex';
            this.style.alignItems = 'center';
            this.style.justifyContent = 'center';
            this.style.background = 'linear-gradient(135deg, #E2E8F0, #CBD5E1)';
            this.style.color = '#64748B';
            this.alt = '📷 ' + (this.alt || 'Bild');
        });
    });
});

// Register Service Worker for PWA
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then((registration) => {
                console.log('SW registered:', registration.scope);
            })
            .catch((error) => {
                console.log('SW registration failed:', error);
            });
    });
}

// PWA Install Prompt
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;

    // Show install button if exists
    const installBtn = document.getElementById('installBtn');
    if (installBtn) {
        installBtn.style.display = 'block';
        installBtn.addEventListener('click', () => {
            deferredPrompt.prompt();
            deferredPrompt.userChoice.then((choiceResult) => {
                if (choiceResult.outcome === 'accepted') {
                    console.log('User accepted install');
                }
                deferredPrompt = null;
            });
        });
    }
});
