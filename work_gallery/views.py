from django.shortcuts import render, get_object_or_404, redirect
from .models import Work
from .forms import WorkForm
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


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

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class EditWork(UpdateView):
    model = Work
    form_class = WorkForm
    template_name = 'work_gallery/edit_work.html'
    success_url = reverse_lazy('work_index')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class DeleteWork(DeleteView):
    model = Work
    success_url = reverse_lazy('work_index')
    template_name = 'delete_work.html'
