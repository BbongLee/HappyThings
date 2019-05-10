from django.shortcuts import render

# request를 넘겨받아 render메서드 호출, yebon/thing_list.html 템플릿을 보여주는 함수
def thing_list(request):
    return render(request, 'yebon/thing_list.html', {})