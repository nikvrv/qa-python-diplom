from app_for_api.client import HttpMethods, HttpClient


class OrdersAPI:

    BASE_ENDPOINT = "/orders"

    def __init__(self, client: HttpClient):
        self.client = client

    def create_order(self, pairs, quantity):
        body = {"stocks": pairs, "quantity": quantity}
        response = self.client.send_request(HttpMethods.POST.value, "/orders", json=body)
        return response

    def get_order_by_id(self, order_id):
        return self.client.send_request(HttpMethods.GET.value, f'/orders/{order_id}')

    def delete_order(self, order_id):
        return self.client.send_request(HttpMethods.DELETE.value, f'/orders/{order_id}')
