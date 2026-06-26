from dataclasses import dataclass
from datetime import datetime


@dataclass
class Driver:
    driverId : int
    driverRef : str
    number : int
    code : str
    forename : str
    surname : str
    nationality : str
    url : str

    def __hash__(self):
        return hash(self.driverId)

    def __str__(self):
        return f"{self.surname}"
