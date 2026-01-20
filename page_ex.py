def no_keyword(keyword):
    return  f'''
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>검색 결과 없음</title>
                </head>
                <body>
                    <h1>검색 결과가 없습니다:{keyword}</h1>
                    <a href="/" style="display:inline-block; padding:6px 12px; background-color:#eee; border:1px solid #ccc; border-radius:4px; text-decoration:none; color:black;">처음으로 돌아가기</a>
                </body>
                </html>
                '''
