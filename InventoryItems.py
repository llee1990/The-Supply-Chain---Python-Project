"""

"""

from abc import ABC, abstractmethod


class Toys(ABC):

    def __init__(self):
        pass


class SantaWorkshop(Toys):

    def __init__(self, has_batteries, dimensions, num_rooms, **kwargs):
        pass
        # if has_batteries.upper() != "N":
        #     raise AttributeError
        # if num_rooms < 1:
        #     raise AttributeError
        # super().__init__(**kwargs)
        # self.dimensions = dimensions
        # self.num_rooms = num_rooms


class RCSpider(Toys):

    def __init__(self, has_batteries, speed, jump_height, has_glow,
                 spider_type, **kwargs):
        pass
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
        # super().__init__(**kwargs)
        # self.speed = speed
        # self.jump_height = jump_height
        # self.has_glow = has_glow
        # self.spider_type = spider_type


class RobotBunny(Toys):

    def __init__(self, num_sounds, color, **kwargs):
        pass
        # if num_sounds < 1:
        #     raise AttributeError
        # if color.title() != "Orange" and color.title() != "Blue" and \
        #         color.title() != "Pink":
        #     raise AttributeError
        # super().__init__(**kwargs)
        # self.num_sounds = num_sounds
        # self.color = color


class StuffedAnimals(ABC):

    def __init__(self):
        pass


class DancingSkeletons(StuffedAnimals):

    def __init__(self, stuffing, fabric, has_glow, **kwargs):
        if stuffing.title() != "Polyester Fibrefill":
            raise AttributeError
        if fabric.title() != "Acrylic":
            raise AttributeError
        super().__init__(**kwargs)
        self.has_glow = has_glow


class Reindeer(StuffedAnimals):

    def __init__(self, stuffing, fabric, has_glow, **kwargs):
        if stuffing.title() != "Wool":
            raise AttributeError
        if fabric.title() != "Cotton":
            raise AttributeError
        super().__init__(**kwargs)
        self.has_glow = has_glow


class EasterBunny(StuffedAnimals):

    def __init__(self, stuffing, fabric, **kwargs):
        pass
        # if stuffing.title() != "Polyester Fibrefill":
        #     raise AttributeError
        # if fabric.title() != "Linen":
        #     raise AttributeError
        # super().__init__(**kwargs)


class Candy(ABC):

    def __init__(self, has_lactose, has_nuts, **kwargs):
        pass
        # super().__init__(**kwargs)
        # self.has_lactose = has_lactose
        # self.has_nuts = has_nuts


class PumpkinCaramelToffee(Candy):

    def __init__(self, variety, **kwargs):
        pass
        # if variety.title() != "Sea Salt" or variety.title() != "Regular":
        #     raise AttributeError
        # super().__init__(**kwargs)
        # self.variety = variety


class CandyCane(Candy):

    def __init__(self, colour, **kwargs):
        pass
        # if colour.title() != "Red" or colour.title() != "Green":
        #     raise AttributeError
        # super().__init__(**kwargs)
        # self.colour = colour


class CremeEggs(Candy):

    def __init__(self, pack_size, **kwargs):
        pass
        # if pack_size < 5:
        #     raise AttributeError
        # super().__init__(**kwargs)
        # self.pack_size = pack_size
