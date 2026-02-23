// Theme toggle — class-based dark mode, respects OS preference, persists to localStorage
(function () {
  const STORAGE_KEY = 'trinly-theme';

  function getPreferred() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored === 'dark' || stored === 'light') return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function apply(theme) {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    localStorage.setItem(STORAGE_KEY, theme);
    // Update meta theme-color
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#212121' : '#ffffff');
  }

  // Apply immediately (called from inline script in <head> for anti-FOUC)
  window.__applyTheme = function () {
    apply(getPreferred());
  };

  // Toggle (called from button click)
  window.__toggleTheme = function () {
    const current = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
    apply(current === 'dark' ? 'light' : 'dark');
  };
})();
