import api
import helpers
import data
import allure

class TestLoginCourier:
    """Тесты авторизации курьера."""

    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка: курьер может авторизоваться, возвращается ID')
    def test_login_courier_success(self, courier_for_login):
        """Проверка успешной авторизации курьера."""
        login_data = helpers.create_login_data(courier_for_login)
        login_response = api.UserApi.login_courier(login_data)

        assert login_response.status_code == 200
        assert "id" in login_response.json(), "Ответ должен содержать ID курьера"

    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка: ошибка при неверном логине')
    def test_login_with_invalid_login(self, courier_for_login):
        """Проверка ошибки при неверном логине."""
        login_data = helpers.create_login_data(courier_for_login)
        login_data['login'] = helpers.generate_random_string(10)
        
        login_response = api.UserApi.login_courier(login_data)

        assert login_response.status_code == 404
        assert login_response.json()["message"] == data.LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR

    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка: ошибка при неверном пароле')
    def test_login_with_invalid_password(self, courier_for_login):
        """Проверка ошибки при неверном пароле."""
        login_data = helpers.create_login_data(courier_for_login)
        login_data['password'] = helpers.generate_random_string(10)
        
        login_response = api.UserApi.login_courier(login_data)

        assert login_response.status_code == 404
        assert login_response.json()["message"] == data.LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR

    @allure.title('Авторизация без логина')
    @allure.description('Проверка: ошибка при отсутствии логина')
    def test_login_without_login(self, courier_for_login):
        """Проверка ошибки при пустом логине."""
        login_data = helpers.create_login_data(courier_for_login)
        login_data['login'] = ''
        
        login_response = api.UserApi.login_courier(login_data)

        assert login_response.status_code == 400
        assert login_response.json()["message"] == data.LOGIN_WITH_EMPTY_FIELD_ERROR

    @allure.title('Авторизация без пароля')
    @allure.description('Проверка: ошибка при отсутствии пароля')
    def test_login_without_password(self, courier_for_login):
        """Проверка ошибки при пустом пароле."""
        login_data = helpers.create_login_data(courier_for_login)
        login_data['password'] = ''
        
        login_response = api.UserApi.login_courier(login_data)

        assert login_response.status_code == 400
        assert login_response.json()["message"] == data.LOGIN_WITH_EMPTY_FIELD_ERROR