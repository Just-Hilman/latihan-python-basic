# Iterating list
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total character: {}, Average character: {}".format(chars, chars/len(animals)))

# Enumerate list
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))


# Enumerate skip lists
def skip_elements(elements):
	# code goes here
	new_element = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_element.append(element)
	return new_element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']