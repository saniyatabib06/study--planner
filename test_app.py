from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "subject": "Python",
            "task": "Flask Revision",
            "date": "2026-10-01"
        }
    )

    assert response.status_code == 302


def test_complete_task():
    client = app.test_client()

    response = client.get("/complete/0")

    assert response.status_code == 302