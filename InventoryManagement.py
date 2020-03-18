"""

"""

import pandas
import InventoryFactories


class OrderProcessor:

    factory_map = {"Toy":
                   {"Christmas": InventoryFactories.SantaShopFactory,
                    "Easter": InventoryFactories.RobotBunnyFactory,
                    "Halloween": InventoryFactories.RCSpiderFactory},
                   "StuffedAnimal":
                   {"Christmas": InventoryFactories.ReindeerFactory,
                    "Easter": InventoryFactories.EasterBunnyFactory,
                    "Halloween": InventoryFactories.DancingSkeletonFactory},
                   "Candy":
                   {"Christmas": InventoryFactories.CandyCanesFactory,
                    "Easter": InventoryFactories.CremeEggsFactory,
                    "Halloween": InventoryFactories.PCTFactory}}

    def __init__(self, path):
        self.path = path
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
        self.product_details = {}
        self.factory = OrderProcessor.factory_map[item][holiday]
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
        self.inventory = {}

    def receive_order(self, item):
        self.get_item(item)
        for num in range(int(item.product_details['quantity'])):
            self.inventory[item.name].pop()

    def get_item(self, item):
        if item not in self.inventory:
            self.inventory[item.name] = \
                [new_item for new_item in item.factory().create_items()]
        elif len(self.inventory[item]) < int(item.product_details['quantity']):
            for new_item in item.factory().create_items():
                self.inventory[item.name].append(new_item)
