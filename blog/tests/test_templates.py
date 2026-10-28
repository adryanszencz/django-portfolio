import pytest
from django.urls import reverse

from blog.factories import PostFactory


@pytest.mark.django_db
def test_index_usa_base_e_sidebar(client):
    response = client.get(reverse("index"))

    templates = [t.name for t in response.templates]
    assert response.status_code == 200
    assert {"index.html", "base.html", "sidebar.html"} <= set(templates)


@pytest.mark.django_db
def test_index_mostra_so_posts_publicados(client):
    PostFactory(title="Post publicado")
    PostFactory(title="Post rascunho", published=False)

    html = client.get(reverse("index")).content.decode()

    assert "Post publicado" in html
    assert "Post rascunho" not in html


@pytest.mark.django_db
def test_detalhe_do_post(client):
    post = PostFactory(title="Detalhe", content="Conteúdo completo do post")

    response = client.get(post.get_absolute_url())

    assert response.status_code == 200
    assert "post_detail.html" in [t.name for t in response.templates]
    assert "Conteúdo completo do post" in response.content.decode()


@pytest.mark.django_db
def test_rascunho_nao_abre_no_detalhe(client):
    post = PostFactory(published=False)

    assert client.get(post.get_absolute_url()).status_code == 404


@pytest.mark.django_db
def test_sidebar_lista_posts_recentes(client):
    PostFactory(title="Recente na sidebar")

    response = client.get(reverse("index"))

    assert "Recente na sidebar" in [p.title for p in response.context["recent_posts"]]
