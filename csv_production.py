import csv
import sys

file_name="c://lab11//data.csv"
fd = open(file_name, "r")
reader = csv.reader(fd, delimiter=':')
production_data = []

for row in reader:
    day = int(row[0].strip())
    production_number = int(row[1].strip())
    production_data.append((day, production_number))
fd.close()

min_production = min(production_number for day, production_number in production_data)
print("Мінімальний випуск продукції: ", min_production)
print("Дні з максимальним випуском продукції: " )
for day, production_number in production_data:
    if production_number == min_production:
        print("День ", day)
        