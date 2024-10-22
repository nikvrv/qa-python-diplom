from random import choices, randint

import faker


def get_sign_up_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password


def get_stock_name() -> list[str]:
    stocks = ("EUR", "USD", "GEL", "AED", "RUB")
    return choices(stocks, k=2)


def get_random_int(start: int, stop: int) -> int:
    return randint(999, 9999)


def create_order_data() -> dict[str, int | str]:
    return {"stocks": "".join(get_stock_name()), "quantity": randint(0, 100)}
