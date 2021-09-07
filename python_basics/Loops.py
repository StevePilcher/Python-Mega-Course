avg_grade_list = [9.1, 8.8, 7.5]

for grade in avg_grade_list:
    print(round(grade))

for letter in 'hello':
    print(letter)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int):
        print(color)


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))