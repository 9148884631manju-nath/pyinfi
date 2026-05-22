from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from http.cookies import SimpleCookie
import uuid
import os
import socketserver
from lib.pyinfi import PYINFI
SESSION_STORAGE = {}
PUBLIC_DIR = os.path.abspath("./res")
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        mses = SESSION_STORAGE
        # Send a 200 OK response
        self.send_response(200)
        parsed_url = urlparse(self.path)
        query_arguments = parse_qs(parsed_url.query)
        pfor = query_arguments.get("code",[""])[0]
        # Set the content type to plain text
        pge = query_arguments.get("page",["home"])
        #print(str(query_arguments))
        fln = pge[0]+'.json' #"web/welcome.json"
        
        match pfor:
         case "api":
              self.send_header("Content-type", "text/json")
              self.end_headers()
              pi = PYINFI(PUBLIC_DIR,self.headers.get("host"),fln,self.path,self.headers,query_arguments,mses)
              html_content = str(pi)
              self.wfile.write(html_content.encode('utf-8'))
         case _:
             self.send_header("Content-type", "text/html")
             self.end_headers()
             pi = PYINFI(PUBLIC_DIR,self.headers.get("host"),fln,self.path,self.headers,query_arguments,mses)
             html_content = str(pi)
             self.wfile.write(html_content.encode('utf-8'))

# Define the server address and port
socketserver.TCPServer.allow_reuse_address = True
server_address = ("127.0.0.1", 8000)

# Create and run the server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server running on http://localhost:8000...")
httpd.serve_forever()