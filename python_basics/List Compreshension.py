# Loop a list

temps = [210, 310, 260, 180, 230]

new_temps = []

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# Loop as a list comprehension

newer_temps = [temp / 10 for temp in temps]

print(newer_temps)

# loop with if else conditional

newest_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]


# replace strings with 0 in lists

def foo3(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]


print(newest_temps)


# quiz answers

# function to return numbers only


def foo(lst):
    return [i for i in lst if isinstance(i, int)]


print(foo([1, -5, 'abc', 'trolley', -2, 3, 6, 0]))


# positive numbers only
def foo1(lst):
    return [i for i in lst if i > 0]


print(foo1([1, -5, -2, 3, 6, 0]))

# Cheatsheet (List Comprehensions)
#
# In this section, you learned that:
#
#     A list comprehension is an expression that creates a list by iterating over another container.
#
#     A basic list comprehension:
#
#         [i*2 for i in [1, 5, 10]]
#
#     Output: [2, 10, 20]
#
#     List comprehension with if condition:
#
#         [i*2 for i in [1, -2, 10] if i>0]
#
#     Output: [2, 20]
#
#     List comprehension with an if and else condition:
#
#         [i*2 if i>0 else 0 for i in [1, -2, 10]]
#
#     Output: [2, 0, 20]


