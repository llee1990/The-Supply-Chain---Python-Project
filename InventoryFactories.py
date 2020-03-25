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

    def create_item(self, item_type, **kwargs):
        if item_type == ItemEnum.TOY.value:
            return self._create_toy(**kwargs)
        if item_type == ItemEnum.STUFFED_ANIMAL.value:
            return self._create_stuffed_animal(**kwargs)
        if item_type == ItemEnum.CANDY.value:
            return self._create_candy(**kwargs)

    @abstractmethod
    def _create_toy(self, **kwargs):
        pass

    @abstractmethod
    def _create_stuffed_animal(self, **kwargs):
        pass

    @abstractmethod
    def _create_candy(self, **kwargs):
        pass


class ChristmasItemFactory(SeasonalItemFactory):

    def __init__(self):
        super().__init__()

    def _create_toy(self, **kwargs) -> SantaWorkshop:
        return SantaWorkshop(**kwargs)

    def _create_stuffed_animal(self, **kwargs) -> Reindeer:
        return Reindeer(**kwargs)

    def _create_candy(self, **kwargs) -> CandyCane:
        return CandyCane(**kwargs)


class HalloweenItemFactory(SeasonalItemFactory):

    def __init__(self):
        super().__init__()

    def _create_toy(self, **kwargs) -> RCSpider:
        return RCSpider(**kwargs)

    def _create_stuffed_animal(self, **kwargs) -> DancingSkeletons:
        return DancingSkeletons(**kwargs)

    def _create_candy(self, **kwargs) -> PumpkinCaramelToffee:
        return PumpkinCaramelToffee(**kwargs)


class EasterItemFactory(SeasonalItemFactory):

    def __init__(self):
        super().__init__()

    def _create_toy(self, **kwargs) -> RobotBunny:
        return RobotBunny(**kwargs)

    def _create_stuffed_animal(self, **kwargs) -> EasterBunny:
        return EasterBunny(**kwargs)

    def _create_candy(self, **kwargs) -> CremeEggs:
        return CremeEggs(**kwargs)
