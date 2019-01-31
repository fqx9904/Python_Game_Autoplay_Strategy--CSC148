"""
grade module
"""
from typing import Any


class GradeEntry:
    """Represent a general entry with student grade information.

    course_id - a course iddentifier in which the grade earned
    weight - credit weight of the course
    grade - no value until we know whether numeric or letter value is used
    """
    course_id: str
    course_weight: float
    grade: None

    def __init__(self, course_id: str, weight: float, grade=None) -> None:
        """Initialize a new grade entry.
        """
        self.course_id = course_id
        self.grade = grade
        self.weight = weight

    def __eq__(self, other: Any) -> bool:
        """Return whether self is equivalent to other.
        """
        return type(self) == type(other) and self.course_id == other.course_id and self.weight == other.weight and \
            self.grade == other.grade

    def __str__(self) -> str:
        """Return a string representation of a grade entry.
        """
        return "{}: Weight:{}, Grade:{}".format(self.course_id, self.weight, self.grade)

    def generate_points(self) -> float:
        """return a float numebr which is the grade earned of the course.
        """
        raise NotImplementedError("Subclass needed")


class LetterGradeEntry(GradeEntry):
    """Represent a grade entry with letter grade.

    letter_grade - a grade represented by {A, B, C, D, E, F} and suffix {+, -}
    """
    letter_grade: str

    table = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
             'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0.0}

    def __init__(self, course_id: str, weight: float, grade: str) -> None:
        """Initialize a new letter grade entry.
        """
        GradeEntry.__init__(self, course_id, weight, grade)
        self.grade = grade

    def generate_points(self) -> float:
        """return a float numebr which is the grade earned of the course.
        """
        return self.table[self.grade]


class NumericGradeEntry(GradeEntry):
    """Represent a grade entry with letter grade.

    num_grade - a grade represented by {A, B, C, D, E, F} and suffix {+, -}
    """
    num_grade: int

    table = {4.0: [85, 100], 3.7: [80, 84], 3.3: [77, 79], 3.0: [73, 76], 2.7: [70, 72], 2.3: [67, 69], 2.0: [63, 66],
             1.7: [60, 62], 1.3: [57, 59], 1.0: [53, 56], 0.7: [50, 52]}

    def __init__(self, course_id: str, weight: float, grade: int) -> None:
        """Initialize a new numeric grade entry.
        """
        GradeEntry.__init__(self, course_id, weight, grade)
        self.grade = round(grade)

    def generate_points(self) -> float:
        """return a float numebr which is the grade earned of the course.
        """
        if self.grade < 50:
            return 0.0
        for p in self.table:
            if self.grade in range(self.table[p][0], self.table[p][1] + 1):
                return p


if __name__ == '__main__':
    from grade import LetterGradeEntry, NumericGradeEntry

    grades = [NumericGradeEntry('csc148', 0.5, 87), NumericGradeEntry('mat137', 1.0, 76),
              LetterGradeEntry('his450', 0.5, 'B+')]
    for g in grades:
        # Use appropriate ??? methods or attributes of g in format
        print('Weight: {}, grade: {}, points: {}'.format(g.weight, g.grade, g.generate_points()))
    # Use methods or attributes of g to compute weight times points
    total = sum([g.weight * g.generate_points() for g in grades])  # using each g in grades
    # sum up the credits
    total_weight = sum([g.weight for g in grades])
    print('GPA = {}'.format(total / total_weight))
