import pytest
from django.urls import reverse


def test_home_retorna_hello_world(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert response.content.decode() == "Hello World"


def test_url_da_home(client):
    assert reverse("home") == "/home/"


@pytest.mark.django_db
def test_rota_inexistente_da_404(client):
    response = client.get("/qualquer/coisa/")

    assert response.status_code == 404
