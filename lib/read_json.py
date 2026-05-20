import json
def rjson(file):
 with open (file, 'r') as ff:
  data = json.load(ff)
  return data