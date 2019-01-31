"""
race module
"""
from typing import Any


class RaceRegistry:
    """A class representing a new race registry with runners' email and their speed category.
    """

    def __init__(self, email: str, category: str) -> None:
        """Initialize a new race registry.

        # Question 1
        Precondition: category must be one of 'under 20 min', 'under 30 min', 'under 40 min', '40 min or over'
        """

        self.email = email
        self.runner = {email: category}

    def __eq__(self, other: Any) -> bool:
        """Return wether self is equivalent to other.

        >>> RaceRegistry('jack@mail.toronto.ca', 'under 20 min') == RaceRegistry('jack@mail.toronto.ca', 'under 20 min')
        True
        >>> RaceRegistry('anna@mail.toronto.ca', 'under 20 min') == RaceRegistry('jack@mail.toronto.ca', 'under 20 min')
        False
        """

        return type(self) == type(other) and self.runner == other.runner

    def __str__(self) -> str:
        """Return a string representation of race registry.

        >>> print(RaceRegistry('jack@mail.toronto.ca', 'under 20 min'))
        The race has runners jack@mail.toronto.ca.
        """

        return "The race has runners {}.".format(self.email)

    def register(self, email: str, category: str) -> None:
        """Register runner's email and catergory to the race registry

        >>> r = RaceRegistry('ann@mail.utoronto.ca', 'under 20 min')
        >>> r.register('jack@mail.utoronto.ca', 'under 20 min')
        >>> r.runner
        {'ann@mail.utoronto.ca': 'under 20 min', 'jack@mail.utoronto.ca': 'under 20 min'}
        """

        self.email += ', ' + email
        self.runner[email] = category

    def email_to_category(self, email: str) -> str:
        """Return a string representing the category of the given runner's email.

        >>> r = RaceRegistry('ann@mail.utoronto.ca', 'under 20 min')
        >>> r.email_to_category('ann@mail.utoronto.ca')
        'under 20 min'
        """

        return self.runner[email]

    def category_to_email(self, category: str) -> list:
        """Return a list containing the emails of runners which is under the given speed category.

        >>> r = RaceRegistry('ann@mail.utoronto.ca', 'under 20 min')
        >>> r.register('jack@mail.utoronto.ca', 'under 20 min')
        >>> r.category_to_email('under 20 min')
        ['ann@mail.utoronto.ca', 'jack@mail.utoronto.ca']
        """

        result = []
        for email in self.runner:
            if self.runner[email] == category:
                result.append(email)
        return result


if __name__ == '__main__':
    from doctest import testmod
    testmod()

    r = RaceRegistry('gerhard@mail.utoronto.ca', 'under 40 min')
    r.register('tom@mail.utoronto.ca', 'under 30 min')
    r.register('toni@mail.utoronto.ca', 'under 20 min')
    r.register('margot@mail.utoronto.ca', 'under 30 min')
    r.register('gerhard@mail.utoronto.ca', 'uner 30 min')

    print(r.category_to_email('under 30 min'))
