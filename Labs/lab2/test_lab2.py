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
