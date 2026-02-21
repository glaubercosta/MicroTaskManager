from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from database import Base, get_db
from main import app

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

def override_get_db() -> Generator[Session, None, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db() -> Generator[None, None, None]:
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_task() -> None:
    response = client.post("/tasks", json={"title": "Test Task", "status": "todo"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["status"] == "todo"
    assert "id" in data

def test_read_tasks() -> None:
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

def test_filter_tasks() -> None:
    client.post("/tasks", json={"title": "Done Task", "status": "done"})
    client.post("/tasks", json={"title": "Todo Task", "status": "todo"})
    
    response = client.get("/tasks?status=done")
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Done Task"

def test_search_tasks() -> None:
    client.post("/tasks", json={"title": "Apple"})
    client.post("/tasks", json={"title": "Banana"})
    
    response = client.get("/tasks?q=App")
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Apple"

def test_read_task_not_found() -> None:
    response = client.get("/tasks/999")
    assert response.status_code == 404

def test_update_task() -> None:
    create_resp = client.post("/tasks", json={"title": "Old Name"})
    task_id = create_resp.json()["id"]
    
    update_resp = client.put(
        f"/tasks/{task_id}", json={"title": "New Name", "status": "doing"}
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "New Name"
    assert update_resp.json()["status"] == "doing"

def test_delete_task() -> None:
    create_resp = client.post("/tasks", json={"title": "To Delete"})
    task_id = create_resp.json()["id"]
    
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 200
    
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
