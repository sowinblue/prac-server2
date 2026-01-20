from http.server import HTTPServer, BaseHTTPRequestHandler

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content.type', 'text/html; charset=utf-8')
        self.end_headers()

        html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>음악 보따리</title>
        </head>
        <body>
            <h1> 좋아하는 장르를 적어봐! </h1>
        <form methon="GET">
            <label for="genre"> 장르 </label>
            <input type="text" id="genre placeholder="장르 입력">
            <button>등록</button>
        </form>
        </body>
        </html>
        '''

        self.wfile.write(html.encode('utf-8'))

host = 'localhost'
port = 8000

serve = HTTPServer((host,port),myhandler)

print(f"서버가 시작되었습니다. http://{host}:{port}")
print("종료 : Ctrl + C")


try:
    serve.serve_forever()
except KeyboardInterrupt:
    print("서버 종료")
    serve.server_close
