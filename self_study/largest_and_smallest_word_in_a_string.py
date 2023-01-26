user_string = str(input("Enter a sentence: "))
words = user_string.split(" ")
smallest = words[0]
largest = words[0]

for i in range(1, len(words)):
    if len(words[i]) < len(smallest):
        smallest = words[i]
    if len(words[i]) > len(largest):
        largest = words[i]

print("The smallest word is", smallest)
print("The largest word is", largest)
