"""
This module contains classes that are involved with inventory management
"""

import pandas
import time
from datetime import date
from InventoryFactories import ChristmasItemFactory, EasterItemFactory,\
    HalloweenItemFactory, FactoryEnum
from ErrorHandling import InvalidDataError


class OrderProcessor:
    """The OrderProcessor class processes new orders entered into the system"""

    # Maps factories to the corresponding holidays
    factory_map = {
        FactoryEnum.EASTER: EasterItemFactory,
        FactoryEnum.CHRISTMAS: ChristmasItemFactory,
        FactoryEnum.HALLOWEEN: HalloweenItemFactory
    }

    def __init__(self):
        """
        Initializes a OrderProcessor object
        """
        self._path = ""

    @property
    def path(self):
        """
        Setter for self._path
        :return: A String containing the path of the input file
        """
        return self._path

    def prompt_file_input(self):
        """
        Prompts user for the input file path
        """
        while True:
            path = input("Enter an excel file to process orders: ")
            if ".xlsx" not in path:
                print("Error: File must be a type of .xlsx extension.\n")
            else:
                break
        self._path = path

    def get_orders(self):
        """
        Creates orders from each row in the input Excel file
        :return: Yields Order objects
        """
        self.prompt_file_input()
        excel_df = pandas.read_excel(self.path)
        for row in excel_df.iterrows():
            yield Order(**row[1])


class Order:
    """Creates Order objects that contain values used to create new items"""

    def __init__(self, order_number, product_id, item, name, holiday,
                 **kwargs):
        """
        Initializes a Order object

        :param order_number: an int
        :param product_id: A String
        :param item: A String
        :param name: A String
        :param holiday: A String
        :param kwargs: Keyword arguments that contain product details
        """
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
        """
        Getter for self._order_number
        :return: A String, the order number
        """
        return self._order_number

    @property
    def product_id(self):
        """
        Getter for self._product_id
        :return: A String, the product ID
        """
        return self._product_id

    @property
    def item_type(self):
        """
        Getter for self._item_type
        :return: A String, the type of item
        """
        return self._item_type

    @property
    def name(self):
        """
        Getter for self._name
        :return: A String, the item name
        """
        return self._name

    @property
    def holiday(self):
        """
        Getter for self._holiday
        :return: A String, the item holiday
        """
        return self._holiday

    @property
    def factory(self):
        """
        Getter for self._factory
        :return: A SeasonalItemFactory, the type of factory used to create the
        item
        """
        return self._factory

    @property
    def product_details(self):
        """
        Getter for self._product_details
        :return: A dict, contains product details
        """
        return self._product_details

    def get_order_history(self):
        """
        Gets order history in the required format
        :return: A String containing an order's record
        """
        history = ""
        history += f"Order {self.order_number}, Item {self.item_type}, "\
                   f"Product ID {self.product_id}, Name \"{self.name}\", " \
                   f"Quantity {self.product_details['quantity']}\n"
        return history


class Store:
    """
    The Store class contains the store inventory and all order histories
    """

    # The default order size to create when there is not enough items in stock
    # in the inventory
    DEFAULT_ORDER_SIZE = 100

    def __init__(self):
        """
        Initializes a Store object
        """
        self.inventory = {}
        self.order_history = []

    def __update_inventory_item(self, order, quantity):
        """
        Updates inventory amount based on order quantity

        :param order: an Order
        :param quantity: an int
        """
        while quantity != 0:
            self.inventory[order.name].pop()
            quantity -= 1

    def __check_inventory(self, order, new_item, amount):
        """
        Checks inventory to see if new items need to be created and added
        to inventory

        :param order: an Order
        :param new_item: an Item
        :param amount: an Int
        """
        # item does not exist in inventory
        name = order.name
        if name not in self.inventory:
            self.inventory[name] = [new_item for _
                                    in
                                    range(self.DEFAULT_ORDER_SIZE)]

        # item quantity is less than the order amount
        elif len(self.inventory[name]) < amount:
            curr_quantity = int(len(self.inventory[order]))
            self.inventory[name] = [new_item for _
                                    in range(self.DEFAULT_ORDER_SIZE
                                             + curr_quantity)]

    def process_item(self, order):
        """
        Processes orders - create new items is needed, adds to inventory
        and updates the order history

        :param order: an Order
        """
        factory = order.factory
        order_amount = int(order.product_details['quantity'])

        try:    # processing an order
            new_item = factory.create_item(item_type=order.item_type,
                                           **order.product_details)

        except InvalidDataError as ide:  # encountered error while processing
            order_error_message = str(ide)
            self.__append_order_history(order, order_error_message)

        else:   # no error in processing the order
            self.__check_inventory(order, new_item, order_amount)
            self.__update_inventory_item(order, order_amount)
            self.__append_order_history(order, new_item.error_message)

    def __append_order_history(self, order, message):
        """
        Adds order record to order history list

        :param order: an Order
        :param message: a String
        """
        self.order_history.append((order, message))

    def __get_order_history(self):
        """
        Gets all the order records in a List and return as a String

        :return: A String containing details of the entire order history
        """
        order_history = ""
        for order in self.order_history:
            if order[1] == "":      # order was processed successfully
                order_history += f"{order[0].get_order_history()}\n"
            else:
                order_history += f"Order {order[0].order_number}, " \
                                 f"{order[1]}\n\n"
        return order_history

    def create_report(self):
        """
        Creates and exports a order history report in a .txt file that follows
        the formatting listed in the requirements document.
        """
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
