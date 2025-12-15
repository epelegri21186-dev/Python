import json
with open('ex2.json', 'r') as f:
    dades = json.load(f)
    dades['colors']=['blanc','negre','groc']
    print(dades)
    json.dump(dades,f)
with open('ex2.json', 'w') as f:
    dades['colors']=['blanc','negre','groc']
    json.dump(dades,f)