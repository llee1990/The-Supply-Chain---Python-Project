"""

"""


class InvalidDataError(Exception):

    def __init__(self):
        super().__init__(f"Could not process order, data was corrupt.")