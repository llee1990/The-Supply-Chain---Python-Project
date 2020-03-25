"""

"""
from InventoryManagement import OrderProcessor, Store
import time
import texttable


class UserMenu:

    BORDER_LENGTH = 35

    def __init__(self):
        self.order_processor = OrderProcessor()
        self.store = Store()
        UserMenu.load_intro()

    @staticmethod
    def load_intro():
        """
        generated from http://patorjk.com/
        """
        str = "\n" \
              "       🎃 🎃 🎃    🐰    🐰    🎅🎅🎅🎅 \n" \
              "          🎃       🐰    🐰    🎅     \n" \
              "          🎃       🐰🐰🐰🐰    🎅🎅🎅 \n" \
              "          🎃       🐰    🐰    🎅    \n" \
              "          🎃       🐰    🐰    🎅🎅🎅🎅\n" \
              "\n\n" \
              "   🐰🐰🐰🐰    🎅    🎅      🎁🎁🎁     🎃🎃🎃🎃 \n" \
              "   🐰          🎅    🎅     🎁    🎁    🎃    🎃 \n" \
              "    🐰🐰🐰      🎅 🎅 🎅    🎁     🎁    🎃🎃🎃 \n" \
              "         🐰     🎅    🎅    🎁    🎁     🎃      \n" \
              "   🐰🐰🐰🐰      🎅    🎅     🎁🎁🎁      🎃       \n"
        print(str)

    def process_web_orders(self):
        print("\n\n1. Process web orders")
        print("-" * self.BORDER_LENGTH)
        try:
            orders = self.order_processor.get_orders()
            order_count = 0
            for order in orders:
                self.store.process_item(order)
                order_count += 1
        except FileNotFoundError as fne:
            print("Error: " + str(fne).split("]")[1].strip())
        else:
            print(f"\nSuccessfully processed {order_count} orders...")
        print("-" * self.BORDER_LENGTH + "\n\n")

    def check_inventory(self):
        print("\n\n2. CheckInventory")
        print("-" * self.BORDER_LENGTH)
        if not self.store.inventory:
            print("No items in inventory...")
            print("-" * self.BORDER_LENGTH + "\n\n")
            return
        table = texttable.Texttable()
        table.set_deco(table.HEADER)
        table.add_rows([["Item Name",    "Stock", "Quantity"]])
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
        print("-" * self.BORDER_LENGTH + "\n\n")

    def exit_program(self):
        print("\n\n3. Exit Program")
        print("-" * self.BORDER_LENGTH)
        print("Printing report...\n")
        self.store.create_report()
        time.sleep(0.5)
        print("Exiting program...")
        time.sleep(0.5)
        print("-" * self.BORDER_LENGTH + "\n\n")
        exit()

    def execute_program(self):
        menu_options = {
            1: self.process_web_orders,
            2: self.check_inventory,
            3: self.exit_program
        }
        program_running = True
        while program_running:
            print("-" * self.BORDER_LENGTH)
            print("What would you like to do today?")
            print("-" * self.BORDER_LENGTH)
            print("1. Process web orders")
            print("2. Check inventory")
            print("3. Exit program")
            print("-" * self.BORDER_LENGTH)
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
    program = UserMenu()
    program.execute_program()


if __name__ == "__main__":
    main()
