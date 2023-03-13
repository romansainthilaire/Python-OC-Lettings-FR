from django.urls import reverse


def test_index(client):
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in content
