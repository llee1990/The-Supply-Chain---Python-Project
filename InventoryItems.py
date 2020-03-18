"""

"""

import abc


class InventoryItems(abc.ABC):

    def __init__(self, name, description, product_id):
        self.name = name
        self.description = description
        self.product_id = product_id


class Toys(InventoryItems):

    def __init__(self, has_batteries, min_age, **kwargs):
        super().__init__(**kwargs)
        self.has_batteries = has_batteries
        self.min_age = min_age


class SantaWorkshop(Toys):

    def __init__(self, has_batteries, dimensions, num_rooms, **kwargs):
        if has_batteries.upper() != "N":
            raise AttributeError
        if num_rooms < 1:
            raise AttributeError
        self.dimensions = dimensions
        self.num_rooms = num_rooms
        super().__init__(**kwargs)


class RCSpider(Toys):

    def __init__(self, has_batteries, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        if has_batteries.upper() != "Y":
            raise AttributeError
        if speed < 1:
            raise AttributeError
        if jump_height < 1:
            raise AttributeError
        if has_glow.upper() != "N" or has_glow.upper() != "Y":
            raise AttributeError
        if spider_type.upper() != "Tarantula" or \
                spider_type.upper() != "Wolf Spider":
            raise AttributeError
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.spider_type = spider_type
        super().__init__(**kwargs)


class RobotBunny(Toys):

    def __init__(self, num_sounds, color, **kwargs):
        if num_sounds < 1:
            raise AttributeError
        if color.title() != "Orange" or color.title() != "Blue" or \
                color.title() != "Pink":
            raise AttributeError
        self.num_sounds = num_sounds
        self.color = color
        super().__init__(**kwargs)


class StuffedAnimals(InventoryItems):

    def __init__(self):
        super().__init__()


class DancingSkeletons(StuffedAnimals):

    def __init__(self):
        super().__init__()


class Reindeer(StuffedAnimals):

    def __init__(self):
        super().__init__()


class EasterBunny(StuffedAnimals):

    def __init__(self):
        super().__init__()


class Candy(InventoryItems):

    def __init__(self):
        pass


class PumpkinCaramelToffee(Candy):

    def __init__(self):
        super().__init__()


class CandyCane(Candy):

    def __init__(self):
        super().__init__()


class CremeEggs(Candy):

    def __init__(self):
        super().__init__()