from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Define the directory where the data will be stored
DATA_DIR = "data"

class DummyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the output file exists
        if not os.path.exists(OUTPUT_FILE):
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'File not found\n')
            return

        # Read the contents of the output file
        with open(OUTPUT_FILE, 'rb') as f:
            file_content = f.read()

        # Send the file content in the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(file_content)


    def do_POST(self):
        # Extract the content length from the request headers
        content_length = int(self.headers['Content-Length'])
        # Read the POST data from the request body
        post_data = self.rfile.read(content_length)

        # Ensure the data directory exists
        os.makedirs(DATA_DIR, exist_ok=True)
        # Write the POST data to a file in the data directory
        with open(os.path.join(DATA_DIR, 'output.txt'), 'wb') as f:
            f.write(post_data)

        # Send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Data received and written to file\n')

def run_server(server_class=HTTPServer, handler_class=DummyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting dummy server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
