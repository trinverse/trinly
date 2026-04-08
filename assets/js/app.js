// Trinly — vanilla JS utilities
document.addEventListener('DOMContentLoaded', function () {
  // --- Page loader fadeout ---
  var loader = document.getElementById('page-loader');
  if (loader) {
    loader.style.opacity = '0';
    setTimeout(function () { loader.style.display = 'none'; }, 300);
  }

  // --- Mobile menu toggle ---
  var menuBtn = document.getElementById('mobile-menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', function () {
      var open = mobileMenu.classList.toggle('hidden');
      menuBtn.setAttribute('aria-expanded', !open);
    });
    // Close menu when a link is clicked
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.add('hidden');
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --- Scroll-to-top button ---
  var scrollBtn = document.getElementById('scroll-top');
  if (scrollBtn) {
    window.addEventListener('scroll', function () {
      scrollBtn.classList.toggle('hidden', window.scrollY < 400);
    });
    scrollBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // --- Portfolio filtering (vanilla, no Isotope) ---
  var filters = document.querySelectorAll('[data-filter]');
  var items = document.querySelectorAll('[data-category]');
  if (filters.length && items.length) {
    filters.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        // Update active state
        filters.forEach(function (b) { b.classList.remove('bg-gradient-to-r', 'from-[#7C3AED]', 'to-[#4F46E5]', 'text-white'); b.classList.add('bg-[#F0F0F8]', 'dark:bg-[#16161E]', 'text-[#0A0A1A]', 'dark:text-[#F0F0F5]'); });
        btn.classList.add('bg-gradient-to-r', 'from-[#7C3AED]', 'to-[#4F46E5]', 'text-white');
        btn.classList.remove('bg-[#F0F0F8]', 'dark:bg-[#16161E]', 'text-[#0A0A1A]', 'dark:text-[#F0F0F5]');

        var filter = btn.getAttribute('data-filter');
        items.forEach(function (item) {
          if (filter === '*' || item.getAttribute('data-category') === filter) {
            item.style.display = '';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // --- Scroll reveal for cards ---
  var reveals = document.querySelectorAll('[data-reveal]');
  if (reveals.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('opacity-100', 'translate-y-0');
          entry.target.classList.remove('opacity-0', 'translate-y-4');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    reveals.forEach(function (el) { observer.observe(el); });
  }

  // --- Smooth scroll for anchor links ---
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
