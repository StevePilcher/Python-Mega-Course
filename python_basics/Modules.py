import time
import os

while True:
    if os.path.exists('fruits.txt'):
        with open('fruits.txt') as file:
            print(file.read())
    else:
        print('File does not exist')
    time.sleep(10)

