import string
import requests
import api
import random

def generate_random_string(length):
    """Генерирует случайную строку заданной длины из строчных букв."""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_new_courier_personal_data(empty_field=None):
    """Генерирует новые данные курьера с возможностью пустого поля."""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    if empty_field is not None:
        courier_data[empty_field] = ''
    return courier_data

def create_login_data(courier_data):
    """Создаёт данные для входа на основе данных курьера."""
    return {
        'login': courier_data['login'],
        'password': courier_data['password']
    }

def get_courier_id(courier_data):
    """Получает ID курьера через авторизацию."""
    login_data = create_login_data(courier_data)
    login_response = api.login_courier(login_data)
    return login_response.json().get('id')

def create_courier(register=False):
    """Создаёт данные курьера, при необходимости регистрирует в API."""
    courier_data = generate_new_courier_personal_data()
    if register:
        api.create_courier(courier_data)
    return courier_data

def delete_courier(courier_data):
    """Удаляет курьера по ID после авторизации."""
    try:
        courier_id = get_courier_id(courier_data)
        if courier_id:
            api.delete_courier(courier_id)
    except requests.exceptions.RequestException as error:
        print(f"Ошибка удаления курьера: {error}")