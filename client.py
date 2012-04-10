import BaseHTTPServer
from urllib import quote_plus

class StackAuthServer(BaseHTTPServer.BaseHTTPRequestHandler):
    
    app_id  = 237
    app_key = 'rLH9jCghgsD38YzwSl06PQ(('
    
    def write_response(self, content, status_code=200, additional_headers={}):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        for key, value in additional_headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(content)
    
    def write_redirect(self, location):
        self.write_response('Redirecting you to <a href="%s">$s</a>...' % location,
                            302, { 'Location': location })
    
    def do_GET(self):
        
        # If the user is requesting the index, then send a redirect
        # to the OAuth authorization page to begin the auth process.
        if self.path == '/':
            self.write_redirect('https://stackexchange.com/oauth/dialog?client_id=%s&scope=read_inbox,no_expiry&redirect_uri=%s' %
                                (self.app_id, quote_plus('http://localhost:9000/auth')))
        elif self.path == '/auth':
            self.write_response('Your application was authorized.')
        else:
            self.write_response('<h1>404 File Not Found</h1><p>The path "%s" does not exist on this server.</p>' % self.path, 404)

httpd = BaseHTTPServer.HTTPServer(('localhost', 9000), StackAuthServer)
httpd.serve_forever()