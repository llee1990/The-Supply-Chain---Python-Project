"""

"""

import pandas
import time
from datetime import date
from InventoryFactories import ChristmasItemFactory, EasterItemFactory,\
    HalloweenItemFactory, FactoryEnum


class OrderProcessor:
    factory_map = {
        FactoryEnum.EASTER: EasterItemFactory,
        FactoryEnum.CHRISTMAS: ChristmasItemFactory,
        FactoryEnum.HALLOWEEN: HalloweenItemFactory
    }

    def __init__(self, path):
        self.path = path
        self.order_list = []

    def add_orders(self, order):
        self.order_list.append(order)

    def clear_order_list(self):
        self.order_list = []

    def get_orders(self):
        excel_df = pandas.read_excel(self.path)
        for row in excel_df.iterrows():
            yield Order(**row[1])

    def order_history(self):
        history = ""
        for order in self.order_list:
            history += f"Order {order.order_number}, Item {order.item_type}, "\
                f"Product ID {order.product_id}, Name \"{order.name}\", " \
                f"Quantity {order.product_details['quantity']}\n"
        return history


class Order:

    def __init__(self, order_number, product_id, item, name, holiday,
                 **kwargs):
        self.order_number = order_number
        self.product_id = product_id
        self.item_type = item
        self.name = name
        self.holiday = holiday
        self.factory = OrderProcessor.factory_map[FactoryEnum(holiday)]()
        # Product details to instantiate Item objects
        self.product_details = {'name': name, 'product_id': product_id}
        for arg, value in kwargs.items():
            if arg != "holiday" and not pandas.isnull(value):
                self.product_details[arg] = value

    def __str__(self):
        separator = "-" * 20
        order_details = f"Order number: {self.order_number}\n" \
                        f"ID: {self.product_id}\n" \
                        f"Item type: {self.item_type}\n" \
                        f"Item name: {self.name}\n\n" \
                        f">>Product details<<"
        product_details = ""
        for key, value in self.product_details.items():
            product_details += f"{key}: {value}\n"
        return '\n'.join([separator, order_details,
                          product_details, separator])


class Store:

    DEFAULT_ORDER_SIZE = 100

    def __init__(self):
        self.inventory = {}
        self.order_history = []

    def receive_order(self, order):
        self.process_item(order)

    def update_inventory_item(self, order, quantity):
        while quantity != 0:
            del self.inventory[order][-1]
            quantity -= 1

    def process_item(self, order):
        factory = order.factory
        order_name = order.name
        new_item = factory.create_items(item_type=order.item_type,
                                        **order.product_details)
        order_amount = int(order.product_details['quantity'])

        # item does not exist in inventory
        if order_name not in self.inventory:
            self.inventory[order_name] = [new_item for _
                                          in range(self.DEFAULT_ORDER_SIZE)]

        # item quantity is less than the order amount
        elif len(self.inventory[order_name]) < order_amount:
            curr_quantity = int(len(self.inventory[order]))
            self.inventory[order_name] = [new_item for _
                                          in range(self.DEFAULT_ORDER_SIZE
                                                   + curr_quantity)]

        self.update_inventory_item(order, order_amount)
        # TODO: Add method to update order_history

    def get_order_history(self):
        # TODO: implement
        history = ""
        for order in self.order_history:
            history += order.__str__()
        return history

    @staticmethod
    def create_report(orders):
        local_time = time.localtime()
        day = date.today().day
        if day < 10:
            day = '0' + str(day)
        month = date.today().month
        if month < 10:
            month = '0' + str(month)
        year = str(date.today().year)[0:2]
        hour = time.strftime('%H', local_time)
        minute = time.strftime('%M', local_time)
        file_name = f"DTR_{day}{month}{year}_{hour}{minute}"
        with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:
            title = 'HOLIDAY STORE - DAILY TRANSACTION REPORT(DRT)\n'
            date_time = f"{day}-{month}-{year} {hour}:{minute}\n\n"
            orders = orders.get_order_history()
            data = title + date_time + orders
            file.write(data)
