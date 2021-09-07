# Keyword arguements passed to a function, returns a dictionary

def mean(**kwargs):
    return kwargs


print(mean(a=4, b=6, c=7))

# Output dict {'a': 4, 'b': 6, 'c': 7}

