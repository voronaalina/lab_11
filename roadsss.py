import json

with open('c://lab11//roads.json', 'r') as json_file:
    roads_data = json.load(json_file)

total_length = sum(roads_data.values())
average_length = total_length / len(roads_data)

print("Середня довжина доріг: ", average_length , " km")
print("Дороги з меншою довжиною ніж середня: ")
for road, length in roads_data.items(): 
    if length < average_length:
        print(road + ":" + str(length) + " km")
