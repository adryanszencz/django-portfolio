import pytest
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.factories import PostFactory
from blog.models import Post


def test_post_registrado_no_admin():
    assert admin.site.is_registered(Post)


@pytest.fixture
def admin_client_logado(client):
    get_user_model().objects.create_superuser("admin", "admin@email.com", "senha-de-teste-123")
    client.login(username="admin", password="senha-de-teste-123")
    return client


@pytest.mark.django_db
def test_lista_de_posts_no_admin(admin_client_logado):
    PostFactory(title="Post no admin")

    response = admin_client_logado.get(reverse("admin:blog_post_changelist"))

    assert response.status_code == 200
    assert "Post no admin" in response.content.decode()


@pytest.mark.django_db
def test_cria_post_pelo_admin(admin_client_logado):
    autor = get_user_model().objects.get(username="admin")

    response = admin_client_logado.post(
        reverse("admin:blog_post_add"),
        {"title": "Criado no admin", "slug": "criado-no-admin", "author": autor.id, "content": "Texto", "published": "on"},
    )

    assert response.status_code == 302
    assert Post.objects.filter(slug="criado-no-admin", published=True).exists()
