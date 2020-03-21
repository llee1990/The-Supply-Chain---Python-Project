"""

"""
from InventoryManagement import OrderProcessor, Order


class UserMenu:

    def __init__(self, path):
        self.path = path

    def process_web_orders(self):
        pass

    def check_inventory(self):
        pass

    def exit_program(self):
        pass


def main():
    a = OrderProcessor("orders.xlsx")
    a.get_orders()
    for order in a.order_list:
        print(order)


if __name__ == "__main__":
    main()