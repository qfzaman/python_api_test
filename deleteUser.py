import requests

def delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
    print("DELETE User: Test passed")

delete_user()