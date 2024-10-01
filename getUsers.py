import requests

def get_users_list():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert "data" in data, "Response does not contain 'data' field"
    print("GET List Users: Test passed")

get_users_list()