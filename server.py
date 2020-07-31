import http.server
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Check JSON there http://127.0.0.1/last.json')
    httpd.serve_forever()