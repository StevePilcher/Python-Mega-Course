import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or "n":
            return "The word does not exist. Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word does not exist. Please double check it"


# User Inputs a search word
word = input('Enter word: ')

# Output of the function call
output = translate(word)

# Iterate through the list [] outputted from the function and print each one

if type(output) == list:
    for item in output:
        print('- ' + item)
else:
    print(output)
