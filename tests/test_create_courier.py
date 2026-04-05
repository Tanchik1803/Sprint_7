import pytest
import api
import helpers
import data
import allure

class TestCreateCourier:
    """Тесты создания курьера."""

    @allure.title('Создание курьера')
    @allure.description('Проверка: курьера можно создать, код 201, ответ {"ok": true}')
    def test_create_courier_success(self, courier_credentials):
        """Проверка успешного создания курьера."""
        response = api.create_courier(courier_credentials)

        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        assert response.json() == {"ok": True}


    @allure.title('Создание двух курьеров с одинаковыми данными')
    @allure.description('Проверка: нельзя создать двух курьеров с одинаковым логином')
    def test_create_duplicate_courier_returns_409(self):
        """Проверка ошибки при создании дубликата курьера."""
        courier_data = helpers.generate_new_courier_personal_data()
        
        response_first = api.create_courier(courier_data)
        assert response_first.status_code == 201

        response_second = api.create_courier(courier_data)
        assert response_second.status_code == 409
        assert response_second.json()['message'] == data.CREATE_COURIER_DUPLICATION_ERROR

    @allure.title('Создание курьера с пустым обязательным полем')
    @allure.description('Проверка: нельзя создать курьера без логина или пароля')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_create_courier_with_empty_required_field(self, empty_field):
        """Проверка ошибки при пустом обязательном поле."""
        courier_data = helpers.generate_new_courier_personal_data(empty_field=empty_field)
        create_response = api.create_courier(courier_data)

        assert create_response.status_code == 400
        assert create_response.json()["message"] == data.CREATE_COURIER_EMPTY_FIELD_ERROR

    @allure.title('Создание курьера с существующим логином')
    @allure.description('Проверка: нельзя создать курьера с логином, который уже зарегистрирован')
    def test_create_courier_with_existing_login(self, courier_for_login):
        """Проверка ошибки при создании курьера с существующим логином."""
        new_data = helpers.generate_new_courier_personal_data()
        new_data['login'] = courier_for_login['login']
        
        create_response = api.create_courier(new_data)

        assert create_response.status_code == 409
        assert create_response.json()["message"] == data.CREATE_COURIER_DUPLICATION_ERROR