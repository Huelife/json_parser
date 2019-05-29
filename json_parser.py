#json_parser.py: Simple JSON parser

import json

with open('dataMay-28-2019.json', 'r') as jsonfile:
  data_dict = json.load(jsonfile)
  print(json.dumps(data_dict,indent=2,sort_keys=True))
