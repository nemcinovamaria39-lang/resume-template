import http.server
import socketserver
import os

PORT = 8000

web_dir = '.'
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    print(f"Структура файлов:")
    print(f"  index.html")
    print(f"  images/v4_63.png")
    print(f"  css/main.css")
    print("Нажмите Ctrl+C для остановки")
    httpd.serve_forever()