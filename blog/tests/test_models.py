import pytest
from django.db import IntegrityError

from blog.factories import PostFactory, UserFactory
from blog.models import Post


@pytest.mark.django_db
def test_cria_post():
    post = PostFactory(title="Meu primeiro post")

    assert Post.objects.count() == 1
    assert str(post) == "Meu primeiro post"


@pytest.mark.django_db
def test_post_comeca_como_rascunho():
    post = Post.objects.create(title="Rascunho", slug="rascunho", author=UserFactory(), content="Texto")

    assert post.published is False
    assert post.created_at is not None


@pytest.mark.django_db
def test_slug_e_unico():
    PostFactory(slug="repetido")

    with pytest.raises(IntegrityError):
        PostFactory(slug="repetido")


@pytest.mark.django_db
def test_posts_mais_recentes_primeiro():
    antigo = PostFactory()
    novo = PostFactory()

    assert list(Post.objects.all()) == [novo, antigo]


@pytest.mark.django_db
def test_autor_tem_os_seus_posts():
    autor = UserFactory()
    PostFactory.create_batch(3, author=autor)

    assert autor.posts.count() == 3
