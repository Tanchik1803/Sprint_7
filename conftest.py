import pytest
import helpers

@pytest.fixture
def courier_credentials():
    """Фикстура создаёт и регистрирует курьера, возвращает данные для входа."""
    courier_data = helpers.generate_new_courier_personal_data()
    yield courier_data
    helpers.delete_courier(courier_data)

@pytest.fixture
def courier_for_login():
    """Фикстура создаёт курьера для тестов авторизации."""
    courier_data = helpers.create_courier(register=True)
    yield courier_data
    helpers.delete_courier(courier_data)