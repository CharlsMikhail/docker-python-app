from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hola Mundo cambiando\n")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8097)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Servidor corriendo en puerto 8097...")
    httpd.serve_forever()

