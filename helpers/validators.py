
def valid_price(price):
    if 0 < price:
        return price
    raise ValueError("[ERROR]The invalid price!!!")


def valid_rate(price):
    if 0 < price <= 10:
        return price
    raise ValueError("[ERROR]The invalid rating!!!")
