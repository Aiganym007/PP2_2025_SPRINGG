import json
with open(r"C:\Users\Gulistan\Desktop\PP2_2025_SPRING\example.json", "r") as file:
    data = json.load(file)
data["price"] = 900

with open(r'C:\Users\Gulistan\Desktop\PP2_2025_SPRING\example.json', 'w') as file:
    json.dump(data, file, indent=4)
