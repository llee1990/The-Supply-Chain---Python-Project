"""

"""
from InventoryManagement import OrderProcessor, Store
import time
import texttable


class UserMenu:

    def __init__(self, path):
        self.order_processor = OrderProcessor(path)
        self.store = Store()

    def process_web_orders(self):
        orders = self.order_processor.get_orders()
        for order in orders:
            self.order_processor.add_orders(order)
        for order in self.order_processor.order_list:
            self.store.receive_order(order)
        print(f"\nSuccessfully processed "
              f"{len(self.order_processor.order_list)} "
              f"orders...\n")
        self.order_processor.clear_order_list()

    def check_inventory(self):
        table = texttable.Texttable()
        table.set_deco(table.HEADER)
        table.add_rows([["Name",    "Stock", "Quantity"]])
        table.set_cols_align(["l", "r", "r"])
        table.set_cols_dtype(['t',  # text
                              't',  # float (decimal)
                              'i',  # float (exponent)
                              ])
        for key, value in self.store.inventory.items():
            row = [key]
            if len(value) == 0:
                row.append("Out of Stock")
            elif 0 < len(value) < 3:
                row.append("Very Low")
            elif 3 < len(value) < 10:
                row.append("Low")
            else:
                row.append("In stock")
            row.append(len(value))
            table.add_row(row)
        print(f"\n{table.draw()}\n")

    def exit_program(self):
        print("Printing report...")
        self.store.create_report()
        time.sleep(0.5)
        print("Exiting program...")
        time.sleep(0.5)
        exit()


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