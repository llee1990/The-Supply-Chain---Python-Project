"""

"""

from abc import ABC, abstractmethod
from enum import Enum
from InventoryItems import SantaWorkshop, RCSpider, RobotBunny, \
    DancingSkeletons, Reindeer, EasterBunny, PumpkinCaramelToffee, \
    CandyCane, CremeEggs, ItemEnum


class FactoryEnum(Enum):
    CHRISTMAS = "Christmas"
    EASTER = "Easter"
    HALLOWEEN = "Halloween"


class SeasonalItemFactory(ABC):

    def __init__(self):
        pass

    def create_items(self, item_type, **order):

        if item_type == ItemEnum.TOY:
            self.create_toy(**order)
        if item_type == ItemEnum.STUFFED_ANIMAL:
            self.create_stuffed_animal(**order)
        if item_type == ItemEnum.CANDY:
            self.create_candy(**order)

    @abstractmethod
    def create_toy(self, **kwargs):
        pass

    @abstractmethod
    def create_stuffed_animal(self, **kwargs):
        pass

    @abstractmethod
    def create_candy(self, **kwargs):
        pass


class ChristmasItemFactory(SeasonalItemFactory):

    def __init__(self):
        pass

    def create_toy(self, **kwargs) -> SantaWorkshop:
        return SantaWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> Reindeer:
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs) -> CandyCane:
        return CandyCane(**kwargs)


class HalloweenItemFactory(SeasonalItemFactory):

    def __init__(self):
        pass

    def create_toy(self, **kwargs) -> RCSpider:
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> DancingSkeletons:
        return DancingSkeletons(**kwargs)

    def create_candy(self, **kwargs) -> PumpkinCaramelToffee:
        return PumpkinCaramelToffee(**kwargs)


class EasterItemFactory(SeasonalItemFactory):

    def __init__(self):
        pass

    def create_toy(self, **kwargs) -> RobotBunny:
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> EasterBunny:
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs) -> CremeEggs:
        return CremeEggs(**kwargs)
