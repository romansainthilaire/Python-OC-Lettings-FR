import pytest

from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.mark.django_db
def test_list(client):
    profiles = Profile.objects.all()
    path = reverse("profiles:list")
    response = client.get(path)
    content = response.content.decode()
    assert response.status_code == 200
    assert "<title>Profiles</title>" in content
    for profile in profiles:
        assert profile.user.username in content


@pytest.mark.django_db
def test_detail(client):
    user = User.objects.create(
        username="Batman",
        password="mdp123test",
        first_name="Bruce",
        last_name="Wayne",
        email="bruce.wayne@gmail.com"
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city="Gotham City"
    )
    path = reverse("profiles:detail", kwargs={"username": user.username})
    response = client.get(path)
    content = response.content.decode()
    assert response.status_code == 200
    assert f"<title>{user.username}</title>" in content
    assert user.first_name in content
    assert user.last_name in content
    assert user.email in content
    assert profile.favorite_city in content
