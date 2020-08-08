import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)


def translate(results, w):
    w = w.lower()
    print("hello0")
    if w in data:
        print("hello1")
        return data[w]
        print("hello2")
    elif w.title() in data:  # If user entered "texas" this will check for "Texas" as well.
        print("hello3")
        return data[w.title()]
        print("hello4")
    elif w.upper() in data:  # In case user enters words like USA or NATO
        print("hello5")
        return data[w.upper()]
        print("hello6")
    elif len(get_close_matches(w, data.keys())) > 0:
        print("hello7")
        yn = input("Did you mean %s? Enter Y if yes and N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            print("hello8")
            return data[get_close_matches(w, data.keys())[0]]
            print("hello9")
        elif yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
            print("hello10")
        elif yn == "N":
            print("hello11")
            return "The word doesn't exist. Please double check it."
            print("hello11")
        elif yn == "n":
            print("hello12")
            return "The word doesn't exist. Please double check it."
        else:
            print("hello13")
            return "We didn't understand your entry."
    else:
        print("hello14")
        return "That word doesn't exist. Please check your spelling."


cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

print(results)
print(w)

if results:
    for result in results:
        print(result[1])
        
output = translate(results, word)

if type (output) == list:
    for item in output:
        print(item)

else:
    print(output)