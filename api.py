import requests
import urls
import allure

@allure.step('Отправляем запрос на создание курьера')
def create_courier(data):
    return requests.post(urls.CREATE_COURIER, json=data)

@allure.step('Отправляем запрос на удаление курьера')
def delete_courier(courier_id):
    return requests.delete(f"{urls.DELETE_COURIER}{courier_id}")

@allure.step('Отправляем запрос авторизации курьера')
def login_courier(data):
    return requests.post(urls.LOGIN_COURIER, json=data)

@allure.step('Отправляем запрос на создание заказа')
def create_order(data):
    return requests.post(urls.CREATE_ORDER, json=data)

@allure.step('Отправляем запрос на получение списка заказов')
def get_orders():
    return requests.get(urls.GET_ORDERS)

@allure.step('Отправляем запрос на получение заказа по номеру')
def get_order_by_track(track):
    return requests.get(f"{urls.GET_ORDER_BY_TRACK}?t={track}")

@allure.step('Отправляем запрос на принятие заказа курьером')
def accept_order(courier_id, order_id):
    return requests.patch(f"{urls.ACCEPT_ORDER}?c={courier_id}&o={order_id}") 