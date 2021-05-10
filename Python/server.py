import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''Handle HTTP requsests by returning a fixed 'page','''
    
    # Page to send back.
    Page = '''\

<html>
<title>Welcome</title>
<body>
  <h1>&emsp; Hello, web and Welcome to W Zone</h1>
</body>
</html>
'''
    
    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)
        
        
        #---------------------------------
if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.server_forever()
          
