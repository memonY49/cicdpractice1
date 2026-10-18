from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "FastAPI CI/CD is working!"
    }


def test_student_pass():
    response = client.post(
        "/result",
        json={"name": "Ali", "marks": 75}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Pass"


def test_student_fail():
    response = client.post(
        "/result",
        json={"name": "Sara", "marks": 35}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Fail"
