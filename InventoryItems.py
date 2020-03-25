"""
This module contains all the types of inventory items that can be created by
the inventory system.
"""

from abc import ABC
from enum import Enum
from ErrorHandling import InvalidDataError


class ItemEnum(Enum):
    """Enum class for types of Items"""
    TOY = "Toy"
    STUFFED_ANIMAL = "StuffedAnimal"
    CANDY = "Candy"


class Item(ABC):
    """
    Abstract class for Item, parent class of all items that can be
    created
    """

    def __init__(self, name, description, product_id, quantity, order_number):
        """
        Initializes an Item object

        :param name: A String
        :param description: A String
        :param product_id: A String
        :param quantity: A String
        :param order_number: A String
        """
        self._name = name
        self._description = description
        self._product_id = product_id
        self._quantity = quantity
        self._error_message = ''
        self._order_number = order_number

    @property
    def error_message(self):
        """
        Getter for self._error_message
        :return: A String, the error message if any
        """
        return self._error_message

    @property
    def order_number(self):
        """
        Getter for self._order_number
        :return: A String, the order number of the item
        """
        return self._order_number


class Toy(Item):
    """
    The Toy class is the parent class of all toy items.
    """

    def __init__(self, min_age, has_batteries, **kwargs):
        """
        Initializes a Toy object

        :param min_age: A String
        :param has_batteries: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if int(min_age) < 1:
            self._error_message += '"min_age" must be greater than "1". '
        self._min_age = min_age
        self._has_batteries = has_batteries


class SantaWorkshop(Toy):
    """
    The SantaWorkshop class creates SantaWorkshop toys
    """

    def __init__(self, dimensions, num_rooms, **kwargs):
        """
        Initializes a SantaWorkshop object

        :param dimensions: A String
        :param num_rooms: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._has_batteries.upper() != "N":
            self._error_message += '"has_batteries" must be "N". '
        if int(num_rooms) < 1:
            self._error_message += '"num_rooms" must be greater than "1". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._dimensions = dimensions
        self._num_rooms = num_rooms


class RCSpider(Toy):
    """
    The RCSpider class creates RCSpider toys
    """

    def __init__(self, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        """
        Initializes a RCSpider object

        :param speed: A String
        :param jump_height: A String
        :param has_glow: A String
        :param spider_type: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._has_batteries.upper() != "Y":
            self._error_message += '"has_batteries" must be "Y". '
        if int(speed) < 1:
            self._error_message += '"speed" must be greater than "1". '
        if int(jump_height) < 1:
            self._error_message += '"jump_height" must be greater than "1". '
        if has_glow.upper() != "N" and has_glow.upper() != "Y":
            self._error_message += '"has_glow" must be set to "Y" or "N". '
        if spider_type.title() != "Tarantula" and \
                spider_type.title() != "Wolf Spider":
            self._error_message += \
                '"spider_type" must be either "Tarantula" or "Wolf Spider". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._speed = speed
        self._jump_height = jump_height
        self._has_glow = has_glow
        self._spider_type = spider_type


class RobotBunny(Toy):
    """
    The RobotBunny class creates RobotBunny toys
    """

    def __init__(self, num_sound, colour, **kwargs):
        """
        Initializes a RobotBunny object

        :param num_sound: A String
        :param colour: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if int(num_sound) < 1:
            self._error_message += '"num_sound" must be greater than "1" '
        if colour.title() != "Orange" and colour.title() != "Blue" and \
                colour.title() != "Pink":
            self._error_message += '"colour" must be either ' \
                                   '"Orange", "Blue", or "Pink". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._num_sound = num_sound
        self._colour = colour


class StuffedAnimal(Item):
    """Parent class of all StuffedAnimal toys"""

    def __init__(self, stuffing, size, fabric, **kwargs):
        """
        Initializes a StuffedAnimal object

        :param stuffing: A String
        :param size: A String
        :param fabric: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if size.upper() != "S" and size.upper() != "M" and size.upper() != "L":
            self._error_message += '"size" must be either "S", "M" ' \
                                  'or "L". '
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric


class DancingSkeletons(StuffedAnimal):
    """
    Creates DancingSkeletons stuffed animals
    """

    def __init__(self, has_glow, **kwargs):
        """
        Initializes a DancingSkeletons object

        :param has_glow: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._stuffing.title() != "Polyester Fibrefill":
            self._error_message += '"stuffing" must be "Polyester Fibrefill". '
        if self._fabric.title() != "Acrylic":
            self._error_message += '"fabric" must be "Acrylic". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._has_glow = has_glow


class Reindeer(StuffedAnimal):
    """
    Creates Reindeer stuffed animals
    """

    def __init__(self, has_glow, **kwargs):
        """
        Initializes a Reindeer object

        :param has_glow: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._stuffing.title() != "Wool":
            self._error_message += '"stuffing" must be "Wool". '
        if self._fabric.title() != "Cotton":
            self._error_message += '"fabric" must be "Cotton". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._has_glow = has_glow


class EasterBunny(StuffedAnimal):
    """
    Creates EasterBunny stuffed animals
    """

    def __init__(self, colour, **kwargs):
        """
        Initializes an EasterBunny object

        :param colour: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._stuffing.title() != "Polyester Fibrefill":
            self._error_message += '"stuffing" must be "Polyester Fibrefill". '
        if self._fabric.title() != "Linen":
            self._error_message += '"fabric" must be "Linen". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._colour = colour


class Candy(Item):
    """
    Parent class of all Candy items
    """

    def __init__(self, has_lactose, has_nuts, **kwargs):
        super().__init__(**kwargs)
        self._has_lactose = has_lactose
        self._has_nuts = has_nuts


class PumpkinCaramelToffee(Candy):
    """
    Creates PumpkinCaramelToffee candy objects
    """

    def __init__(self, variety, **kwargs):
        """
        Initializes a PumpkinCaramelToffee object

        :param variety: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._has_lactose.upper() != "Y":
            self._error_message += '"has_lactose" must be "Y". '
        if self._has_nuts.upper() != "Y":
            self._error_message += '"has_nuts" must be "Y". '
        if variety.title() != "Sea Salt" and variety.title() != "Regular":
            self._error_message += \
                '"variety" must be "Sea Salt" or "Regular". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._variety = variety


class CandyCane(Candy):
    """
    Creates CandyCane candy objects
    """

    def __init__(self, colour, **kwargs):
        """
        Initializes a CandyCane object

        :param colour: A String
        :param kwargs: Keyword arguments containing item attributes
        that are passed to super()
        """
        super().__init__(**kwargs)
        if self._has_lactose.upper() != "N":
            self._error_message += '"has_lactose" must be "N". '
        if self._has_nuts.upper() != "N":
            self._error_message += '"has_nuts" must be "N". '
        if colour.title() != "Red" and colour.title() != "Green":
            self._error_message += '"colour" must be "Red" or "Green". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)
        self._colour = colour


class CremeEggs(Candy):
    """
    Creates CremeEggs candy objects
    """

    def __init__(self, pack_size, **kwargs):
        """
        Initializes a CremeEggs object

        :param pack_size: A String
        :param kwargs:
        """
        super().__init__(**kwargs)
        if self._has_lactose.upper() != "Y":
            self._error_message += '"has_lactose" must be "Y". '
        if self._has_nuts.upper() != "Y":
            self._error_message += '"has_nuts" must be "Y". '
        if int(pack_size) < 5:
            self._error_message += '"has_nuts" must be greater than "5". '
        if self._error_message != '':
            raise InvalidDataError(self.error_message)

        self._pack_size = pack_size
