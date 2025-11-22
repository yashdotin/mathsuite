(function(){
  const page = document.getElementById('page-content');
  if (!page) return;

  requestAnimationFrame(()=> {
    page.classList.add('page-enter-active');
  });

  function navigateWithExit(url){
    page.classList.remove('page-enter-active');
    page.classList.add('page-exit-active');
    setTimeout(()=> {
      window.location.href = url;
    }, 320);
  }

  document.addEventListener('click', function(e){
    let a = e.target;
    while(a && a.tagName !== 'A') a = a.parentElement;
    if(!a) return;
    if (a.target === '_blank' || a.hasAttribute('download')) return;
    const href = a.getAttribute('href');
    if (!href) return;
    if (href.startsWith('http') && !href.startsWith(location.origin)) return;
    if (href.startsWith('#')) return;
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;

    e.preventDefault();
    navigateWithExit(href);
  }, true);

})();
