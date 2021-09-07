# Unlimited number of arguments passed to the function

def mean_2(*args):
    return args


print(mean_2('abc', 2, 2 * 3))


def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)


print(foo('snow', 'glacier', 'iceberg'))


# input ['snow', 'glacier', 'iceberg']
# output ['GLACIER', 'ICEBERG', 'SNOW']


def foo2(*args):
    args = [x.upper() for x in args]
    return sorted(args)


print(foo2('snow', 'glacier', 'iceberg'))
