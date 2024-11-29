pythonInt = 50
pythonStr = 'A big dog'
pythonFloat = 2.31
pythonBool = True
pythonNone = None
pythonHash = {'Daddy': 'Jason', 'Mommy': 'Ayami', 'Kid': 'Sean'}
pythonArray = ['Sturge', 27, 5.55, 'Rain']

import json
jsonInt = json.dumps(pythonInt)
jsonStr = json.dumps(pythonStr)
jsonFloat = json.dumps(pythonFloat)
jsonBool = json.dumps(pythonBool)
jsonNone = json.dumps(pythonNone)
jsonHash = json.dumps(pythonHash)
jsonArray = json.dumps(pythonArray)

print(jsonInt)
print(jsonStr)
print(jsonFloat)
print(jsonBool)
print(jsonNone)
print(jsonHash)
print(jsonArray)

print(type(jsonInt))
print(type(jsonFloat))
print(type(jsonHash))
