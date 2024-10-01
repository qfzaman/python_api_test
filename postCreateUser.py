import requests

def post_create_user():
    newUser = {
        "name": "fahmid",
        "job": "qa"
    }
    response = requests.post("https://reqres.in/api/users", json=newUser)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    data = response.json()
    assert data["name"] == "fahmid", f"Expected name 'fahmid', but got {data['name']}"
    assert data["job"] == "qa", f"Expected job 'qa', but got {data['job']}"
    print("POST Create User: Test passed")

post_create_user()