from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_task():
    resp = client.post("/tasks", json={"title": "write tests", "completed": False})
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == 1
    assert data["title"] == "write tests"
    assert data["completed"] is False


def test_list_tasks():
    resp = client.get("/tasks")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 1
