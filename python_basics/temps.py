def weather_condition(temp):
    if temp > 7:
        return 'Warm'
    else:
        return 'Cold'


temp = float(input('Please enter the temperature:'))
print(type(temp))

weather_condition(temp)
