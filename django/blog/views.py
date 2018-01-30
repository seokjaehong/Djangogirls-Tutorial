from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def post_list(reuqest):
    # 1. 브라우저에서 요청
    # 2. 장고 runserver로 실행중인 서버에 도착
    # 3. runserver는 요청을 장고코드로 전달
    # 4. 장고 코드중 config.urls묘듈이 해당요청을 받음
    # 5. config.urls모듈은 ''(admin/를 제외한 모든요청)을 blog.urls모듈로 전달
    # 6. blog.urls모듈은 받은 요청의 url과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수(view)를 실행
    # 8. 함수의 실행결과(리턴값)을 브라우저로 다시전달
    # Http프로토콜로 텍스트 데이터 응답을 반환
    # return HttpResponse('Post List')
    return HttpResponse('<html><body><h1>Post List</h1><p>post 목록을 보여줄 예정입니다.</p></body></html>')

