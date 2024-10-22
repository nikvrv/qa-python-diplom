import allure

from app_for_api.orders_api import OrdersAPI
from helpers import get_stock_name


class TestAPIOrders:

    @allure.title("Create order")
    def test_create_order(self, http_client):
        orders_api = OrdersAPI(http_client)
        pair = "".join(get_stock_name())
        response = orders_api.create_order(pair, 10)

        assert response.status_code == 201
        assert response.json()['quantity'] == 10
        assert response.json()['stocks'] == pair
        orders_api.delete_order(response.json()['id'])

    @allure.title("Get order by id")
    def test_get_order_by_id(self, http_client, create_order, delete_order):
        order_id = create_order['id']
        orders_api = OrdersAPI(http_client)
        response = orders_api.get_order_by_id(order_id)

        assert response.status_code == 200
        assert response.json()['stocks'] == create_order['stocks']
        assert response.json()['quantity'] == create_order['quantity']
