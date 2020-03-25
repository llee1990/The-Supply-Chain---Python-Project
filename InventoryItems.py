"""
"""

from abc import ABC
from enum import Enum
from ErrorHandling import InvalidDataError


class ItemEnum(Enum):
    TOY = "Toy"
    STUFFED_ANIMAL = "StuffedAnimal"
    CANDY = "Candy"


class Item(ABC):

    def __init__(self, name, description, product_id, quantity, order_number):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.quantity = quantity
        self.error_message = ''
        self.order_number = order_number


class Toy(Item):

    def __init__(self, min_age, has_batteries, **kwargs):
        super().__init__(**kwargs)
        if min_age < 1:
            self.error_message += '"min_age" must be greater than "1". '
        self.min_age = min_age
        self.has_batteries = has_batteries


class SantaWorkshop(Toy):

    def __init__(self, dimensions, num_rooms, **kwargs):
        super().__init__(**kwargs)
        if self.has_batteries.upper() != "N":
            self.error_message += '"has_batteries" must be "N". '
        if num_rooms < 1:
            self.error_message += '"num_rooms" must be greater than "1". '
        self.dimensions = dimensions
        self.num_rooms = num_rooms
        if self.error_message != '':
            # print(self.error_message)
            raise InvalidDataError(self.error_message)

    def __str__(self):

        return f"{self.name}, {self.description}, {self.product_id}, " \
               f"{self.quantity}, {self.min_age}, {self.has_batteries}, " \
               f"{self.dimensions}, {self.num_rooms}"


class RCSpider(Toy):

    def __init__(self, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        super().__init__(**kwargs)
        if self.has_batteries.upper() != "Y":
            self.error_message += '"has_batteries" must be "Y". '
        if speed < 1:
            self.error_message += '"speed" must be greater than "1". '
        if jump_height < 1:
            self.error_message += '"jump_height" must be greater than "1". '
        if has_glow.upper() != "N" and has_glow.upper() != "Y":
            self.error_message += '"has_glow" must be set to "Y" or "N". '
        if spider_type.title() != "Tarantula" and \
                spider_type.title() != "Wolf Spider":
            self.error_message += '"spider_type" must be either "Tarantula" ' \
                                  'or "Wolf Spider". '
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.spider_type = spider_type
        if self.error_message != '':
            raise InvalidDataError


class RobotBunny(Toy):

    def __init__(self, num_sound, colour, **kwargs):
        super().__init__(**kwargs)
        if num_sound < 1:
            self.error_message += '"num_sound" must be greater than "1" '

        if colour.title() != "Orange" and colour.title() != "Blue" and \
                colour.title() != "Pink":
            self.error_message += '"colour" must be either "Orange", "Blue", '\
                                  'or "Pink". '
        self.num_sound = num_sound
        self.color = colour
        if self.error_message != '':
            raise InvalidDataError


class StuffedAnimal(Item):

    def __init__(self, stuffing, size, fabric, **kwargs):
        super().__init__(**kwargs)
        if size.upper() != "S" and size.upper() != "M" and size.upper() != "L":
            self.error_message += '"size" must be either "S", "M" ' \
                                  'or "L". '
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric


class DancingSkeletons(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        super().__init__(**kwargs)
        if self.stuffing.title() != "Polyester Fibrefill":
            self.error_message += '"stuffing" must be "Polyester Fibrefill". '
        if self.fabric.title() != "Acrylic":
            self.error_message += '"fabric" must be "Acrylic". '
        self.has_glow = has_glow
        if self.error_message != '':
            raise InvalidDataError


class Reindeer(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        super().__init__(**kwargs)
        if self.stuffing.title() != "Wool":
            self.error_message += '"stuffing" must be "Wool". '
        if self.fabric.title() != "Cotton":
            self.error_message += '"fabric" must be "Cotton". '
        self.has_glow = has_glow
        if self.error_message != '':
            raise InvalidDataError


class EasterBunny(StuffedAnimal):

    def __init__(self, colour, **kwargs):
        super().__init__(**kwargs)
        if self.stuffing.title() != "Polyester Fibrefill":
            self.error_message += '"stuffing" must be "Polyester Fibrefill". '
        if self.fabric.title() != "Linen":
            self.error_message += '"fabric" must be "Linen". '
        self.colour = colour
        if self.error_message != '':
            self.quantity = 0
            raise InvalidDataError(self.error_message)


class Candy(Item):

    def __init__(self, has_lactose, has_nuts, **kwargs):
        super().__init__(**kwargs)
        self.has_lactose = has_lactose
        self.has_nuts = has_nuts


class PumpkinCaramelToffee(Candy):

    def __init__(self, variety, **kwargs):
        super().__init__(**kwargs)
        if self.has_lactose.upper() != "Y":
            self.error_message += '"has_lactose" must be "Y". '
        if self.has_nuts.upper() != "Y":
            self.error_message += '"has_nuts" must be "Y". '
        if variety.title() != "Sea Salt" and variety.title() != "Regular":
            self.error_message += '"variety" must be "Sea Salt" or "Regular". '
        self.variety = variety
        if self.error_message != '':
            raise InvalidDataError


class CandyCane(Candy):

    def __init__(self, colour, **kwargs):
        super().__init__(**kwargs)
        if self.has_lactose.upper() != "N":
            self.error_message += '"has_lactose" must be "N". '
        if self.has_nuts.upper() != "N":
            self.error_message += '"has_nuts" must be "N". '
        if colour.title() != "Red" and colour.title() != "Green":
            self.error_message += '"colour" must be "Red" or "Green". '
        self.colour = colour
        if self.error_message != '':
            raise InvalidDataError


class CremeEggs(Candy):

    def __init__(self, pack_size, **kwargs):
        super().__init__(**kwargs)
        if self.has_lactose.upper() != "Y":
            self.error_message += '"has_lactose" must be "Y". '
        if self.has_nuts.upper() != "Y":
            self.error_message += '"has_nuts" must be "Y". '
        if pack_size < 5:
            self.error_message += '"has_nuts" must be greater than "5". '
        self.pack_size = pack_size
        if self.error_message != '':
            raise InvalidDataError


def main():
    args = {'name': 'Santas Workshop - Essentials Edition', 'product_id':
        'C1230T',
     'quantity': 10,
     'description': 'The most sought after christmas present! Get yours today!',
     'has_batteries': 'N', 'min_age': 5.0, 'dimensions': '50,90',
     'num_rooms': 4.0}
    santa_workshop = SantaWorkshop(**args)
    print(hash(santa_workshop))

    args = {'name': 'Easter Bunny with Top Hat', 'product_id': 'E2446E', 'quantity': 2, 'description': 'The easter bunny is now ready for all the tea parties you can host with his Jacket and Top Hat!', 'colour': 'Grey', 'stuffing': 'Polyester Fibrefill', 'size': 'M', 'fabric': 'Linen'}
    easter_bunny = EasterBunny(**args)
    hash(easter_bunny)

    # args = {'name': 'Mr. Hoppers', 'product_id': 'E4835T', 'quantity': 10, 'description': 'Learn the alphabet with the interactive toys for infants.', 'has_batteries': 'Y', 'min_age': 1.0, 'num_sound': 30.0, 'colour': 'Orange'}
    # easter_toy = RobotBunny(**args)
    # print(easter_toy)
    #
    # args = {'name': 'Howling Wolf Spider', 'product_id': 'H2345T', 'quantity': 4, 'description': 'The howling wolf spider jumps higher and faster than the terrifying tarantula. This is the toy for the ultimate prank.', 'has_batteries': 'Y', 'min_age': 9.0, 'speed': 15.0, 'jump_height': 5.0, 'has_glow': 'N', 'spider_type': 'Wolf Spider'}
    # rc_spider = RCSpider(**args)
    # print(rc_spider)
    #
    # args = {'name': 'Skello the Tap Dancer', 'product_id': 'H4443S', 'quantity': 1, 'description': 'Decorate your home with Skello the Tap Dancer. Oh the whimsical horror!', 'has_glow': 'Y', 'stuffing': 'Polyester Fibrefill', 'size': 'L', 'fabric': 'Acrylic'}
    # halloween_stuffed_animals = DancingSkeletons(**args)
    # print(halloween_stuffed_animals)


if __name__ == "__main__":
    main()