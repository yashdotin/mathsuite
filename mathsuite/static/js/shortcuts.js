
document.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    
    const el = document.activeElement;
    if (el && el.tagName === 'INPUT') {
      const form = el.closest('form');
      if (form) form.requestSubmit();
    }
  }
});
