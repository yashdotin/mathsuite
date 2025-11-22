
(function() {
  const btn = document.getElementById('themeToggle');
  if (!btn) return;
  const body = document.body;

 
  const saved = localStorage.getItem('mathsuite_theme');
  if (saved === 'dark') {
    body.classList.add('dark');
    btn.innerHTML = `<i class="bi bi-brightness-high"></i>`;
  } else {
    btn.innerHTML = `<i class="bi bi-moon-stars"></i>`;
  }

  btn.addEventListener('click', function() {
    
    body.classList.add('theme-transition');
    window.setTimeout(() => body.classList.remove('theme-transition'), 350);

    const isDark = body.classList.toggle('dark');
    if (isDark) {
      btn.innerHTML = `<i class="bi bi-brightness-high"></i>`;
      localStorage.setItem('mathsuite_theme', 'dark');
    } else {
      btn.innerHTML = `<i class="bi bi-moon-stars"></i>`;
      localStorage.setItem('mathsuite_theme', 'light');
    }
  });
})();
