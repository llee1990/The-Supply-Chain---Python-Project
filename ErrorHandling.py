"""

"""


class InvalidDataError(Exception):

    DEFAULT_MESSAGE = "Could not process order data was corrupted, "

    def __init__(self, message=""):
        self.message = message
        super().__init__(f"{self.DEFAULT_MESSAGE}, " + message)
