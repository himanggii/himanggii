from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def start_file_server_vulnerable(port=8000):
    with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving files on port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    start_file_server_vulnerable()
