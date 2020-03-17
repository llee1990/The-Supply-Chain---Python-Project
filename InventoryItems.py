"""

"""

import abc


class InventoryItems(abc.ABC):

    def __init__(self):
        pass


class Toys(InventoryItems):

    def __init__(self):
        super().__init__()


class SantaWorkshop(Toys):

    def __init__(self):
        super().__init__()


class RCSpider(Toys):

    def __init__(self):
        super().__init__()


class RobotBunny(Toys):

    def __init__(self):
        super().__init__()


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