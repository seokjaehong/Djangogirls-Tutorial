from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


# Create your views here.

def post_list(request):
    # 1. 브라우저에서 요청
    # 2. 장고 runserver로 실행중인 서버에 도착
    # 3. runserver는 요청을 장고코드로 전달
    # 4. 장고 코드중 config.urls묘듈이 해당요청을 받음
    # 5. config.urls모듈은 ''(admin/를 제외한 모든요청)을 blog.urls모듈로 전달
    # 6. blog.urls모듈은 받은 요청의 url과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수(view)를 실행
    #   7.1 setting모듈의 Templates 속성 내의 목록에서 blog/post_list.html파일의 내용을 가져옴
    #   7.2 가져온 내용을 처리 (렌더렝, render())하여 리턴
    # 8. 함수의 실행결과(리턴값)을 브라우저로 다시전달
    # Http프로토콜로 텍스트 데이터 응답을 반환

    posts = Post.objects.all()
    # render()함수에 전달할 dict 객체 생성

    context = {
        'posts': posts,
    }

    # return HttpResponse('Post List')
    # return HttpResponse('<html><bodㅇy><h1>Post List</h1><p>post 목록을 보여줄 예정입니다.</p></body></html>')
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # post_detail('localhost:8000/detail')


def post_detail(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)
    '''
    localhost:8000/detail/로 온 요청을 'blog/post_detail.html'을 render한 결과를 리턴 
    :return: 
    '''


def post_add(request):
    # 1. localhost:8000/add로 접근시
    # 이 뷰가 실행되어서 pOST ADD PAGE 라는 문구를 보여주도록 urls 작
    # 2.  HttpResponse가 아니라 blog/post_add.html을 출력
    # post_add.html은 base.html을 확장 title(h2)부분에 'post add' 출력

    if request.method == 'POST':
        # 요청의 method가 post일 때
        title = request.POST['title']
        content = request.POST['content']
        # return HttpResponse(f'{title}:{content}')
        # ORM을 사용해서 title과 content 해당하는 post생성

        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )
        return redirect('post-detail', pk=post.pk)

        #redirect가 아니라 render를 쓰는경우
        # context ={
        #     'post' : post,
        # }
        # return render(request ,'blog/post_detail.html',context)

        #return HttpResponse(f'{post.pk}{post.title}{post.content}')

    else:
        # 요청의 method가 get일때
        pass

        return render(request, 'blog/post_add.html')
    # return HttpResponse('Post add page')
#
# def post_delete(request, pk):
#     if Post.request =='POST' :
#         post = Post.obeject.get(pk=pk)
#         post.delete()
#         return redirect('post-list')

def post_delete(request, pk):
    """
    post_detail의 구조를 참조해서
    pk에 해당하는 post를 삭제하는 view를 구현하고 url과 연결
    pk가 3이면 url은 "/3/delete/"
    이 view는 POST메서드에 대해서만 처리한다 (request.method == 'POST')
    (HTML 템플릿을 사용하지 않음)
    삭제코드
        post = Post.objects.get(pk=pk)
        post.delete()
    삭제 후에는 post-list로 redirect (post_add()를 참조)
    1. post_delete() view함수의 동작을 구현
    2. post_delete view와 연결될 urls를 blog/urls.py에 구현
    3. post_delete로 연결될 URL을 post_detail.html의 form에 작성
        csrf_token사용!
        action의 위치가 요청을 보낼 URL임
    """
    # pk에 해당하는 Post를 삭제
    if request.method =='POST' :
        post = Post.objects.get(pk=pk)
        post.delete()
        # 이후 post-list라는 URL name을 갖는 view로 redirect
        return redirect('post-list')