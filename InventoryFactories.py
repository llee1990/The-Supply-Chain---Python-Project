"""

"""

from abc import ABC, abstractmethod
from InventoryItems import SantaWorkshop, RCSpider, RobotBunny, \
    DancingSkeletons, Reindeer, EasterBunny, PumpkinCaramelToffee, \
    CandyCane, CremeEggs


class SeasonalItemFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_toy(self):
        pass

    @abstractmethod
    def create_stuffed_animal(self):
        pass

    @abstractmethod
    def create_candy(self):
        pass


class ChristmasItemFactory(SeasonalItemFactory):

    def __init__(self):
        pass

    def create_toy(self) -> SantaWorkshop:
        return SantaWorkshop()

    def create_stuffed_animal(self) -> Reindeer:
        return Reindeer()

    def create_candy(self) -> CandyCane:
        return CandyCane()


class HalloweenItemFactory(SeasonalItemFactory):

    def __init__(self):
        pass

    def create_toy(self) -> RCSpider:
        return RCSpider()

    def create_stuffed_animal(self) -> DancingSkeletons:
        return DancingSkeletons()

    def create_candy(self) -> PumpkinCaramelToffee:
        return PumpkinCaramelToffee()


class EasterItemFactory(SeasonalItemFactory):

    def __init__(self):
        pass

    def create_toy(self) -> RobotBunny:
        return RobotBunny()

    def create_stuffed_animal(self) -> EasterBunny:
        return EasterBunny()

    def create_candy(self) -> CremeEggs:
        return CremeEggs()
