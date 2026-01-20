html_main = '''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>사랑연대기</title>
            </head>
            <center>
            <body>
                <h1>연대기</h1>
                <ul style="display: flex; flex-direction: column; align-items: center; padding-left: 0;">
                    <li style="list-style: disc; margin-left: 20px;"><a href="/?keyword=초기">아기 덕후 시절</a></li>
                    <li style="list-style: disc; margin-left: 20px;"><a href="/?keyword=과도기">폭풍의 덕후 시절</a></li>
                    <li style="list-style: disc; margin-left: 20px;"><a href="/?keyword=후기">프로 덕후의 선택</a></li>
                </ul>

                <form method="GET">
                    <label for="keyword">검색</label>
                    <input type="text" id="keyword" name="keyword" placeholder="초기,과도기,후기 중 선택">
                    <button type="submit">등록</button>
                </form>
            </body>
            </center>
            </html>
            '''