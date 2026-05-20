# Gustossi Bolivia — Sitio Web
**El Sabor del Buen Gusto**

## 📁 Estructura de carpetas

```
gustossi-web/
│
├── index.html              ← Página principal
├── css/
│   └── style.css           ← Todos los estilos
├── js/
│   └── main.js             ← Lógica, slider y datos
├── images/
│   ├── icons/              ← Logo (logo.png, logo-white.png, favicon.ico)
│   ├── hero/               ← Banners del slider principal
│   ├── productos/          ← Fotos de cada producto
│   ├── categorias/         ← Fotos de categorías
│   ├── recetas/            ← Fotos de recetas
│   └── reviews/            ← Fotos de clientes (opcional)
└── pages/                  ← Páginas internas (próximamente)
```

---

## 🖼️ Cómo agregar imágenes

### 1. Logo
Coloca los archivos en `images/icons/`:
- `logo.png` — logo color (para el nav)
- `logo-white.png` — logo blanco (para el footer)
- `favicon.ico` — ícono del navegador

Luego en `index.html`, reemplaza en el nav:
```html
<!-- ANTES (ícono temporal) -->
<i class="fa-solid fa-cookie-bite"></i> Gustos<span>si</span>

<!-- DESPUÉS (con logo real) -->
<img src="images/icons/logo.png" alt="Gustossi" class="nav-logo-img">
```

### 2. Productos, categorías, recetas y hero

Abre el archivo `js/main.js` y busca las secciones `DATA.heroSlides`, `DATA.productos`, `DATA.categorias`, `DATA.recetas`.

En cada objeto, rellena el campo `img` con la ruta de la imagen:

```js
// ANTES (sin imagen, muestra ícono)
{ nombre: 'Panetón Tradicional', img: '', ... }

// DESPUÉS (con imagen real)
{ nombre: 'Panetón Tradicional', img: 'images/productos/paneton-tradicional.jpg', ... }
```

---

## 🚀 Subir a GitHub Pages

1. Crea un repositorio en GitHub (ej: `gustossi-web`)
2. Sube todos los archivos
3. Ve a **Settings → Pages → Source: main / root**
4. Tu sitio estará en: `https://tuusuario.github.io/gustossi-web/`

---

## 🎨 Colores oficiales Gustossi

| Variable         | Color     | Uso                  |
|------------------|-----------|----------------------|
| `--brand`        | `#C8440A` | Naranja principal    |
| `--brand-dark`   | `#9B3008` | Hover / oscuro       |
| `--brand-light`  | `#FAECE7` | Fondos suaves        |
| `--cream`        | `#FDF8F2` | Fondo general        |
| `--brown`        | `#3D2008` | Texto títulos        |
| `--warm`         | `#F5E6D0` | Fondos alternos      |

---

## ✏️ Editar contenido

Todo el contenido (productos, reviews, recetas, stats) está centralizado en el objeto `DATA` al inicio de `js/main.js`. Solo edita ese archivo para actualizar la web.
