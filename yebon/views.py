from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import HappyThings
from .forms import HappyThingForm

# request를 넘겨받아 render메서드 호출, yebon/thing_list.html 템플릿을 보여주는 함수
def thing_list(request):
	things = HappyThings.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'yebon/thing_list.html', {'things':things})

def thing_detail(request, pk):
    thing = get_object_or_404(HappyThings, pk=pk)
    return render(request, 'yebon/thing_detail.html', {'thing': thing})

def thing_new(request):
    if request.method == "POST":
        form = HappyThingForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.reporter = request.user
            thing.published_date = timezone.now()
            thing.save()
            return redirect('post_detail', pk=thing.pk)
    else:
        form = HappyThingForm()
    return render(request, 'yebon/thing_edit.html', {'form': form})