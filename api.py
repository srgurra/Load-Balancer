from http.server import BaseHTTPRequestHandler, HTTPServer

import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status= 200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_GET(self):
        if self.path =="/hello":
            self._set_headers()
            response = {"message": "Hello, world!"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            response= {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        if self.path == "/echo":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            self._set_headers()
            response = {"you_sent":data}
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            response = {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode())
def run(server_class= HTTPServer, handler_class = SimpleAPIHandler, port = 8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running at http://localhost:{port}/")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
