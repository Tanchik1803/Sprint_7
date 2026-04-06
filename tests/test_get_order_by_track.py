import api
import data
import allure

class TestGetOrderByTrack:
    """Тесты получения заказа по номеру."""

    @allure.title('Успешное получение заказа по номеру')
    @allure.description('Проверка: успешный запрос возвращает объект с заказом')
    def test_get_order_by_track_success(self):
        """Проверка успешного получения заказа по треку."""
        order_data = data.order_data(['BLACK'])
        create_response = api.OrderApi.create_order(order_data)
        order_track = create_response.json().get('track')
        
        response = api.OrderApi.get_order_by_track(order_track)

        assert response.status_code == 200
        assert "order" in response.json() or "track" in response.json()

    @allure.title('Получение заказа без номера')
    @allure.description('Проверка: ошибка при отсутствии номера заказа')
    def test_get_order_without_track(self):
        """Проверка ошибки при отсутствии номера заказа."""
        get_order_response = api.OrderApi.get_order_by_track('')

        assert get_order_response.status_code == 400
        assert get_order_response.json()["message"] == data.MISSING_ORDER_ID_ERROR

    @allure.title('Получение несуществующего заказа')
    @allure.description('Проверка: ошибка при несуществующем номере заказа')
    def test_get_nonexistent_order(self):
        """Проверка ошибки при несуществующем треке."""
        get_order_response = api.OrderApi.get_order_by_track('555555')

        assert get_order_response.status_code == 404
        assert get_order_response.json()["message"] == data.MISSING_TRACK_ERROR