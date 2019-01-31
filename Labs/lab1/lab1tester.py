if __name__ == '__main__':
    from lab1 import RaceRegistry

    r = RaceRegistry('gerhard@mail.utoronto.ca', 'under 40 min')
    r.register('tom@mail.utoronto.ca', 'under 30 min')
    r.register('toni@mail.utoronto.ca', 'under 20 min')
    r.register('margot@mail.utoronto.ca', 'under 30 min')
    r.register('gerhard@mail.utoronto.ca', 'uner 30 min')

    print(r.category_to_email('under 30 min'))
