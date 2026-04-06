CREATE_COURIER_DUPLICATION_ERROR = "Этот логин уже используется. Попробуйте другой."
CREATE_COURIER_EMPTY_FIELD_ERROR = "Недостаточно данных для создания учетной записи"
LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR = "Учетная запись не найдена"
LOGIN_WITH_EMPTY_FIELD_ERROR = "Недостаточно данных для входа"
COURIER_NOT_FOUND_ERROR = "Курьера с таким id нет."
MISSING_COURIER_ID_ERROR = "Недостаточно данных для удаления курьера"
MISSING_ORDER_ID_ERROR = "Недостаточно данных для поиска"
MISSING_TRACK_ERROR = "Заказ не найден"

def order_data(color=''):
    data = {
        "firstName": "Ирина",
        "lastName": "Петрова",
        "address": "г.Москва",
        "metroStation": "Сокольники",
        "phone": "+7 912 345 6789",
        "rentTime": 2,
        "deliveryDate": "2026-04-03",
        "comment": "Жду",
    }
    if color:
        data["color"] = color

    return data