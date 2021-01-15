"""
this application provide the definition of different words in english
it's a kind of dictionary, this is the first version (terminal mode).
next i will try to add graphical interface and database acess
"""
import json
from difflib import get_close_matches


data = json.load(open("data/data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        matches = get_close_matches(w, data.keys())
        if(len(matches) > 0):
            response = input("did you mean {} instead y for yes and n for no"
                             .format(matches[0]))
            if(response == "y"):
                return data[matches[0]]
            elif(response == "N"):
                return "the word does'nt exist"
            else:
                return "we didn't understand the entry"
    return "The word doesn't exist. Please check it."


word = input("enter a word: ")

outpout = translate(word)

if type(outpout) == list:
    for translation in outpout:
        print(translation)
else:
    print(outpout)
