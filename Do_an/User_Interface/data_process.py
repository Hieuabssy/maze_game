import json

#Các hàm quản lí tài khoản người dùng
def load_data(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data
def save_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
def check_account(file_name, username, password):
    data = load_data(file_name)
    if len(username) < 6 or len(password) < 6:
        return -1
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return 1
    return 0
def add_user(file_name, username, password):
    data = load_data(file_name)
    data["users"].append({"username": username, "password": password})
    save_data(data, file_name)