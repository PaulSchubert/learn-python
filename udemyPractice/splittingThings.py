panagram = """The quick brown 
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9, 223, 372, 036, 854, 775, 807"
print(numbers.split(","))


#replaceing values in place (string to int)
for index in range(len(stringArray)):
    stringArray[index] = int(stringArray[index])
print(stringArray)

#second method, creating a new list and appending
for value in stringArray:
    intArray.append(int(value))
print(intArray)
