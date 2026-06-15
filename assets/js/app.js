// Trinly — minimal interactions (Claude-style calm UI)
document.addEventListener('DOMContentLoaded', function () {
  var loader = document.getElementById('page-loader');
  if (loader) {
    loader.style.opacity = '0';
    setTimeout(function () { loader.style.display = 'none'; }, 180);
  }

  var menuBtn = document.getElementById('mobile-menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', function () {
      var open = mobileMenu.classList.toggle('hidden');
      menuBtn.setAttribute('aria-expanded', !open);
    });
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.add('hidden');
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  var scrollBtn = document.getElementById('scroll-top');
  if (scrollBtn) {
    window.addEventListener('scroll', function () {
      scrollBtn.classList.toggle('hidden', window.scrollY < 400);
    }, { passive: true });
    scrollBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  var filters = document.querySelectorAll('[data-filter]');
  var items = document.querySelectorAll('[data-category]');
  if (filters.length && items.length) {
    filters.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        filters.forEach(function (b) {
          b.classList.remove('tl-filter-active');
          b.classList.add('tl-filter');
        });
        btn.classList.add('tl-filter-active');
        btn.classList.remove('tl-filter');
        var filter = btn.getAttribute('data-filter');
        items.forEach(function (item) {
          item.style.display = (filter === '*' || item.getAttribute('data-category') === filter) ? '' : 'none';
        });
      });
    });
  }

  var reveals = document.querySelectorAll('[data-reveal]');
  if (reveals.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('opacity-100', 'translate-y-0');
          entry.target.classList.remove('opacity-0', 'translate-y-5');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

    reveals.forEach(function (el, i) {
      el.classList.add('opacity-0', 'translate-y-5');
      el.style.transitionDelay = (i % 6) * 0.05 + 's';
      observer.observe(el);
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = this.getAttribute('href');
      if (id.length <= 1) return;
      var target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});
