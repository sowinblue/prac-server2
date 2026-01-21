html_main = ''''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>사마죄</title>
        </head>
        <center>
        <body>
        <form method="GET">
                <label for="keyword">검색</label>
                <input type="text" id="keyword" name="keyword" placeholder="초기,과도기,후기 중 선택">
                <button type="submit">등록</button>
            </form>
            <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;

            border: 1px solid #ccc;
            padding: 16px;
            width: 300px;
            margin: 40px auto;
            background-color: #ffffff;
            ">
            <p style="font-size:20px;"><strong>연대기</strong></p>
                <a href="/?keyword=초기" style="display:inline-block; padding:6px 12px; background-color:#eee; border:1px solid #ccc; border-radius:4px; text-decoration:none; color:black;">아기 덕후 시절</a>
                <a href="/?keyword=과도기" style="display:inline-block; padding:6px 12px; background-color:#eee; border:1px solid #ccc; border-radius:4px; text-decoration:none; color:black;">폭풍의 덕후 시절</a>
                <a href="/?keyword=후기" style="display:inline-block; padding:6px 12px; background-color:#eee; border:1px solid #ccc; border-radius:4px; text-decoration:none; color:black;">프로 덕후의 선택</a>
            </div>

            
        </body>
        </center>
        </html>
        '''