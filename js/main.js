// Menu mobile
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();

// Boutons « copier » sur les algos
document.querySelectorAll('.copy').forEach(function (b) {
  b.addEventListener('click', function () {
    var code = b.closest('.algo').querySelector('code').textContent.trim();
    var done = function () {
      var old = b.textContent;
      b.textContent = 'Copié';
      setTimeout(function () { b.textContent = old; }, 1400);
    };
    if (navigator.clipboard) {
      navigator.clipboard.writeText(code).then(done);
    } else {
      var t = document.createElement('textarea');
      t.value = code;
      document.body.appendChild(t);
      t.select();
      document.execCommand('copy');
      document.body.removeChild(t);
      done();
    }
  });
});

// Recherche dans le glossaire
(function () {
  var input = document.getElementById('gloss-search');
  if (!input) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('dl.gloss dt'));
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    items.forEach(function (dt) {
      var dd = dt.nextElementSibling;
      var hit = !q || (dt.textContent + ' ' + dd.textContent).toLowerCase().indexOf(q) !== -1;
      dt.classList.toggle('hide', !hit);
      dd.classList.toggle('hide', !hit);
    });
  });
})();
