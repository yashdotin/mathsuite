
(function(){
  const cards = document.querySelectorAll('.interactive-card[data-tilt]');
  if (!cards.length) return;

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = e.clientX - cx;
      const dy = e.clientY - cy;
      const rx = (dy / rect.height) * -6; 
      const ry = (dx / rect.width) * 6; 
      card.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg) translateZ(6px)`;
      card.classList.add('tilt-active');
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
      card.classList.remove('tilt-active');
    });
  });
})();
