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
        filters.forEach(function (b) { b.classList.remove('bg-[#0D0D0D]', 'dark:bg-[#ECECEC]', 'text-white', 'dark:text-[#0D0D0D]'); b.classList.add('bg-gray-100', 'dark:bg-[#2F2F2F]', 'text-[#0D0D0D]', 'dark:text-[#ECECEC]'); });
        btn.classList.add('bg-[#0D0D0D]', 'dark:bg-[#ECECEC]', 'text-white', 'dark:text-[#0D0D0D]');
        btn.classList.remove('bg-gray-100', 'dark:bg-[#2F2F2F]', 'text-[#0D0D0D]', 'dark:text-[#ECECEC]');

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
