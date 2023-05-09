from django.shortcuts import render, get_object_or_404, redirect
from .models import Work
from .forms import WorkForm
from django.contrib.auth.decorators import user_passes_test


# list all work experiences
def work_index(request):
    works = Work.objects.all()
    context = {
        'works': works
    }
    return render(request, 'work_gallery/work_index.html', context)

# show a work experience
def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    context = {
        'work': work
    }
    return render(request, 'work_gallery/work_detail.html', context)

# create a work experience only accessible by admin
@user_passes_test(lambda u: u.is_superuser)
def create_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('work_index')
    else:
        form = WorkForm()
    context = {
        'form': form
    }
    return render(request, 'work_gallery/create_work.html', context)
