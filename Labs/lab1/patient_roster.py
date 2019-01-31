"""
asdasd
"""
from typing import Any


class Patient:
    """A class representing a patient containing patient's OHIP number, family name, last name and gender.
    """

    def __init__(self, OHIP: int, family_name: str, last_name: str, gender: str) -> None:
        """Initialize a new patient roster.
        """
        self.OHIP = OHIP
        self.familty = family_name
        self.last = last_name
        self.gender = gender

    def __eq__(self, other: Any) -> bool:
        """Return whether self and other are equal.
        """

        return type(self) == type(other) and self.OHIP == other.OHIP

class Roster:
    """A class representing a
    """

    def __init__(self)
