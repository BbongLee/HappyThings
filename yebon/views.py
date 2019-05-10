from django.shortcuts import render
from django.utils import timezone
from .models import HappyThings

# request를 넘겨받아 render메서드 호출, yebon/thing_list.html 템플릿을 보여주는 함수
def thing_list(request):
	things = HappyThings.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'yebon/thing_list.html', {'things':things})