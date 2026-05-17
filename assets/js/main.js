// CosplayItalia AI - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {

  // ============================================
  // MOBILE MENU TOGGLE
  // ============================================
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav = document.getElementById('mobileNav');

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', function() {
      mobileNav.classList.toggle('open');
      const icon = menuToggle.querySelector('i');
      if (mobileNav.classList.contains('open')) {
        icon.className = 'fas fa-times';
      } else {
        icon.className = 'fas fa-bars';
      }
    });
  }

  // ============================================
  // COOKIE BANNER
  // ============================================
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieConsent = localStorage.getItem('cookieConsent');

  if (!cookieConsent && cookieBanner) {
    setTimeout(function() {
      cookieBanner.classList.add('show');
    }, 1500);
  }

  // ============================================
  // SMOOTH SCROLL
  // ============================================
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ============================================
  // LAZY LOADING IMAGES
  // ============================================
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
          }
          imageObserver.unobserve(img);
        }
      });
    });

    document.querySelectorAll('img[data-src]').forEach(function(img) {
      imageObserver.observe(img);
    });
  }

  // ============================================
  // READING PROGRESS BAR
  // ============================================
  const article = document.querySelector('.post-content');
  if (article) {
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 3px;
      background: linear-gradient(90deg, #7c3aed, #ec4899, #f59e0b);
      z-index: 9999;
      transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', function() {
      const articleTop = article.offsetTop;
      const articleHeight = article.offsetHeight;
      const windowHeight = window.innerHeight;
      const scrollTop = window.scrollY;
      const progress = Math.min(
        Math.max((scrollTop - articleTop + windowHeight) / (articleHeight + windowHeight) * 100, 0),
        100
      );
      progressBar.style.width = progress + '%';
    });
  }

  // ============================================
  // BACK TO TOP BUTTON
  // ============================================
  const backToTop = document.createElement('button');
  backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
  backToTop.setAttribute('aria-label', 'Torna in cima');
  backToTop.style.cssText = `
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #7c3aed, #ec4899);
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1rem;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
    transition: all 0.3s ease;
    opacity: 0;
    transform: translateY(20px);
    z-index: 1000;
  `;
  document.body.appendChild(backToTop);

  window.addEventListener('scroll', function() {
    if (window.scrollY > 300) {
      backToTop.style.opacity = '1';
      backToTop.style.transform = 'translateY(0)';
    } else {
      backToTop.style.opacity = '0';
      backToTop.style.transform = 'translateY(20px)';
    }
  });

  backToTop.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  backToTop.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-3px)';
    this.style.boxShadow = '0 8px 25px rgba(124, 58, 237, 0.5)';
  });

  backToTop.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0)';
    this.style.boxShadow = '0 4px 15px rgba(124, 58, 237, 0.4)';
  });

  // ============================================
  // ANIMATE ON SCROLL
  // ============================================
  if ('IntersectionObserver' in window) {
    const animateObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          animateObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.post-card, .stat-item').forEach(function(el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      animateObserver.observe(el);
    });
  }

});

// ============================================
// COOKIE FUNCTIONS (global)
// ============================================
function acceptCookies() {
  localStorage.setItem('cookieConsent', 'accepted');
  const banner = document.getElementById('cookieBanner');
  if (banner) {
    banner.style.transform = 'translateY(100%)';
    banner.style.transition = 'transform 0.3s ease';
    setTimeout(function() { banner.remove(); }, 300);
  }
}

function declineCookies() {
  localStorage.setItem('cookieConsent', 'declined');
  const banner = document.getElementById('cookieBanner');
  if (banner) {
    banner.style.transform = 'translateY(100%)';
    banner.style.transition = 'transform 0.3s ease';
    setTimeout(function() { banner.remove(); }, 300);
  }
}
