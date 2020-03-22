"""

"""

import pandas

from InventoryFactories import ChristmasItemFactory, EasterItemFactory,\
    HalloweenItemFactory
from InventoryItems import ItemEnum
from InventoryFactories import FactoryEnum
from datetime import date
import time


class OrderProcessor:

    factory_map = {
        FactoryEnum.EASTER: EasterItemFactory,
        FactoryEnum.CHRISTMAS: ChristmasItemFactory,
        FactoryEnum.HALLOWEEN: HalloweenItemFactory
    }

    # factory_map = {"Toy":
    #                {"Christmas": InventoryFactories.SantaShopFactory,
    #                 "Easter": InventoryFactories.RobotBunnyFactory,
    #                 "Halloween": InventoryFactories.RCSpiderFactory},
    #                "StuffedAnimal":
    #                {"Christmas": InventoryFactories.ReindeerFactory,
    #                 "Easter": InventoryFactories.EasterBunnyFactory,
    #                 "Halloween": InventoryFactories.DancingSkeletonFactory},
    #                "Candy":
    #                {"Christmas": InventoryFactories.CandyCanesFactory,
    #                 "Easter": InventoryFactories.CremeEggsFactory,
    #                 "Halloween": InventoryFactories.PCTFactory}}

    def __init__(self, path):
        self.path = path
        self.order_list = []

    def get_orders(self):
        excel_df = pandas.read_excel(self.path)
        for row in excel_df.iterrows():
            self.order_list.append(Order(**row[1]))
            # yield Order(**row[1])

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
        self.product_details = {}
        self.factory = OrderProcessor.factory_map[FactoryEnum(holiday)]
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

    def __init__(self):
        self.inventory = {}

    def receive_order(self, item):
        self.get_item(item)
        for num in range(int(item.product_details['quantity'])):
            self.inventory[item.name].pop()

    def get_item(self, item):
        print(item)
        print(self.inventory)
        if item not in self.inventory:
            new_item = item.factory.create_items(item.item_type, **item)
            print(new_item)

            self.inventory[item.name] = \
                [new_item for new_item in item.factory().create_items()]

        elif len(self.inventory[item]) < int(item.product_details['quantity']):
            for new_item in item.factory().create_items():
                self.inventory[item.name].append(new_item)

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
            date_time = f"{day}-{month}-{year} {hour}:{minute}\n"
            orders = orders.order_history()
            data = title + date_time + orders
            file.write(data)

