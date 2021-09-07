def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean


print(mean([1, 9, 5]))


def mean_2(*args):
    return args


print(mean_2('abc', 2, 2 * 3))
