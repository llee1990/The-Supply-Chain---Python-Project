"""

"""

from abc import ABC, abstractmethod
from enum import Enum
from ErrorHandling import InvalidDataError


class ItemEnum(Enum):
    TOY = "Toy"
    STUFFED_ANIMAL = "StuffedAnimal"
    CANDY = "Candy"


class Item(ABC):

    def __init__(self, name, description, product_id, quantity):
        self.name = name
        self.description = description
        self.product_id = product_id
        self.quantity = quantity
        self.error_message = ''


class Toy(Item):

    def __init__(self, min_age, has_batteries, **kwargs):
        super().__init__(**kwargs)
        if min_age < 1:
            self.error_message += '"min_age" must be greater than "1". '
            raise InvalidDataError
        self.min_age = min_age
        self.has_batteries = has_batteries


class SantaWorkshop(Toy):

    def __init__(self, dimensions, num_rooms, **kwargs):
        if self.has_batteries.upper() != "N":
            self.error_message += '"has_batteries" must be "N". '
            raise InvalidDataError
        if num_rooms < 1:
            self.error_message += '"num_rooms" must be greater than "1". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.dimensions = dimensions
        self.num_rooms = num_rooms


class RCSpider(Toy):

    def __init__(self, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        if self.has_batteries.upper() != "Y":
            self.error_message += '"has_batteries" must be "Y". '
            raise InvalidDataError
        if speed < 1:
            self.error_message += '"speed" must be greater than "1". '
            raise InvalidDataError
        if jump_height < 1:
            self.error_message += '"jump_height" must be greater than "1". '
            raise InvalidDataError
        if has_glow.upper() != "N" or has_glow.upper() != "Y":
            self.error_message += '"has_glow" must be set to "Y" or "N". '
            raise InvalidDataError
        if spider_type.upper() != "Tarantula" or \
                spider_type.upper() != "Wolf Spider":
            self.error_message += '"spider_type" must be either "Tarantula" ' \
                                  'or "Wolf Spider". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.spider_type = spider_type


class RobotBunny(Toy):

    def __init__(self, num_sound, colour, **kwargs):
        if num_sound < 1:
            self.error_message += '"num_sound" must be greater than "1" '
            raise InvalidDataError
        if colour.title() != "Orange" and colour.title() != "Blue" and \
                colour.title() != "Pink":
            self.error_message += '"colour" must be either "Orange", "Blue", '\
                                  'or "Pink". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.num_sound = num_sound
        self.color = colour


class StuffedAnimal(Item):

    def __init__(self, stuffing, size, fabric, **kwargs):
        if size.upper() != "S" and size.upper() != "M" and size.upper() != "L":
            self.error_message += '"size" must be either "S", "M" ' \
                                  'or "L". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric


class DancingSkeletons(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        if self.stuffing.title() != "Polyester Fibrefill":
            self.error_message += '"stuffing" must be "Polyester Fibrefill". '
            raise InvalidDataError
        if self.fabric.title() != "Acrylic":
            self.error_message += '"fabric" must be "Acrylic". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.has_glow = has_glow


class Reindeer(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        if self.stuffing.title() != "Wool":
            self.error_message += '"stuffing" must be "Wool". '
            raise InvalidDataError
        if self.fabric.title() != "Cotton":
            self.error_message += '"fabric" must be "Cotton". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.has_glow = has_glow


class EasterBunny(StuffedAnimal):

    def __init__(self, colour, **kwargs):
        if self.stuffing.title() != "Polyester Fibrefill":
            self.error_message += '"stuffing" must be "Polyester Fibrefill". '
            raise InvalidDataError
        if self.fabric.title() != "Linen":
            self.error_message += '"fabric" must be "Linen". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.colour = colour


class Candy(Item):

    def __init__(self, has_lactose, has_nuts, **kwargs):
        super().__init__(**kwargs)
        self.has_lactose = has_lactose
        self.has_nuts = has_nuts


class PumpkinCaramelToffee(Candy):

    def __init__(self, variety, **kwargs):
        if self.has_lactose != "N":
            self.error_message += '"has_lactose" must be "N". '
            raise InvalidDataError
        if self.has_nuts != "Y":
            self.error_message += '"has_nuts" must be "Y". '
            raise InvalidDataError
        if variety.title() != "Sea Salt" or variety.title() != "Regular":
            self.error_message += '"variety" must be "Sea Salt" or "Regular". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.variety = variety


class CandyCane(Candy):

    def __init__(self, colour, **kwargs):
        if self.has_lactose != "Y":
            self.error_message += '"has_lactose" must be "Y". '
            raise InvalidDataError
        if self.has_nuts != "N":
            self.error_message += '"has_nuts" must be "N". '
            raise InvalidDataError
        if colour.title() != "Red" or colour.title() != "Green":
            self.error_message += '"colour" must be "Red" or "Green". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.colour = colour


class CremeEggs(Candy):

    def __init__(self, pack_size, **kwargs):
        if self.has_lactose != "N":
            self.error_message += '"has_lactose" must be "N". '
            raise InvalidDataError
        if self.has_nuts != "Y":
            self.error_message += '"has_nuts" must be "Y". '
            raise InvalidDataError
        if pack_size < 5:
            self.error_message += '"has_nuts" must be greater than "5". '
            raise InvalidDataError
        super().__init__(**kwargs)
        self.pack_size = pack_size


def main():
    args = {'name': 'Santas Workshop - Essentials Edition', 'product_id':
        'C1230T',
     'quantity': 10,
     'description': 'The most sought after christmas present! Get yours today!',
     'has_batteries': 'N', 'min_age': 5.0, 'dimensions': '50,90',
     'num_rooms': 4.0}
    santa_workshop = SantaWorkshop(**args)
    print(santa_workshop)

    args = {'name': 'Easter Bunny with Top Hat', 'product_id': 'E2446E', 'quantity': 2, 'description': 'The easter bunny is now ready for all the tea parties you can host with his Jacket and Top Hat!', 'colour': 'Grey', 'stuffing': 'Polyester Fibrefill', 'size': 'M', 'fabric': 'Linen'}
    easter_bunny = EasterBunny(**args)
    print(easter_bunny)

    args = {'name': 'Mr. Hoppers', 'product_id': 'E4835T', 'quantity': 10, 'description': 'Learn the alphabet with the interactive toys for infants.', 'has_batteries': 'Y', 'min_age': 1.0, 'num_sound': 30.0, 'colour': 'Orange'}
    easter_toy = RobotBunny(**args)
    print(easter_toy)

    args = {'name': 'Howling Wolf Spider', 'product_id': 'H2345T', 'quantity': 4, 'description': 'The howling wolf spider jumps higher and faster than the terrifying tarantula. This is the toy for the ultimate prank.', 'has_batteries': 'Y', 'min_age': 9.0, 'speed': 15.0, 'jump_height': 5.0, 'has_glow': 'N', 'spider_type': 'Wolf Spider'}
    rc_spider = RCSpider(**args)
    print(rc_spider)

    args = {'name': 'Skello the Tap Dancer', 'product_id': 'H4443S', 'quantity': 1, 'description': 'Decorate your home with Skello the Tap Dancer. Oh the whimsical horror!', 'has_glow': 'Y', 'stuffing': 'Polyester Fibrefill', 'size': 'L', 'fabric': 'Acrylic'}
    halloween_stuffed_animals = DancingSkeletons(**args)
    print(halloween_stuffed_animals)


if __name__ == "__main__":
    main()
