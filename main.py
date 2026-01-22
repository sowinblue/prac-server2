from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime
from page_main import html_main
from page_early import html_early
from page_mid import html_mid
from page_late import html_late
from page_ex import no_keyword

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class myhandler(BaseHTTPRequestHandler):
    comments = []  # [{"id":1, "text":"댓글내용"}, ...]
    next_id = 1

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        comment_text = params.get('comment', [''])[0]
        edit_id = params.get('edit_id', [''])[0]


        if comment_text:  # 내용이 있으면 처리
            if edit_id:  # 수정 모드
                for c in type(self).comments:
                    if str(c["id"]) == edit_id:
                        c["text"] = comment_text # 그 자리에서 수정
                        c["edited_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            else:  # 새 댓글 추가
                type(self).comments.append({
                    "id": type(self).next_id,
                    "text": comment_text,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # 생성 시간
                    "edited_at": None

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
        
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        keyword = params.get("keyword", [""])[0]
        print("keyword:", keyword)  # 입력값 없으면 빈 문자열
        delete_id = params.get("delete", [""])[0]
        edit_id = params.get('edit', [''])[0]
        
        
        
        comment_html = ""
        edit_text = ""
        if edit_id:
            # 수정할 댓글 찾아서 input에 미리 채움
            for c in type(self).comments:
                if str(c["id"]) == edit_id:
                    edit_text = c["text"]


        if delete_id:
            for c in type(self).comments:
                if str(c["id"]) == delete_id:
            # 삭제 표시로 바꿈
                    c["text"] = f'<span style="color:red; text-decoration: line-through;">삭제된 댓글입니다</span>'


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
                    <div style="width: 100%; text-align: center;">
                    <ul style="list-style:none; padding:0; margin:0;">
            """

            
            comment_html += '<div style="width:100%; text-align:center;"><ul style="list-style:none; padding-left:0; margin:0;">'
            
            
            # 댓글 렌더링
            for c in type(self).comments:
                comment_html += "<li>"
                comment_html += c['text']  # 삭제 표시 포함
                

                # 삭제되지 않은 댓글만 삭제 버튼 표시
                if "삭제된 댓글입니다" not in c['text']:
                    time_str = c['edited_at'] if c['edited_at'] else c['created_at']
                    edited_label = " (수정됨)" if c['edited_at'] else ""
                    comment_html += f"<span style='float:right; font-size:0.7em; color:#888;'>{time_str}{edited_label}</span>"
                    comment_html += f' <a href="/?delete={c["id"]}">삭제</a>'
                    comment_html += f' <a href="/?edit={c["id"]}">수정</a>'
                comment_html += "</li>"


            comment_html += f"""
                        </ul>
                    </div>
                    <form method="POST" style="width:100%; text-align:center; margin-top:15px;">
                        <input name="comment" value="{edit_text}" style="width:70%; padding: 5px;" placeholder="댓글을 입력하세요">
                        {('<input type="hidden" name="edit_id" value="'+edit_id+'">') if edit_id else ''}
                        <button style="padding: 5px 10px;">{'수정' if edit_id else '등록'}</button>
                    </form>
                </div>
            """
                
            # 닫기 + 입력폼
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
