from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogForm
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


# list all posts
def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_index.html', context)

# show a post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

# create a post only accessible by admin
@user_passes_test(lambda u: u.is_superuser)
def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False) # Create a Form instance, but don't save it yet
            form.author = request.user # Set the author field manually
            form.save() # Now save the Form (Post object) instance to the database
            return redirect('blog_index')
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create_post.html', context)

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class EditPost(UpdateView):
    model = Post
    form_class = BlogForm
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('blog_index')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_index')
    template_name = 'delete_post.html'
