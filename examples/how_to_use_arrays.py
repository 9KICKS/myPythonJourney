from array import *

x = array('i', [1, 2, 3, 4, 5])
print(x)

print()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
print(numbers[3:8:2])

print()

sentences = ["Obi is a boy", "Ada is a girl", "Tommy is a dog"]
print(sentences[0])
print(sentences[0][0:3])

print()

numbers.append("Folahan")
numbers.insert(4, "Joshua")
print(numbers)

print()

import numpy as np

x = np.array([2, 4, 6, 8, 10, 12])
print(x / 2)

# or

print()

new = []
y = [2, 4, 6, 8, 10, 12]
for value in y:
    new.append(value / 2)
print(new)

# .clear() - to clear the contents of the list
# .copy - to copy contents from one array to another
# .count - to count how many times an element appears in a list
# set takes in unique values, it doesn't take same values
