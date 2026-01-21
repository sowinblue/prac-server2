from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs 
from page_main import html_main
from page_early import html_early
from page_mid import html_mid
from page_late import html_late
from page_ex import no_keyword

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/static/"):
            file_path = "." + self.path  # 예: ./static/mid.png
            try:
                with open(file_path, "rb") as f:
                    self.send_response(200)
                    if file_path.endswith(".png"):
                        self.send_header("Content-type", "image/png")
                    elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                        self.send_header("Content-type", "image/jpeg")
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
            return
        
        
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        keyword = params.get("keyword", [""])[0]  # 입력값 없으면 빈 문자열


        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()


        if not keyword:
            html = html_main
        elif  keyword == "초기":
            html = html_early
        elif keyword == "과도기":
            html = html_mid
        elif keyword =="후기":
            html = html_late
        else:
            html = no_keyword(keyword)
        
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
