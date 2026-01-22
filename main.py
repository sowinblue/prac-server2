from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs 
from page_main import html_main
from page_early import html_early
from page_mid import html_mid
from page_late import html_late
from page_ex import no_keyword

class myhandler(BaseHTTPRequestHandler):
    comments = []  # [{"id":1, "text":"댓글내용"}, ...]
    next_id = 1

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        comment_text = params.get('comment', [''])[0]

        if comment_text:
            # 댓글 추가
            type(self).comments.append({
                "id": type(self).next_id,
                "text": comment_text
            })
            type(self).next_id += 1

        # 작성 후 메인페이지로 리다이렉트
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()



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
        
        deleted_message_html = ""
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        keyword = params.get("keyword", [""])[0]  # 입력값 없으면 빈 문자열
        delete_id = params.get("delete", [""])[0]
        

        
        if delete_id:
            type(self).comments = [
                c for c in type(self).comments if str(c["id"]) != delete_id
            ]

            deleted_message_html = f"""
                <div style="color:red; text-decoration: line-through; text-align:center; margin: 8px 0;">
                    삭제된 댓글입니다
                </div>
                """

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
        
        
        #메인 페이지만
        # 메인 페이지만 댓글 렌더링
        if not keyword:

            comment_html = """
                <hr>
                <div style="
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 8px;

                    padding: 16px;
                    width: 300px;
                    margin: 40px auto;
                    background-color: #ffffff;
                ">
                    <h3>댓글</h3>
                    <ul style="list-style:none; padding:0;">
            """

            # 댓글 리스트
            for c in type(self).comments:
                comment_html += f"""
                <li>
                    {c['text']}
                    <a href="/?delete={c['id']}">삭제</a>
                </li>
                """

        comment_html += "</ul>"
        # 삭제 메시지 붙이기
        comment_html += deleted_message_html

                
            # 닫기 + 입력폼
        comment_html += """
                </ul>
                <form method="POST">
                    <input name="comment">
                    <button>등록</button>
                </form>
            </div>
        """

        html += comment_html


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
