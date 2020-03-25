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

    def __init__(self, name, description, product_id, quantity, order_number):
        self._name = name
        self._description = description
        self._product_id = product_id
        self._quantity = quantity
        self._error_message = ''
        self._order_number = order_number
        
    @property
    def error_message(self):
        return self._error_message

    @property
    def order_number(self):
        return self._order_number


class Toy(Item):

    def __init__(self, min_age, has_batteries, **kwargs):
        super().__init__(**kwargs)
        if min_age < 1:
            self._error_message += '"min_age" must be greater than "1". '
        self._min_age = min_age
        self._has_batteries = has_batteries   


class SantaWorkshop(Toy):

    def __init__(self, dimensions, num_rooms, **kwargs):
        super().__init__(**kwargs)
        if self._has_batteries.upper() != "N":
            self._error_message += '"has_batteries" must be "N". '
        if num_rooms < 1:
            self._error_message += '"num_rooms" must be greater than "1". '
        self._dimensions = dimensions
        self._num_rooms = num_rooms
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError
        
    def __str__(self):
        
        return f"{self._name}, {self._description}, {self._product_id}, " \
               f"{self._quantity}, {self._min_age}, {self._has_batteries}, " \
               f"{self._dimensions}, {self._num_rooms}"


class RCSpider(Toy):

    def __init__(self, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        super().__init__(**kwargs)
        if self._has_batteries.upper() != "Y":
            self._error_message += '"has_batteries" must be "Y". '
        if speed < 1:
            self._error_message += '"speed" must be greater than "1". '
        if jump_height < 1:
            self._error_message += '"jump_height" must be greater than "1". '
        if has_glow.upper() != "N" and has_glow.upper() != "Y":
            self._error_message += '"has_glow" must be set to "Y" or "N". '
        if spider_type.title() != "Tarantula" and \
                spider_type.title() != "Wolf Spider":
            self._error_message += '"spider_type" must be either "Tarantula" ' \
                                  'or "Wolf Spider". '
        self._speed = speed
        self._jump_height = jump_height
        self._has_glow = has_glow
        self._spider_type = spider_type
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class RobotBunny(Toy):

    def __init__(self, num_sound, colour, **kwargs):
        super().__init__(**kwargs)
        if num_sound < 1:
            self._error_message += '"num_sound" must be greater than "1" '
        if colour.title() != "Orange" and colour.title() != "Blue" and \
                colour.title() != "Pink":
            self._error_message += '"colour" must be either "Orange", "Blue", '\
                                  'or "Pink". '
        self._num_sound = num_sound
        self._colour = colour
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class StuffedAnimal(Item):

    def __init__(self, stuffing, size, fabric, **kwargs):
        super().__init__(**kwargs)
        if size.upper() != "S" and size.upper() != "M" and size.upper() != "L":
            self._error_message += '"size" must be either "S", "M" ' \
                                  'or "L". '
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric


class DancingSkeletons(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        super().__init__(**kwargs)
        if self._stuffing.title() != "Polyester Fibrefill":
            self._error_message += '"stuffing" must be "Polyester Fibrefill". '
        if self._fabric.title() != "Acrylic":
            self._error_message += '"fabric" must be "Acrylic". '
        self._has_glow = has_glow
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class Reindeer(StuffedAnimal):

    def __init__(self, has_glow, **kwargs):
        super().__init__(**kwargs)
        if self._stuffing.title() != "Wool":
            self._error_message += '"stuffing" must be "Wool". '
        if self._fabric.title() != "Cotton":
            self._error_message += '"fabric" must be "Cotton". '
        self._has_glow = has_glow
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class EasterBunny(StuffedAnimal):

    def __init__(self, colour, **kwargs):
        super().__init__(**kwargs)
        if self._stuffing.title() != "Polyester Fibrefill":
            self._error_message += '"stuffing" must be "Polyester Fibrefill". '
        if self._fabric.title() != "Linen":
            self._error_message += '"fabric" must be "Linen". '
        self._colour = colour
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class Candy(Item):

    def __init__(self, has_lactose, has_nuts, **kwargs):
        super().__init__(**kwargs)
        self._has_lactose = has_lactose
        self._has_nuts = has_nuts


class PumpkinCaramelToffee(Candy):

    def __init__(self, variety, **kwargs):
        super().__init__(**kwargs)
        if self._has_lactose.upper() != "Y":
            self._error_message += '"has_lactose" must be "Y". '
        if self._has_nuts.upper() != "Y":
            self._error_message += '"has_nuts" must be "Y". '
        if variety.title() != "Sea Salt" and variety.title() != "Regular":
            self._error_message += '"variety" must be "Sea Salt" or "Regular". '
        self._variety = variety
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class CandyCane(Candy):

    def __init__(self, colour, **kwargs):
        super().__init__(**kwargs)
        if self._has_lactose.upper() != "N":
            self._error_message += '"has_lactose" must be "N". '
        if self._has_nuts.upper() != "N":
            self._error_message += '"has_nuts" must be "N". '
        if colour.title() != "Red" and colour.title() != "Green":
            self._error_message += '"colour" must be "Red" or "Green". '
        self._colour = colour
        if self._error_message != '':
            print(self._error_message)
            raise InvalidDataError


class CremeEggs(Candy):

    def __init__(self, pack_size, **kwargs):
        super().__init__(**kwargs)
        if self._has_lactose.upper() != "Y":
            self._error_message += '"has_lactose" must be "Y". '
        if self._has_nuts.upper() != "Y":
            self._error_message += '"has_nuts" must be "Y". '
        if pack_size < 5:
            self._error_message += '"has_nuts" must be greater than "5". '
        self._pack_size = pack_size
        if self._error_message != '':
            print(self._error_message)
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
