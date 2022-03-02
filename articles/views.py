from django.shortcuts import render

# Create your views here.
#django의 모든 view함수들은 기본적으로 request인자를 첫번째 인자로 받는다.
def index(request): 
    #request라는 곳에는 무엇이 들어있을까?
    #단, django에서 templates 파일들은 모두 app/templates 폴더에 들어있다.
    #render 함수의 2번째 인자, 파일명은 정확하게는 파일경로입니다.
    #templates가 생략된 파일경로이다.
    print(dir(request))
    return render(request, 'index.html') 