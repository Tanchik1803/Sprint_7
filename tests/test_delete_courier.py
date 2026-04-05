import api
import helpers
import data
import allure

class TestDeleteCourier:
    """Тесты удаления курьера."""

    @allure.title('Успешное удаление курьера')
    @allure.description('Проверка: успешный запрос возвращает {"ok": true}')
    def test_delete_courier_success(self, courier_for_login):
        """Проверка успешного удаления курьера."""
        courier_id = helpers.get_courier_id(courier_for_login)
        response = api.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удаление курьера без ID')
    @allure.description('Проверка: ошибка 400 при отсутствии ID курьера')
    def test_delete_courier_without_id(self):
        """Проверка ошибки при удалении без ID."""
        delete_response = api.delete_courier('')

        assert delete_response.status_code == 400
        assert delete_response.json()["message"] == data.MISSING_COURIER_ID_ERROR
    
    @allure.title('Удаление несуществующего курьера')
    @allure.description('Проверка: ошибка при ID несуществующего курьера')
    def test_delete_nonexistent_courier(self):
        """Проверка ошибки при удалении несуществующего курьера."""
        delete_response = api.delete_courier(999999)

        assert delete_response.status_code == 404
        assert delete_response.json()["message"] == data.COURIER_NOT_FOUND_ERROR