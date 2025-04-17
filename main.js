const PICO_BASE = 'http://192.168.1.42';  // ← mets ici l'IP que t'affiche la Pico au boot

function dispense(name) {
  fetch(`${PICO_BASE}/dispense?cocktail=${name}`)
    .then(r => r.json())
    .then(json => {
      if (json.status==='ok') {
        alert(`Cocktail ${name} lancé !`);
      } else {
        alert('Erreur : ' + json.error);
      }
    })
    .catch(err => {
      console.error(err);
      alert('Impossible de joindre la Pico à ' + PICO_BASE);
    });
}

document.querySelectorAll('.btn-dispense').forEach(btn => {
  btn.addEventListener('click', () => {
    const name = btn.dataset.cocktail;
    dispense(name);
  });
});