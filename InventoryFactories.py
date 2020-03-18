"""

"""

import abc


class InventoryFactory(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def create_items(self):
        pass


class ToysFactory(InventoryFactory):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def create_items(self):
        pass


class SantaShopFactory(ToysFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class RCSpiderFactory(ToysFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class RobotBunnyFactory(ToysFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class StuffedAnimalsFactory(InventoryFactory):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def create_items(self):
        pass


class DancingSkeletonFactory(StuffedAnimalsFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class ReindeerFactory(StuffedAnimalsFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class EasterBunnyFactory(StuffedAnimalsFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class CandyFactory(InventoryFactory):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def create_items(self):
        pass


class PCTFactory(CandyFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class CandyCanesFactory(CandyFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass


class CremeEggsFactory(CandyFactory):

    def __init__(self):
        super().__init__()

    def create_items(self):
        pass