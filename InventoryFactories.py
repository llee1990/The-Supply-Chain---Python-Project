"""
This module contains all of the abstract factories used to create inventory
items.
"""

from abc import ABC, abstractmethod
from enum import Enum
from InventoryItems import SantaWorkshop, RCSpider, RobotBunny, \
    DancingSkeletons, Reindeer, EasterBunny, PumpkinCaramelToffee, \
    CandyCane, CremeEggs, ItemEnum


class FactoryEnum(Enum):
    """Enum class for types of holidays"""
    CHRISTMAS = "Christmas"
    EASTER = "Easter"
    HALLOWEEN = "Halloween"


class SeasonalItemFactory(ABC):
    """SeasonalItemFactory abstract factory class used to create different
    inventory items based on item types"""

    def __init__(self):
        """Initializes a SeasonalItemFactory object"""
        pass

    def create_item(self, item_type, **kwargs):
        """
        Creates inventory item based on item type

        :param item_type: A String
        :param kwargs: Keyword arguments taken from Series object
        :return: Toy, StuffedAnimal, or Candy based on item_type value
        """
        if item_type == ItemEnum.TOY.value:
            return self._create_toy(**kwargs)
        if item_type == ItemEnum.STUFFED_ANIMAL.value:
            return self._create_stuffed_animal(**kwargs)
        if item_type == ItemEnum.CANDY.value:
            return self._create_candy(**kwargs)

    @abstractmethod
    def _create_toy(self, **kwargs):
        """Private abstract method for create_toy"""
        pass

    @abstractmethod
    def _create_stuffed_animal(self, **kwargs):
        """Private abstract method for create_stuffed_animal"""
        pass

    @abstractmethod
    def _create_candy(self, **kwargs):
        """Private abstract method for create_candy"""
        pass


class ChristmasItemFactory(SeasonalItemFactory):
    """ChristmasItemFactory class, creates Items that are Christmas themed"""

    def __init__(self):
        """Initializes a ChristmasItemFactory object"""
        super().__init__()

    def _create_toy(self, **kwargs) -> SantaWorkshop:
        """
        Creates a christmas Toy
        :param kwargs: Keyword arguments containing item attributes
        :return: SantaWorkshop of type Toy
        """
        return SantaWorkshop(**kwargs)

    def _create_stuffed_animal(self, **kwargs) -> Reindeer:
        """
        Creates a christmas StuffedAnimal
        :param kwargs: Keyword arguments containing item attributes
        :return: Reindeer of type StuffedAnimal
        """
        return Reindeer(**kwargs)

    def _create_candy(self, **kwargs) -> CandyCane:
        """
        Creates a christmas Candy
        :param kwargs: Keyword arguments containing item attributes
        :return: CandyCane of type Candy
        """
        return CandyCane(**kwargs)


class HalloweenItemFactory(SeasonalItemFactory):
    """HalloweenItemFactory class, creates Items that are Halloween themed"""

    def __init__(self):
        """Initializes a HalloweenItemFactory object"""
        super().__init__()

    def _create_toy(self, **kwargs) -> RCSpider:
        """
        Creates a Halloween Toy
        :param kwargs: Keyword arguments containing item attributes
        :return: RCSpider of type Toy
        """
        return RCSpider(**kwargs)

    def _create_stuffed_animal(self, **kwargs) -> DancingSkeletons:
        """
        Creates a Halloween StuffedAnimal
        :param kwargs: Keyword arguments containing item attributes
        :return: DancingSkeleton of type StuffedAnimal
        """
        return DancingSkeletons(**kwargs)

    def _create_candy(self, **kwargs) -> PumpkinCaramelToffee:
        """
        Creates a Halloween Candy
        :param kwargs: Keyword arguments containing item attributes
        :return: PumpkinCaramelToffee of type Toy
        """
        return PumpkinCaramelToffee(**kwargs)


class EasterItemFactory(SeasonalItemFactory):
    """EasterItemFactory class, creates Items that are Easter themed"""

    def __init__(self):
        """Initializes a EasterItemFactory object"""
        super().__init__()

    def _create_toy(self, **kwargs) -> RobotBunny:
        """
        Creates an Easter Toy
        :param kwargs: Keyword arguments containing item attributes
        :return: RobotBunny of type Toy
        """
        return RobotBunny(**kwargs)

    def _create_stuffed_animal(self, **kwargs) -> EasterBunny:
        """
        Creates an Easter StuffedAnimal
        :param kwargs: Keyword arguments containing item attributes
        :return: EasterBunny of type StuffedAnimal
        """
        return EasterBunny(**kwargs)

    def _create_candy(self, **kwargs) -> CremeEggs:
        """
        Creates an Easter Candy
        :param kwargs: Keyword arguments containing item attributes
        :return: CremeEggs of type Candy
        """
        return CremeEggs(**kwargs)
