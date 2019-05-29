#json_parser.py: Simple JSON parser

import json

#user inputs .json file then it is loaded and displayed on the console
with open(input('.json file name: '), 'r') as jsonfile:
  data_dict = json.load(jsonfile)
  print(json.dumps(data_dict,indent=2,sort_keys=True))
