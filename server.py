from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from src.data.Event import Event
from src.application.create_event import create_event
from src.data.User import User
from src.application.create_user import create_user


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with open('src/user/HTML/create_event.html', 'rb') as file: 
            self.wfile.write(file.read()) 

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_dict = dict(parse.parse_qs(post_data.decode('utf-8')))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('src/user/HTML/create_event.html', 'rb') as file: 
            self.wfile.write(file.read()) 

        print(f"Posted data: {post_dict}") # do wathever with data
        user = create_user('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(1660521522845)
        event = create_event(user,post_dict)
    
        print (event)
        

if __name__ == "__main__":        
    webServer = HTTPServer(("localhost", 8080), Server)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()