# from http.server import HTTPServer, BaseHTTPRequestHandler
#
# from io import BytesIO
#
# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b'Hello, world! GET')
#
#     def do_POST(self):
#         content_length = int(self.headers['Content-Length'])
#         body = self.rfile.read(content_length)
#         self.send_response(200)
#         self.end_headers()
#         response = BytesIO()
#         #response.write(b'This is a POST request. ')
#         response.write(b'Received: ')
#         response.write(body)
#         # self.wfile.write(response.getvalue())
#         print(response.getvalue())
#         #self.wfile.write(b'Hello, world! POST')
#
#
#
# httpd = HTTPServer(('', 1337), SimpleHTTPRequestHandler)
# httpd.serve_forever()

from bazooka import bazooka