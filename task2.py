import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open("orders.json") as f:
        orders_lst = json.load(f)
        orders_lst["orders"].append(order)
    with open("orders.json", "w", encoding="utf-8") as f:
        json.dump(orders_lst, f, indent=4)


if __name__ == '__main__':
    write_order_to_json("some item", 10, 1000, "vasya pupkin", "24.05.2020")
    write_order_to_json("some new item", 120, 10500, "vasya nepupkin", "24.06.2020")
