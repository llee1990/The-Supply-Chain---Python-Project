"""
"""

import pandas
import time
from datetime import date
from InventoryFactories import ChristmasItemFactory, EasterItemFactory,\
    HalloweenItemFactory, FactoryEnum
from ErrorHandling import InvalidDataError


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
        self.product_details = {'name': name, 'product_id': product_id,
                                'order_number': order_number}
        for arg, value in kwargs.items():
            if arg != "holiday" and not pandas.isnull(value):
                self.product_details[arg] = value

    def get_order_history(self):
        history = ""
        history += f"Order {self.order_number}, Item {self.item_type}, "\
                f"Product ID {self.product_id}, Name \"{self.name}\", " \
                f"Quantity {self.product_details['quantity']}\n"
        return history

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
            self.inventory[order.name].pop()
            quantity -= 1

    def process_item(self, order):
        factory = order.factory
        order_name = order.name
        order_amount = int(order.product_details['quantity'])
        try:
            # try processing an order
            new_item = factory.create_items(item_type=order.item_type,
                                            **order.product_details)

        except InvalidDataError as ide:
            # encountered error while processing
            print("\n ERROR")
            order_error_message = str(ide)
            print(order_error_message)
            self.update_order_history(order, order_error_message)

        else:
            # no error in processing the order
            print("\n NO ERROR")
            # item does not exist in inventory
            if order_name not in self.inventory:
                self.inventory[order_name] = [new_item for _
                                              in
                                              range(self.DEFAULT_ORDER_SIZE)]

            # item quantity is less than the order amount
            elif len(self.inventory[order_name]) < order_amount:
                curr_quantity = int(len(self.inventory[order]))
                self.inventory[order_name] = [new_item for _
                                              in range(self.DEFAULT_ORDER_SIZE
                                                       + curr_quantity)]

            self.update_inventory_item(order, order_amount)
            print(new_item)
            print(new_item.error_message)
            self.update_order_history(order, new_item.error_message)

    def update_order_history(self, order, message):
        self.order_history.append([order, message])

    # def append_order_history(self, order, item):
    #     if item.error_message == "":
    #         self.order_history.append(order.get_order_history())
    #     else:
    #         self.order_history.append(f"Order {item.order_number}, "
    #                                   f"{item.error_message})")

    def get_order_history(self):
        order_history = ""
        for order in self.order_history:
            if order[1] == "":      # order was processed successfully
                order_history += f"{order[0].get_order_history()}\n"
            else:
                order_history += f"Order {order[0].order_number}, " \
                                 f"{order[1]}\n\n"
        print(order_history)
        return order_history

    def create_report(self):
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
            all_orders = self.get_order_history()
            data = title + date_time + all_orders
            file.write(data)


def main():

    a = OrderProcessor("orders.xlsx")
    c = Store()
    for order in a.get_orders():
        c.receive_order(order)


if __name__ == "__main__":
    main()