numbers = list(range(2, 101))

print(numbers, "\n")

for element in numbers:
    if element > 2 and element % 2 == 0:
        numbers.remove(element)

for element in numbers:
    if element > 3 and element % 3 == 0:
        numbers.remove(element)

for element in numbers:
    if element > 5 and element % 5 == 0:
        numbers.remove(element)

for element in numbers:
    if element > 7 and element % 7 == 0:
        numbers.remove(element)

print(numbers)
