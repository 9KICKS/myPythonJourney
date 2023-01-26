word = "Hello boss baby"

#for i in word:
#   if i != "b":
#      print(1, end="")


#for i in range(len(word)):
#    if word[i] == "b":
#        print(word[i])

for i, value in enumerate(word):
    if value == "b":
        print(value, " : ", i)

for i, value in enumerate(word):
    if value != "b":
        print(value, end="")
