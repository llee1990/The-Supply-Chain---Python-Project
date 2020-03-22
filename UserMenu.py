"""

"""
from InventoryManagement import OrderProcessor, Store
import time


class UserMenu:

    def __init__(self, path):
        self.order_processor = OrderProcessor(path)
        self.store = Store()

    def process_web_orders(self):
        for order in self.order_processor.get_orders():
            self.store.receive_order(order)

    def check_inventory(self):
        for key, value in self.store.inventory.items():
            if len(value) == 0:
                print(f"{key}: Out of Stock")
            if 0 < len(value) < 3:
                print(f"{key}: Very Low")
            if 3 < len(value) < 10:
                print(f"{key}: Low")
            if len(value) > 10:
                print(f"{key}: In stock")

    def exit_program(self):
        print("Printing report...")
        self.store.create_report(self.order_processor)
        time.sleep(0.5)
        print("Exiting program...")
        time.sleep(0.5)


def execute_program():
    path = "orders.xlsx"
    menu = UserMenu(path)
    menu_options = {
        1: menu.process_web_orders,
        2: menu.check_inventory,
        3: menu.exit_program
    }
    program_running = True
    while program_running:
        print("-" * 15)
        print("What would you like to do today?")
        print("-" * 15)
        print("1. Process web orders")
        print("2. Check inventory")
        print("3. Exit program")
        print("-" * 15)
        user_input = 0
        while user_input < 1 or user_input > 3:
            try:
                user_input = int(input("Select an option:"))
            except ValueError:
                continue
        menu_options[user_input]()
        if user_input == 3:
            break


def main():
    execute_program()


if __name__ == "__main__":
    main()