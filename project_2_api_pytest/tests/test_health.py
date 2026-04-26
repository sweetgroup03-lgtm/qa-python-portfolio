import requests


def test_health(base_url):
    response = requests.get(f"{base_url}/health", timeout=5)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

