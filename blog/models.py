from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Post do portfólio/blog."""

    title = models.CharField("título", max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="autor",
    )
    content = models.TextField("conteúdo")
    published = models.BooleanField("publicado", default=False)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["-created_at", "-id"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
