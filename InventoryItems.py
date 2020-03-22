"""

"""

from abc import ABC, abstractmethod
from enum import Enum


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


class Toy(Item):

    def __init__(self, min_age, has_batteries, **kwargs):
        super().__init__(**kwargs)
        self.min_age = min_age
        self.has_batteries = has_batteries


class SantaWorkshop(Toy):

    def __init__(self, dimensions, num_rooms, **kwargs):
        # if has_batteries.upper() != "N":
        #     raise AttributeError
        if num_rooms < 1:
            raise AttributeError
        super().__init__(**kwargs)
        self.dimensions = dimensions
        self.num_rooms = num_rooms


class RCSpider(Toy):

    def __init__(self, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        # if has_batteries.upper() != "Y":
        #     raise AttributeError
        # if speed < 1:
        #     raise AttributeError
        # if jump_height < 1:
        #     raise AttributeError
        # if has_glow.upper() != "N" or has_glow.upper() != "Y":
        #     raise AttributeError
        # if spider_type.upper() != "Tarantula" or \
        #         spider_type.upper() != "Wolf Spider":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.spider_type = spider_type


class RobotBunny(Toy):

    def __init__(self, num_sound, colour, **kwargs):
        if num_sound < 1:
            raise AttributeError
        # if color.title() != "Orange" and color.title() != "Blue" and \
        #         color.title() != "Pink":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.num_sound = num_sound
        self.color = colour


class StuffedAnimal(Item):

    def __init__(self, stuffing, size, fabric, **kwargs):
        # if size.upper() != "S" and size.upper() != "M" and size.upper() != "L":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric


class DancingSkeletons(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        # if stuffing.title() != "Polyester Fibrefill":
        #     raise AttributeError
        # if fabric.title() != "Acrylic":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.has_glow = has_glow


class Reindeer(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        # if stuffing.title() != "Wool":
        #     raise AttributeError
        # if fabric.title() != "Cotton":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.has_glow = has_glow


class EasterBunny(StuffedAnimal):

    def __init__(self, colour, **kwargs):
        # if stuffing.title() != "Polyester Fibrefill":
        #     raise AttributeError
        # if fabric.title() != "Linen":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.colour = colour


class Candy(Item):

    def __init__(self, has_lactose, has_nuts, **kwargs):
        super().__init__(**kwargs)
        self.has_lactose = has_lactose
        self.has_nuts = has_nuts


class PumpkinCaramelToffee(Candy):

    def __init__(self, variety, **kwargs):
        # if variety.title() != "Sea Salt" or variety.title() != "Regular":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.variety = variety


class CandyCane(Candy):

    def __init__(self, colour, **kwargs):
        # if colour.title() != "Red" or colour.title() != "Green":
        #     raise AttributeError
        super().__init__(**kwargs)
        self.colour = colour


class CremeEggs(Candy):

    def __init__(self, pack_size, **kwargs):
        # if pack_size < 5:
        #     raise AttributeError
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
