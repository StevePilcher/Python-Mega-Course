def area(a, b):
    return a * b


print(area(5, 6))


def join_string(a, b):
    return a + b


print(join_string('abc', 'cde'))

# Keyword arguments uses equals
# Position of key not important
print(area(a=4, b=6))
print(area(b=6, a=4))

# Non-keyword arguments doesn't

print(area(3, 6))

