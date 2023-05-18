from django.views.generic import TemplateView 
from blog.models import Post
from work_gallery.models import Work
class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_experiences'] = Work.objects.order_by('-date')[:2]
        context['posts'] = Post.objects.order_by('-last_modified')[:2]
        return context
