def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean


print(mean([9.1, 4.8, 90]))

pupils = {'Mary': 9.1, 'Scott': 4.8, 'Tim': 9.8}