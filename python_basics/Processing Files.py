my_file = open('fruits.txt')
content = my_file.read()
my_file.close()
print(content)

# Better method

with open('fruits.txt') as my_file2:
    content2 = my_file2.read()

print(content2)

# Different file paths
# specify the file relative to the script

# Create a file

with open('vegetables.txt', 'w') as my_file3:
    my_file3.write('Tomato\nCucumber\nOnion')
    my_file3.write('\nOnion')


# Open file and print only 10 characters

file = open("fruits.txt")
content = file.read()
file.close()
print(content[:10])
