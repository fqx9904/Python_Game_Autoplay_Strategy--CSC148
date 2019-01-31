
try:
    a = a
    1 / 0
    1 + '2'
except ZeroDivisionError as ee:
    print("there is an error")
    print(ee)
except TypeError:
    print('Value Wrong.')
except Exception:
    print("Exception")

print('wow')
