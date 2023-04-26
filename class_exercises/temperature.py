user_temperature = int(input("What is the temperature outside? "))
if 1 <= user_temperature <= 20:
    print("It's cold outside, I suggest you stay indoors.")
elif user_temperature <= 0:
    print("I suggest you take a hot bath cause it's freezing.")
else:
    print("It's a warm day, I suggest you hit the beach.")
