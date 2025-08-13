#
# Author: Rohtash Lakra
#
from configs.base import ROOT_DIR
from core.io.base import read_json_file

fileName = "orders.json"
orders = read_json_file(f"{ROOT_DIR}/data/{fileName}")

sort_by_age = lambda x: x['age']
results = list(filter(sort_by_age, orders))
print(results)
