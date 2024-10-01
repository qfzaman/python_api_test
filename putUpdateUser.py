import requests

def put_update_user():
    jobChange = {
        "name": "fahmid",
        "job": "automation"
    }
    response = requests.put("https://reqres.in/api/users/2", json=jobChange)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert data["name"] == "fahmid", f"Expected name 'fahmid', but got {data['name']}"
    assert data["job"] == "automation", f"Expected job 'automation', but got {data['job']}"
    print("PUT Update User: Test passed")

put_update_user()