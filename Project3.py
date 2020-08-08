import json
from difflib import get_close_matches

# Loading Data into a Python data type.
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # If user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:  # In case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes and N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "That word doesn't exist. Please check your spelling."


# User input.
word = input("Enter word: ")

output = translate(word)

if type (output) == list:
    for item in output:
        print(item)

else:
    print(output)