import pytest
import api
import data
import allure

class TestCreateOrder:
    """Тесты создания заказа."""

    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description('Проверка: заказ можно создать с BLACK, GREY, обоими цветами или без цвета')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ], ids=['black', 'grey', 'both', 'no_color'])
    def test_create_order_with_color_variations(self, color):
        """Проверка создания заказа с разными вариантами цвета."""
        order_info = data.order_data(color)
        response = api.OrderApi.create_order(order_info)

        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        assert "track" in response.json()