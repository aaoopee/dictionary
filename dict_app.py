
import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))

def translate(key):
    lc_key = key.lower()

    if lc_key in data:
        return data[lc_key]
    else:
        closest = get_close_matches(lc_key, data.keys())
        if len(closest) > 0:
            yn = input("Did uyou mean \"%s\" instead (Y for yes, N if no)?" %closest[0])
            yn = yn.lower()
            if (yn == "y"):
                return data[closest[0]]
            else:
                return "Word \"%s\" not recognized." % key
        else:
            return "Word \"%s\" not recognized." % key

result = translate(input("Word: "))

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
