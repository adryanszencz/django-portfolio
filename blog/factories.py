import factory
from django.contrib.auth import get_user_model

from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"usuario{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@email.com")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=5, locale="pt_BR")
    slug = factory.Sequence(lambda n: f"post-{n}")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("paragraph", nb_sentences=5, locale="pt_BR")
    published = True
