import json

from tests.v1.constants import ROUTE


def test_create_job(client):
    data = {
        "title": "Python backend developer",
        "company": "hydroscience",
        "company_url": "www.hydroscience.com",
        "location": "Russia, Moscow",
        "description": "python",
        "date_posted": "2022-06-28"
        }
    response = client.post(f"{ROUTE}/jobs/create-job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "hydroscience"
    assert response.json()["description"] == "python"


def test_read_job(client):
    data = {
        "title": "Python backend developer",
        "company": "hydroscience",
        "company_url": "www.hydroscience.com",
        "location": "Russia, Moscow",
        "description": "python",
        "date_posted": "2022-06-28"
    }
    client.post(f"{ROUTE}/jobs/create-job/", json.dumps(data))

    response = client.get(f"{ROUTE}/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "Python backend developer"
