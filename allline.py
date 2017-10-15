import json
fo = open("alline.json")

alltext = fo.read()

fo.close()

allLine = json.loads(alltext)

print allLine

