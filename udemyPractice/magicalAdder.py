values = input("Please enter three comma seperated values: ")

values = values.split(",")

for i in range(0, 3):
    values[i] = int(values[i])

result = values[0] + values[1] - values[2]

print(result)