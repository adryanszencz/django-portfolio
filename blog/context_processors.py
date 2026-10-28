from blog.models import Post


def recent_posts(request):
    """Últimos posts publicados, usados na sidebar de todas as páginas."""
    return {"recent_posts": Post.objects.filter(published=True)[:5]}
