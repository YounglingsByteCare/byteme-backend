import json
import random
import requests

url = "http://127.0.0.1:5000/api/"

userdata_to_create = [
    {
        "user": ("orange@gmail.com", "tomato"),
        "patients": [
            ("Jesse", "Boise", "male", "1602316430082", {
                "street_name": "Fly Street",
                "house_number": 15,
                "city": "Cape Town",
                "country": "South Africa",
                "postal_code": "7530"
            }, "0185249836"),
            ("Adam", "Banderker", "male", "1208032185082", {
                "street_name": "Wimbledon Street",
                "house_number": 4,
                "city": "Cape Town",
                "country": "South Africa",
                "postal_code": "7530"
            }, "0865001215"),
        ],
    },
    {
        "user": ("tomato@gmail.com", "tomato"),
        "patients": [
            ("Kauthar", "Carelse", "female", "0214523248083", {
                "street_name": "Apache Way",
                "house_number": 256,
                "city": "Johannesburg",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0336578746"),
            ("Tinashi", "Muneri", "male", "0331120458082", {
                "street_name": "Alonzo Street",
                "house_number": 88,
                "city": "Pretoria",
                "country": "South Africa",
                "postal_code": "5555"
            }, "0155466897"),
        ],
    }
]
admindata_to_create = [
    {
        "user": ("Oreo", "oreo@gmail.com", "oreo"),
        "admins": [
            ("Orange", "Juice", "male", "8101015800087", {
                "street_name": "Slim Street",
                "house_number": 12,
                "city": "Johannesburg",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0765559187"),
            ("Grape", "Juice", "male", "2001015800085", {
                "street_name": "Alto Avenue",
                "house_number": 1,
                "city": "Port Elizabeth",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0811555598"),
        ],
    },
    {
        "user": ("Chocolate", "chocolate@gmail.com", "choolate"),
        "admins": [
            ("Mango", "Juice", "female", "3605034800089", {
                "street_name": "Apache Way",
                "house_number": 14,
                "city": "Port Elizabeth",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0725555144"),
            ("Apple", "Juice", "male", "3401015800086", {
                "street_name": "Michael Way",
                "house_number": 13,
                "city": "Johannesburg",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0555700552"),
        ],
    },
    {
        "user": ("Cookies", "cookies@gmail.com", "cookies"),
        "admins": [
            ("Pineapple", "Juice", "male", "4909095800080", {
                "street_name": "Aborford Way",
                "house_number": 2,
                "city": "Johannesburg",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0605555625"),
            ("Guava", "Juice", "female", "5910245800086", {
                "street_name": "Cross Port",
                "house_number": 206,
                "city": "Port Elizabeth",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0605559927"),
        ],
    },
    {
        "user": ("Biscuit", "biscuit@gmail.com", "biscuit"),
        "admins": [
            ("Grapefruit", "Juice", "female", "2311034800085", {
                "street_name": "Apache Way",
                "house_number": 256,
                "city": "Johannesburg",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0555519579"),
            ("Lemon", "Juice", "female", "5209114800081", {
                "street_name": "Apache Way",
                "house_number": 256,
                "city": "Johannesburg",
                "country": "South Africa",
                "postal_code": "1234"
            }, "0835553106"),
        ],
    }
]
hospital_data_to_create = [
    ("Groote Schuur Hospital")
]


def create_and_login_user(email_address, password):
    data = {
        "email": email_address,
        "password": password
    }

    # Firstly, create the user.
    signup_url = url + "auth/signup"

    resp = requests.post(signup_url, json=data)

    if (resp.status_code == 200):
        # Secondly, login the user in.
        login_url = url + "auth/login"

        resp = requests.post(login_url, json=data)
        if resp.status_code == 200:
            token = resp.json()["token"]

            return token
        raise Exception(resp.content)
    raise Exception(resp.content)


def create_and_login_adminuser(name, email_address, password):
    data = {
        "name": name,
        "email": email_address,
        "password": password
    }

    # Firstly, create the user.
    signup_url = url + "auth/admin/signup"

    resp = requests.post(signup_url, json=data)

    if (resp.status_code == 200):
        # Secondly, login the user in.

        login_url = url + "auth/admin/login"
        resp = requests.post(login_url, json=data)
        if resp.status_code == 200:
            token = resp.json()["token"]

            return token
        raise Exception(resp.content)
    raise Exception(resp.content)


def create_patient(jwt_token, name, surname, gender, id_number, address, phone):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }
    data = {
        "name": name,
        "surname": surname,
        "gender": gender,
        "id_number": id_number,
        "address": address,
        "phone": phone
    }

    patients_url = url + "patients"

    resp = requests.post(patients_url, json=data, headers=headers)

    if resp.status_code == 200:
        return resp.json()["id"]
    else:
        raise Exception(resp.content)


def create_admin(jwt_token, name, surname, gender, id_number, address, phone_number):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }
    data = {
        "name": name,
        "surname": surname,
        "gender": gender,
        "id_number": id_number,
        "address": address,
        "phone": phone_number,
    }

    patients_url = url + "admins"

    resp = requests.post(patients_url, json=data, headers=headers)

    if resp.status_code == 200:
        return resp.json()["id"]
    else:
        raise Exception(resp.content)


if __name__ == "__main__":
    user_results = {}
    adminuser_results = {}

    admin_user_count = 1
    print('Creating Admin Users')

    for data_item in admindata_to_create:
        print(
            f'Creating Admin User [{admin_user_count}/{len(admindata_to_create)}]')
        user_data = data_item["user"]
        token = create_and_login_adminuser(
            user_data[0], user_data[1], user_data[2]
        )

        adminuser_results[user_data[1]] = token

        for admin in data_item["admins"]:
            print(f'─ {admin[0]}\t\t[ ]')
            admin_id = create_admin(
                token, admin[0], admin[1], admin[2], admin[3], admin[4], admin[5]
            )
            print(f'\r─ {admin[0]}\t\t[✓]')

        print('')
        admin_user_count += 1

    user_count = 0
    print('Creating Users')

    for data_item in userdata_to_create:
        print(f'Creating User [{user_count}/{len(userdata_to_create)}]')
        # Firstly, create the User data.
        user_data = data_item["user"]
        token = create_and_login_user(user_data[0], user_data[1])

        user_results[user_data[0]] = token

        # Next, create the patient data.
        for patient in data_item["patients"]:
            print(f'─ {admin[0]}\t\t[ ]')
            patient_id = create_patient(
                token, patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]
            )
            print(f'\r─ {admin[0]}\t\t[✓]')
