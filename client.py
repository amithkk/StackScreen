import BaseHTTPServer

class StackAuthServer(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('You requested: "%s"' % self.path)

httpd = BaseHTTPServer.HTTPServer(('localhost', 9000), StackAuthServer)
httpd.serve_forever()
