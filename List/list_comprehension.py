# Print length list
languanges = ["Python", "Java", "Javascript"]
lengths = [len(languange) for languange in languanges]
print(lengths)

# Print kelipatan 3
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# Print kelipatan 2 ganjil
def odd_numbers(n):
	return [x for x in range(1, n + 1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []