import pytest

from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_list(client):
    lettings = Letting.objects.all()
    path = reverse("lettings:list")
    response = client.get(path)
    content = response.content.decode()
    assert response.status_code == 200
    assert "<title>Lettings</title>" in content
    for letting in lettings:
        assert letting.title in content


@pytest.mark.django_db
def test_detail(client):
    address = Address.objects.create(
        number=11,
        street="W 53rd St",
        city="New York",
        state="NY",
        zip_code=10019,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(
        title="Museum of Modern Art",
        address=address
    )
    path = reverse("lettings:detail", kwargs={"letting_id": letting.pk})
    response = client.get(path)
    content = response.content.decode()
    assert response.status_code == 200
    assert f"<title>{letting.title}</title>" in content
    assert str(address.number) in content
    assert address.street in content
    assert address.city in content
    assert address.state in content
    assert str(address.zip_code) in content
    assert address.country_iso_code in content
