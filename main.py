from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs 
from page_main import html_main
from page_early import html_early
from page_mid import html_mid
from page_late import html_late

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
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
            # 🔹 3) 입력이 없으면 처음 페이지 표시
        else:
            html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>검색 결과 없음</title>
            </head>
            <body>
                <h1>검색 결과가 없습니다: {keyword}</h1>
                <a href="/">처음으로 돌아가기</a>
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
