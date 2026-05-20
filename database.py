# ═══════════════════════════════════════════════════════════════
#  GUSTOSSI BOLIVIA · database.py · Creación de Base de Datos
#  Base de datos SQLite para almacenar productos y datos
# ═══════════════════════════════════════════════════════════════

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'gustossi.db')

def crear_base_datos():
    """Crea la base de datos SQLite y todas las tablas"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # ── TABLA: Categorías ──
    c.execute('''CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        icon TEXT,
        hero_img TEXT
    )''')

    # ── TABLA: Productos ──
    c.execute('''CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria_slug TEXT NOT NULL,
        imagen TEXT DEFAULT '',
        destacado INTEGER DEFAULT 0,
        precio REAL DEFAULT 0,
        FOREIGN KEY (categoria_slug) REFERENCES categorias(slug)
    )''')

    # ── TABLA: Reviews ──
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        fuente TEXT,
        icono TEXT,
        avatar TEXT,
        iniciales TEXT,
        texto TEXT,
        estrellas INTEGER DEFAULT 5
    )''')

    # ── TABLA: Recetas ──
    c.execute('''CREATE TABLE IF NOT EXISTS recetas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        fecha TEXT,
        imagen TEXT
    )''')

    # ── TABLA: Estadísticas ──
    c.execute('''CREATE TABLE IF NOT EXISTS estadisticas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero TEXT NOT NULL,
        etiqueta TEXT NOT NULL,
        icono TEXT
    )''')

    # ── TABLA: Timeline / Historia ──
    c.execute('''CREATE TABLE IF NOT EXISTS timeline (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        anio TEXT NOT NULL,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        imagen TEXT
    )''')

    # ── TABLA: Ciudades de distribución ──
    c.execute('''CREATE TABLE IF NOT EXISTS ciudades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        icono TEXT,
        descripcion TEXT
    )''')

    # ── TABLA: Certificaciones ──
    c.execute('''CREATE TABLE IF NOT EXISTS certificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        icono TEXT,
        titulo TEXT NOT NULL,
        descripcion TEXT
    )''')

    # ── TABLA: Slides del Hero ──
    c.execute('''CREATE TABLE IF NOT EXISTS hero_slides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imagen TEXT NOT NULL,
        categoria TEXT,
        nombre TEXT,
        subtitulo TEXT,
        link TEXT
    )''')

    # ── TABLA: Configuración general ──
    c.execute('''CREATE TABLE IF NOT EXISTS configuracion (
        clave TEXT PRIMARY KEY,
        valor TEXT
    )''')

    conn.commit()
    return conn


def insertar_datos(conn):
    """Inserta todos los datos iniciales en la base de datos"""
    c = conn.cursor()

    # ── Limpiar datos existentes ──
    tablas = ['categorias', 'productos', 'reviews', 'recetas', 'estadisticas',
              'timeline', 'ciudades', 'certificaciones', 'hero_slides', 'configuracion']
    for tabla in tablas:
        c.execute(f'DELETE FROM {tabla}')

    # ═══ CATEGORÍAS ═══
    categorias = [
        ('galleteria', 'Galletería', 'Crackers, chips de chocolate, galletas escolares y más variedades', 'fa-cookie-bite', 'images/categorias/galleteria.jpg'),
        ('reposteria', 'Repostería', 'Dulces, pasteles y delicias de repostería artesanal boliviana', 'fa-cake-candles', 'images/categorias/reposteria.jpg'),
        ('navideno', 'Navideño', 'Panetón tradicional, roscas navideñas y productos especiales de temporada', 'fa-gifts', 'images/categorias/navideno.jpg'),
        ('wafer', 'Wafer', 'Obleas crujientes rellenas con cremas en deliciosos sabores', 'fa-layer-group', 'images/categorias/wafer.jpg'),
        ('rellenas', 'Rellenas', 'Galletas rellenas con cremosas y deliciosas variedades de sabores', 'fa-heart', 'images/categorias/rellenas.jpg'),
        ('queques', 'Queques', 'Queques esponjosos y quequitos en variados sabores para toda la familia', 'fa-bread-slice', 'images/categorias/queques.jpg'),
    ]
    c.executemany('INSERT INTO categorias (slug, nombre, descripcion, icon, hero_img) VALUES (?,?,?,?,?)', categorias)

    # ═══ PRODUCTOS ═══
    productos = [
        # Galletería
        ('Galleta Cracker', 'galleteria', 'images/productos/galleta-chip-chocolate.jpg', 0),
        ('Galleta Cracker Integral', 'galleteria', 'images/categorias/galleteria.jpg', 0),
        ('Galleta Chip de Chocolate', 'galleteria', 'images/productos/bandeja-chip-chocolate.jpg', 1),
        ('Galleta Choco Naranja', 'galleteria', 'images/productos/bandeja-choco-naranja.jpg', 1),
        ('Galleta de Almendra', 'galleteria', 'images/productos/galleta-almendra-full.jpg', 1),
        ('Galleta de Coco', 'galleteria', 'images/productos/galleta-coco-full.jpg', 1),
        ('Galleta de Hojaldre', 'galleteria', 'images/productos/bandeja-hojaldre.jpg', 1),
        ('Galletas Dulces Surtidas', 'galleteria', '', 0),
        ('Galletas Dulce Rosquitas', 'galleteria', '', 0),
        ('Galletas de Agua', 'galleteria', '', 0),
        ('Galletas Escolares Animalitos', 'galleteria', '', 0),
        ('Galletas Escolares Caritas', 'galleteria', '', 0),
        ('Galletas Escolares Chiquisalada', 'galleteria', '', 0),
        ('Galletas Escolares MiniCracker', 'galleteria', '', 0),
        ('Galletas Escolares Rosquitas', 'galleteria', '', 0),
        ('Galleta Cracker Integral Avena con Chía', 'galleteria', '', 0),
        # Repostería
        ('Torta de Chocolate', 'reposteria', 'images/productos/reposteria-varios.png', 0),
        ('Torta Surtida', 'reposteria', '', 0),
        ('Alfajores', 'reposteria', '', 0),
        ('Bizcochos Surtidos', 'reposteria', '', 0),
        ('Galleta de Mantequilla', 'reposteria', '', 0),
        # Navideño
        ('Panetón Tradicional', 'navideno', 'images/productos/paneton-tradicional.jpg', 1),
        ('Panetón de Chocolate', 'navideno', 'images/productos/paneton-chocolate.jpg', 1),
        ('Rosca Navideña', 'navideno', 'images/productos/rosca-navidena.jpg', 1),
        ('Turrones Navideños', 'navideno', '', 0),
        ('Galletas Navideñas', 'navideno', '', 0),
        # Wafer
        ('Wafer de Vainilla', 'wafer', '', 0),
        ('Wafer de Fresa', 'wafer', '', 0),
        ('Wafer de Chocolate', 'wafer', '', 0),
        ('Wafer de Limón', 'wafer', '', 0),
        ('Wafer Surtido', 'wafer', '', 0),
        # Rellenas
        ('Rellena de Vainilla', 'rellenas', '', 0),
        ('Rellena de Chocolate', 'rellenas', '', 0),
        ('Rellena de Fresa', 'rellenas', '', 0),
        ('Rellena de Limón', 'rellenas', '', 0),
        ('Rellena Surtida', 'rellenas', '', 0),
        ('Gustossito', 'rellenas', 'images/hero/banner-gustossito.jpg', 0),
        # Queques
        ('Queque Marmolado Surtido', 'queques', 'images/productos/queque-marmolado.png', 0),
        ('Quequito Surtido', 'queques', '', 0),
        ('Queque de Vainilla', 'queques', '', 0),
        ('Queque de Chocolate', 'queques', '', 0),
        ('Queque de Plátano', 'queques', '', 0),
    ]
    c.executemany('INSERT INTO productos (nombre, categoria_slug, imagen, destacado) VALUES (?,?,?,?)', productos)

    # ═══ HERO SLIDES ═══
    slides = [
        ('images/hero/slide-galleteria.jpg', 'Galletería', 'Galletería', 'Las más ricas galletas de Bolivia', 'pages/categoria.html?cat=galleteria'),
        ('images/hero/slide-cracker.jpg', 'Galletería', 'Repostería', 'Las más ricas galletas de Bolivia', 'pages/categoria.html?cat=reposteria'),
        ('images/hero/slide-rellenas.jpg', 'Rellenas', 'Rellena', 'Variedad en productos rellenos de sabores', 'pages/categoria.html?cat=rellenas'),
        ('images/hero/slide-navideno.jpg', 'Navideño', 'Navideño', 'Variedad en productos navideños: Panetón, etc.', 'pages/categoria.html?cat=navideno'),
        ('images/hero/slide-wafer.jpg', 'Wafer', 'Wafer', 'Deliciosas galletas obleas, de varios sabores.', 'pages/categoria.html?cat=wafer'),
        ('images/hero/slide-gustossito.jpg', 'Galletería', 'Queque', 'Deliciosas galletas obleas, de varios sabores.', 'pages/categoria.html?cat=queques'),
    ]
    c.executemany('INSERT INTO hero_slides (imagen, categoria, nombre, subtitulo, link) VALUES (?,?,?,?,?)', slides)

    # ═══ REVIEWS ═══
    reviews = [
        ('Irene Miranda', 'Facebook', 'fa-brands fa-facebook', 'images/reviews/irene.png', 'IM', '"Me encantan las deliciosas galletas Cracker. Son las mejores que he probado en Bolivia."', 5),
        ('Juan Velarde', 'Facebook', 'fa-brands fa-facebook', 'images/reviews/juan-velarde.png', 'JV', '"Soy un adicto a las galletas rellenitas. Las compro todas las semanas sin falta."', 5),
        ('Cristina Aguilar', 'Instagram', 'fa-brands fa-instagram', 'images/reviews/cristina.png', 'CA', '"Quisiera más sabores de las galletas rellenitas, me encantan. ¡Sigan así!"', 5),
        ('Juan Peredo', 'Google', 'fa-brands fa-google', 'images/reviews/juan-peredo.png', 'JP', '"Utilizo las deliciosas galletas crackers integrales en mis preparaciones. ¡Excelentes!"', 5),
    ]
    c.executemany('INSERT INTO reviews (nombre, fuente, icono, avatar, iniciales, texto, estrellas) VALUES (?,?,?,?,?,?,?)', reviews)

    # ═══ RECETAS ═══
    recetas = [
        ('Tiramisú con Galletas Cracker', 'Nov 12, 2020', 'images/recetas/tiramisu.jpg'),
        ('Tarta de Crema con Galletas Cracker', 'Nov 12, 2020', 'images/recetas/tarta-crema.png'),
        ('Leche Frita con Galletas de Agua', 'Nov 12, 2020', 'images/recetas/leche-frita.jpg'),
    ]
    c.executemany('INSERT INTO recetas (titulo, fecha, imagen) VALUES (?,?,?)', recetas)

    # ═══ ESTADÍSTICAS ═══
    stats = [
        ('25+', 'Años de experiencia', 'fa-calendar-check'),
        ('30+', 'Productos en línea', 'fa-boxes-stacked'),
        ('500+', 'Puntos de venta', 'fa-store'),
        ('100K+', 'Clientes satisfechos', 'fa-face-smile'),
    ]
    c.executemany('INSERT INTO estadisticas (numero, etiqueta, icono) VALUES (?,?,?)', stats)

    # ═══ TIMELINE ═══
    timeline = [
        ('2000', 'Fundación', 'Nace Industrias Alimenticias Gustossi S.R.L. en la ciudad de Santa Cruz de la Sierra, con una visión de ofrecer productos de calidad.', 'images/hero/slide-galleteria.jpg'),
        ('2005', 'Primera línea', 'Lanzamos nuestra primera línea de galletas artesanales que rápidamente conquistan el mercado cruceño.', 'images/productos/galleta-chip-chocolate.jpg'),
        ('2010', 'Expansión nacional', 'Nuestros productos llegan a los 9 departamentos de Bolivia. Se inauguran nuevas líneas de producción.', 'images/factory.png'),
        ('2015', 'Línea Navideña', 'Se lanza la exitosa línea de Panetón Gustossi, que se convierte en favorita de las familias bolivianas.', 'images/productos/paneton-tradicional.jpg'),
        ('2020', 'Innovación', 'Incorporamos nuevas tecnologías de producción y ampliamos nuestro portafolio con wafers, queques y rellenas.', 'images/hero/slide-wafer.jpg'),
        ('2026', 'Líderes del mercado', 'Consolidados como una de las marcas líderes en galletería de Bolivia, con más de 30 productos y 500 puntos de venta.', 'images/distribution.png'),
    ]
    c.executemany('INSERT INTO timeline (anio, titulo, descripcion, imagen) VALUES (?,?,?,?)', timeline)

    # ═══ CIUDADES ═══
    ciudades = [
        ('Santa Cruz', 'fa-building', 'Sede central y planta de producción'),
        ('La Paz', 'fa-mountain-sun', 'Distribución en toda la ciudad'),
        ('Cochabamba', 'fa-city', 'Centro de distribución regional'),
        ('Sucre', 'fa-landmark', 'Cobertura en capital constitucional'),
        ('Tarija', 'fa-wine-glass', 'Presencia en mercados locales'),
        ('Oruro', 'fa-masks-theater', 'Distribución activa'),
        ('Potosí', 'fa-gem', 'Llegamos a la ciudad imperial'),
        ('Beni', 'fa-tree', 'Cobertura en Trinidad y Riberalta'),
        ('Pando', 'fa-leaf', 'Presencia en Cobija'),
    ]
    c.executemany('INSERT INTO ciudades (nombre, icono, descripcion) VALUES (?,?,?)', ciudades)

    # ═══ CERTIFICACIONES ═══
    certs = [
        ('fa-shield-halved', 'SENASAG', 'Registro sanitario y control de calidad alimentaria certificada por el Servicio Nacional.'),
        ('fa-certificate', 'ISO 9001', 'Sistema de gestión de calidad que garantiza procesos estandarizados y mejora continua.'),
        ('fa-leaf', 'Ingredientes Naturales', 'Utilizamos ingredientes naturales seleccionados, sin conservantes artificiales dañinos.'),
        ('fa-recycle', 'Compromiso Ambiental', 'Empaques responsables y procesos que minimizan el impacto ambiental.'),
        ('fa-users', 'Responsabilidad Social', 'Generamos empleo digno y apoyamos a comunidades productoras bolivianas.'),
        ('fa-truck-fast', 'Cadena de Frío', 'Distribución con cadena de frío que garantiza la frescura de cada producto.'),
    ]
    c.executemany('INSERT INTO certificaciones (icono, titulo, descripcion) VALUES (?,?,?)', certs)

    # ═══ CONFIGURACIÓN ═══
    config = [
        ('nombre_empresa', 'Gustossi Bolivia'),
        ('slogan', 'El Sabor del Buen Gusto'),
        ('whatsapp', '59175256114'),
        ('facebook', 'https://www.facebook.com/GustossiBolivia'),
        ('instagram', 'https://www.instagram.com/gustossibolivia/'),
        ('tiktok', 'https://www.tiktok.com/@gustossibolivia'),
        ('email', 'contacto@gustossi.com'),
        ('direccion', 'Santa Cruz de la Sierra, Bolivia'),
        ('año_fundacion', '2000'),
    ]
    c.executemany('INSERT INTO configuracion (clave, valor) VALUES (?,?)', config)

    conn.commit()
    print(f"✅ Base de datos creada exitosamente en: {DB_PATH}")
    print(f"   → {c.execute('SELECT COUNT(*) FROM categorias').fetchone()[0]} categorías")
    print(f"   → {c.execute('SELECT COUNT(*) FROM productos').fetchone()[0]} productos")
    print(f"   → {c.execute('SELECT COUNT(*) FROM reviews').fetchone()[0]} reviews")
    print(f"   → {c.execute('SELECT COUNT(*) FROM recetas').fetchone()[0]} recetas")
    print(f"   → {c.execute('SELECT COUNT(*) FROM timeline').fetchone()[0]} hitos de historia")
    print(f"   → {c.execute('SELECT COUNT(*) FROM ciudades').fetchone()[0]} ciudades")
    print(f"   → {c.execute('SELECT COUNT(*) FROM certificaciones').fetchone()[0]} certificaciones")
    print(f"   → {c.execute('SELECT COUNT(*) FROM hero_slides').fetchone()[0]} slides del hero")


if __name__ == '__main__':
    conn = crear_base_datos()
    insertar_datos(conn)
    conn.close()
