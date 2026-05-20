/* ═══════════════════════════════════════════════════════════════
   GUSTOSSI BOLIVIA · categorias-data.js
   Detección automática de ruta — funciona desde index.html y pages/
═══════════════════════════════════════════════════════════════ */

// Detecta si estamos en /pages/ o en la raíz
const _base = window.location.pathname.includes('/pages/') ? '../' : '';

const CATS_DATA = {

  galleteria: {
    nombre:      'Galletería',
    descripcion: 'Crackers, chips de chocolate, galletas escolares y más variedades',
    icon:        'fa-cookie-bite',
    get heroImg() { return _base + 'images/categorias/galleteria.jpg'; },
    productos: [
      { nombre: 'Galleta Cracker',                         get img() { return _base + 'images/productos/galleta-chip-chocolate.jpg'; } },
      { nombre: 'Galleta Cracker Integral',                get img() { return _base + 'images/categorias/galleteria.jpg'; } },
      { nombre: 'Galleta Chip de Chocolate',               get img() { return _base + 'images/productos/bandeja-chip-chocolate.jpg'; } },
      { nombre: 'Galleta Choco Naranja',                   get img() { return _base + 'images/productos/bandeja-choco-naranja.jpg'; } },
      { nombre: 'Galleta de Almendra',                     get img() { return _base + 'images/productos/galleta-almendra-full.jpg'; } },
      { nombre: 'Galleta de Coco',                         get img() { return _base + 'images/productos/galleta-coco-full.jpg'; } },
      { nombre: 'Galleta de Hojaldre',                     get img() { return _base + 'images/productos/bandeja-hojaldre.jpg'; } },
      { nombre: 'Galletas Dulces Surtidas',                img: '' },
      { nombre: 'Galletas Dulce Rosquitas',                img: '' },
      { nombre: 'Galletas de Agua',                        img: '' },
      { nombre: 'Galletas Escolares Animalitos',           img: '' },
      { nombre: 'Galletas Escolares Caritas',              img: '' },
      { nombre: 'Galletas Escolares Chiquisalada',         img: '' },
      { nombre: 'Galletas Escolares MiniCracker',          img: '' },
      { nombre: 'Galletas Escolares Rosquitas',            img: '' },
      { nombre: 'Galleta Cracker Integral Avena con Chía', img: '' },
    ],
  },

  reposteria: {
    nombre:      'Repostería',
    descripcion: 'Dulces, pasteles y delicias de repostería artesanal boliviana',
    icon:        'fa-cake-candles',
    get heroImg() { return _base + 'images/categorias/reposteria.jpg'; },
    productos: [
      { nombre: 'Torta de Chocolate',     get img() { return _base + 'images/productos/reposteria-varios.png'; } },
      { nombre: 'Torta Surtida',          img: '' },
      { nombre: 'Alfajores',              img: '' },
      { nombre: 'Bizcochos Surtidos',     img: '' },
      { nombre: 'Galleta de Mantequilla', img: '' },
    ],
  },

  navideno: {
    nombre:      'Navideño',
    descripcion: 'Panetón tradicional, roscas navideñas y productos especiales de temporada',
    icon:        'fa-gifts',
    get heroImg() { return _base + 'images/categorias/navideno.jpg'; },
    productos: [
      { nombre: 'Panetón Tradicional',  get img() { return _base + 'images/productos/paneton-tradicional-full.jpg'; } },
      { nombre: 'Panetón de Chocolate', get img() { return _base + 'images/productos/paneton-chocolate-full.jpg'; } },
      { nombre: 'Rosca Navideña',       get img() { return _base + 'images/productos/rosca-navidena.jpg'; } },
      { nombre: 'Turrones Navideños',   img: '' },
      { nombre: 'Galletas Navideñas',   img: '' },
    ],
  },

  wafer: {
    nombre:      'Wafer',
    descripcion: 'Obleas crujientes rellenas con cremas en deliciosos sabores',
    icon:        'fa-layer-group',
    get heroImg() { return _base + 'images/categorias/wafer.jpg'; },
    productos: [
      { nombre: 'Wafer de Vainilla',  img: '' },
      { nombre: 'Wafer de Fresa',     img: '' },
      { nombre: 'Wafer de Chocolate', img: '' },
      { nombre: 'Wafer de Limón',     img: '' },
      { nombre: 'Wafer Surtido',      img: '' },
    ],
  },

  rellenas: {
    nombre:      'Rellenas',
    descripcion: 'Galletas rellenas con cremosas y deliciosas variedades de sabores',
    icon:        'fa-heart',
    get heroImg() { return _base + 'images/categorias/rellenas.jpg'; },
    productos: [
      { nombre: 'Rellena de Vainilla',  img: '' },
      { nombre: 'Rellena de Chocolate', img: '' },
      { nombre: 'Rellena de Fresa',     img: '' },
      { nombre: 'Rellena de Limón',     img: '' },
      { nombre: 'Rellena Surtida',      img: '' },
      { nombre: 'Gustossito',           get img() { return _base + 'images/hero/banner-gustossito.jpg'; } },
    ],
  },

  queques: {
    nombre:      'Queques',
    descripcion: 'Queques esponjosos y quequitos en variados sabores para toda la familia',
    icon:        'fa-bread-slice',
    get heroImg() { return _base + 'images/categorias/queques.jpg'; },
    productos: [
      { nombre: 'Queque Marmolado Surtido', get img() { return _base + 'images/productos/queque-marmolado.png'; } },
      { nombre: 'Quequito Surtido',         img: '' },
      { nombre: 'Queque de Vainilla',       img: '' },
      { nombre: 'Queque de Chocolate',      img: '' },
      { nombre: 'Queque de Plátano',        img: '' },
    ],
  },

};
