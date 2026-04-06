import api
import allure

class TestOrderList:
    """Тесты получения списка заказов."""

    @allure.title('Получение списка заказов')
    @allure.description('Проверка: в ответе возвращается список заказов')
    def test_get_orders_list_success(self):
        """Проверка успешного получения списка заказов."""
        response = api.OrderApi.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json(), "Ответ должен содержать список заказов"