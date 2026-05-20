# ═══════════════════════════════════════════════════════════════
#  GUSTOSSI BOLIVIA · server.py · Servidor Backend con API REST
#  Servidor Python que conecta la base de datos con el frontend
# ═══════════════════════════════════════════════════════════════

import http.server
import json
import sqlite3
import os
import urllib.parse

DB_PATH = os.path.join(os.path.dirname(__file__), 'gustossi.db')
PORT = 8000

def get_db():
    """Conecta a la base de datos SQLite"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Para obtener diccionarios
    return conn

def rows_to_list(rows):
    """Convierte filas SQLite a lista de diccionarios"""
    return [dict(row) for row in rows]


class GustossiHandler(http.server.SimpleHTTPRequestHandler):
    """Servidor HTTP que maneja archivos estáticos + API REST"""

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # ══ RUTAS API ══
        if path.startswith('/api/'):
            self.handle_api(path, parsed.query)
            return

        # ══ ARCHIVOS ESTÁTICOS ══
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/newsletter':
            self.handle_newsletter()
            return

        self.send_error(404)

    def handle_api(self, path, query):
        """Maneja todas las rutas de la API REST"""
        try:
            conn = get_db()
            c = conn.cursor()

            # ── GET /api/categorias ──
            if path == '/api/categorias':
                c.execute('SELECT * FROM categorias ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/productos?cat=slug ──
            elif path == '/api/productos':
                params = urllib.parse.parse_qs(query)
                cat = params.get('cat', [None])[0]
                destacados = params.get('destacados', [None])[0]

                if cat:
                    c.execute('SELECT p.*, c.nombre as categoria_nombre FROM productos p JOIN categorias c ON p.categoria_slug = c.slug WHERE p.categoria_slug = ? ORDER BY p.id', (cat,))
                elif destacados:
                    c.execute('SELECT p.*, c.nombre as categoria_nombre FROM productos p JOIN categorias c ON p.categoria_slug = c.slug WHERE p.destacado = 1 ORDER BY p.id')
                else:
                    c.execute('SELECT p.*, c.nombre as categoria_nombre FROM productos p JOIN categorias c ON p.categoria_slug = c.slug ORDER BY p.id')

                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/producto/:id ──
            elif path.startswith('/api/producto/'):
                prod_id = path.split('/')[-1]
                c.execute('SELECT p.*, c.nombre as categoria_nombre FROM productos p JOIN categorias c ON p.categoria_slug = c.slug WHERE p.id = ?', (prod_id,))
                row = c.fetchone()
                if row:
                    self.send_json(dict(row))
                else:
                    self.send_json({'error': 'Producto no encontrado'}, 404)

            # ── GET /api/reviews ──
            elif path == '/api/reviews':
                c.execute('SELECT * FROM reviews ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/recetas ──
            elif path == '/api/recetas':
                c.execute('SELECT * FROM recetas ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/estadisticas ──
            elif path == '/api/estadisticas':
                c.execute('SELECT * FROM estadisticas ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/hero-slides ──
            elif path == '/api/hero-slides':
                c.execute('SELECT * FROM hero_slides ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/timeline ──
            elif path == '/api/timeline':
                c.execute('SELECT * FROM timeline ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/ciudades ──
            elif path == '/api/ciudades':
                c.execute('SELECT * FROM ciudades ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/certificaciones ──
            elif path == '/api/certificaciones':
                c.execute('SELECT * FROM certificaciones ORDER BY id')
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/configuracion ──
            elif path == '/api/configuracion':
                c.execute('SELECT * FROM configuracion')
                data = {row['clave']: row['valor'] for row in c.fetchall()}
                self.send_json(data)

            # ── GET /api/buscar?q=texto ──
            elif path == '/api/buscar':
                params = urllib.parse.parse_qs(query)
                q = params.get('q', [''])[0]
                c.execute('''SELECT p.*, c.nombre as categoria_nombre 
                            FROM productos p 
                            JOIN categorias c ON p.categoria_slug = c.slug 
                            WHERE p.nombre LIKE ? ORDER BY p.nombre''', (f'%{q}%',))
                data = rows_to_list(c.fetchall())
                self.send_json(data)

            # ── GET /api/stats (resumen general) ──
            elif path == '/api/stats':
                data = {
                    'total_productos': c.execute('SELECT COUNT(*) FROM productos').fetchone()[0],
                    'total_categorias': c.execute('SELECT COUNT(*) FROM categorias').fetchone()[0],
                    'total_reviews': c.execute('SELECT COUNT(*) FROM reviews').fetchone()[0],
                    'total_ciudades': c.execute('SELECT COUNT(*) FROM ciudades').fetchone()[0],
                }
                self.send_json(data)

            else:
                self.send_json({'error': 'Ruta no encontrada'}, 404)

            conn.close()

        except Exception as e:
            self.send_json({'error': str(e)}, 500)

    def handle_newsletter(self):
        """Maneja suscripción al newsletter"""
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            email = data.get('email', '')

            if email:
                conn = get_db()
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS newsletter (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    fecha TEXT DEFAULT CURRENT_TIMESTAMP
                )''')
                try:
                    c.execute('INSERT INTO newsletter (email) VALUES (?)', (email,))
                    conn.commit()
                    self.send_json({'success': True, 'message': '¡Suscripción exitosa!'})
                except sqlite3.IntegrityError:
                    self.send_json({'success': False, 'message': 'Este email ya está suscrito.'})
                conn.close()
            else:
                self.send_json({'success': False, 'message': 'Email requerido.'}, 400)
        except Exception as e:
            self.send_json({'error': str(e)}, 500)

    def send_json(self, data, status=200):
        """Envía respuesta JSON con CORS habilitado"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        """Maneja CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        """Log personalizado"""
        try:
            msg = str(args[0]) if args else ''
            if '/api/' in msg:
                print(f"  API  -> {msg}")
        except:
            pass


def main():
    # Verificar que la base de datos existe
    if not os.path.exists(DB_PATH):
        print("⚠️  Base de datos no encontrada. Creándola...")
        from database import crear_base_datos, insertar_datos
        conn = crear_base_datos()
        insertar_datos(conn)
        conn.close()

    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Iniciar servidor
    server = http.server.HTTPServer(('', PORT), GustossiHandler)
    print()
    print("═" * 55)
    print("  🍪 GUSTOSSI BOLIVIA · Servidor Backend")
    print("═" * 55)
    print(f"  🌐 Sitio web:  http://localhost:{PORT}")
    print(f"  🔌 API REST:   http://localhost:{PORT}/api/")
    print(f"  💾 Base datos: {DB_PATH}")
    print("═" * 55)
    print()
    print("  Endpoints API disponibles:")
    print("  ─────────────────────────────────────")
    print(f"  GET  /api/categorias")
    print(f"  GET  /api/productos")
    print(f"  GET  /api/productos?cat=galleteria")
    print(f"  GET  /api/productos?destacados=1")
    print(f"  GET  /api/producto/1")
    print(f"  GET  /api/reviews")
    print(f"  GET  /api/recetas")
    print(f"  GET  /api/estadisticas")
    print(f"  GET  /api/hero-slides")
    print(f"  GET  /api/timeline")
    print(f"  GET  /api/ciudades")
    print(f"  GET  /api/certificaciones")
    print(f"  GET  /api/configuracion")
    print(f"  GET  /api/buscar?q=galleta")
    print(f"  GET  /api/stats")
    print(f"  POST /api/newsletter")
    print()
    print("  Presiona Ctrl+C para detener el servidor")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  🛑 Servidor detenido.")
        server.server_close()


if __name__ == '__main__':
    main()
