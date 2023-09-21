import numpy as np
import time
import json

""""
Easy Logic flow chart at speed typing...

"""


username = str(input("Input Username : "))


file_path = 'text_list.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    print(json.dumps(data, indent=4)) 