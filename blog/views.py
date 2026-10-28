from django.http import HttpResponse
from django.views import generic

from blog.models import Post


def home(request):
    return HttpResponse("Hello World")


class PostList(generic.ListView):
    queryset = Post.objects.filter(published=True)
    template_name = "index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetail(generic.DetailView):
    queryset = Post.objects.filter(published=True)
    template_name = "post_detail.html"
