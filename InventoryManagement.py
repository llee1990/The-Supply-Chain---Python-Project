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

    def __init__(self):
        self._path = ""

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def prompt_file_input(self):
        while True:
            path = input("Enter an excel file to process orders: ")
            if ".xlsx" not in path:
                print("Error: File must be a type of .xlsx extension.\n")
            else:
                break
        self.path = path

    def get_orders(self):
        self.prompt_file_input()
        excel_df = pandas.read_excel(self.path)
        for row in excel_df.iterrows():
            yield Order(**row[1])


class Order:

    def __init__(self, order_number, product_id, item, name, holiday,
                 **kwargs):
        self._order_number = order_number
        self._product_id = product_id
        self._item_type = item
        self._name = name
        self._holiday = holiday
        self._factory = OrderProcessor.factory_map[FactoryEnum(holiday)]()
        self._product_details = {'name': name, 'product_id': product_id,
                                 'order_number': order_number}
        for arg, value in kwargs.items():
            if arg != "holiday" and not pandas.isnull(value):
                self._product_details[arg] = value

    @property
    def order_number(self):
        return self._order_number

    @property
    def product_id(self):
        return self._product_id

    @property
    def item_type(self):
        return self._item_type

    @property
    def name(self):
        return self._name

    @property
    def holiday(self):
        return self._holiday

    @property
    def factory(self):
        return self._factory

    @property
    def product_details(self):
        return self._product_details

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

    def __update_inventory_item(self, order, quantity):
        while quantity != 0:
            self.inventory[order.name].pop()
            quantity -= 1

    def process_item(self, order):
        factory = order.factory
        name = order.name
        order_amount = int(order.product_details['quantity'])

        try:    # processing an order
            new_item = factory.create_items(item_type=order.item_type,
                                            **order.product_details)

        except InvalidDataError as ide:  # encountered error while processing
            order_error_message = str(ide)
            self.__append_order_history(order, order_error_message)

        else:   # no error in processing the order

            # item does not exist in inventory
            if name not in self.inventory:
                self.inventory[name] = [new_item for _
                                        in
                                        range(self.DEFAULT_ORDER_SIZE)]

            # item quantity is less than the order amount
            elif len(self.inventory[name]) < order_amount:
                curr_quantity = int(len(self.inventory[order]))
                self.inventory[name] = [new_item for _
                                        in range(self.DEFAULT_ORDER_SIZE
                                                 + curr_quantity)]

            self.__update_inventory_item(order, order_amount)
            self.__append_order_history(order, new_item.error_message)

    def __append_order_history(self, order, message):
        self.order_history.append([order, message])

    def __get_order_history(self):
        order_history = ""
        for order in self.order_history:
            if order[1] == "":      # order was processed successfully
                order_history += f"{order[0].get_order_history()}\n"
            else:
                order_history += f"Order {order[0].order_number}, " \
                                 f"{order[1]}\n\n"
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
            all_orders = self.__get_order_history()
            data = title + date_time + all_orders
            file.write(data)
