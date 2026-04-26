import requests


def test_create_task(base_url):
    payload = {"title": "Learn pytest"}
    response = requests.post(f"{base_url}/tasks", json=payload, timeout=5)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["completed"] is False
    assert isinstance(body["id"], int)


def test_get_missing_task_returns_404(base_url):
    response = requests.get(f"{base_url}/tasks/999999", timeout=5)
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_complete_task(base_url):
    created = requests.post(f"{base_url}/tasks", json={"title": "Complete me"}, timeout=5)
    task_id = created.json()["id"]

    completed = requests.patch(f"{base_url}/tasks/{task_id}/complete", timeout=5)
    assert completed.status_code == 200
    assert completed.json()["completed"] is True

