print("Enter an integer, the input ends if it is 0: ", end='')
lst = []
user_input = 1
while user_input != 0:
    user_input = float(input())
    if user_input != 0:
        lst.append(user_input)

positives = 0
negatives = 0
total = 0
average = 0

for number in lst:
    total += number
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
average = total/len(lst)

print("The number of positives is ", positives)
print("The number of negatives is ", negatives)
print("The total is ", total)
print("The average is ", average)
