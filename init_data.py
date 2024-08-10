import json
import os

data = {
    "personas": [],
    "gastos": []
}

if not os.path.exists('data'):
    os.makedirs('data')

with open('data/gastos.json', 'w') as f:
    json.dump(data, f, indent=4)
