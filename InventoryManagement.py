"""

"""

import pandas


class OrderProcessor:

    factory_map = {
        "Christmas": None,
        "Easter": None,
        "Halloween": None
    }

    def __init__(self, path):
        self.path = path
        self.order_list = []

    def get_orders(self):
        excel_df = pandas.read_excel(self.path)
        for row in excel_df.iterrows():
            self.order_list.append(Order(**row[1]))


class Order:

    def __init__(self, order_number, product_id, item, name, **kwargs):
        self.order_number = order_number
        self.product_id = product_id
        self.item_type = item
        self.name = name
        self.product_details = {}
        for arg, value in kwargs.items():
            if arg != "holiday" and not pandas.isnull(value):
                self.product_details[arg] = value

    def __str__(self):
        separator = "-" * 20
        order_details = f"Order number: {self.order_number}\n" \
                        f"ID: {self.product_id}\n" \
                        f"Item type: {self.item_type}\n" \
                        f"Item name: {self.name}\n" \
                        f"Product details: {self.product_details}"
        return '\n'.join([separator, order_details, separator])


class Store:

    def __init__(self):
        pass