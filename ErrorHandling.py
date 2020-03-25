"""
This module contains custom exceptions
"""


class InvalidDataError(Exception):
    """Custom exception for invalid data entries"""

    DEFAULT_MESSAGE = "Could not process order data was corrupted"

    def __init__(self, message=""):
        """Initializes an InvalidDataError object"""
        self.message = message
        super().__init__(f"{self.DEFAULT_MESSAGE}, " + message)
