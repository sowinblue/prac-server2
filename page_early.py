def html_early(comments):
    return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>초기</title>
            </head>
            <body>
                <a href="/" style="display:inline-block; padding:6px 12px; background-color:#eee; border:1px solid #ccc; border-radius:4px; text-decoration:none; color:black;">처음으로 돌아가기</a>

            <h3>댓글 목록</h3>
                    <div>
                        {comments}
                    </div>

                    <h3>댓글 작성</h3>
                    <form method="POST">
                        <input type="hidden" name="action" value="add">
                        <input type="hidden" name="keyword" value="초기">
                        <input type="text" name="text" placeholder="댓글 작성">
                        <button type="submit">작성</button>
                    </form>

                </body>
                </html>
            '''


def render_comments(comment_list):
    html = ""
    for c in comment_list:
        html += f'''
        <p>
            {c["text"]}
            <form method="POST" style="display:inline;">
                <input type="hidden" name="action" value="delete">
                <input type="hidden" name="id" value="{c["id"]}">
                <input type="hidden" name="keyword" value="초기">
                <button type="submit">삭제</button>
            </form>
        </p>
        '''
    return html
