#name = "Folahan"
#age = 21.7658

#bio = "{} is {} years old".format(name, age)
#bio = "{1} is {0} years old".format(age, name)
#bio = "{0} is {1} years old, and {0} loves {2}".format(name, age, "Java")
#bio = "{0:>20} is {1} years old, and {0} loves {2}".format(name, age, "Java")
#bio = "{0:^20} is {1:>10.2f} years old, and {0} loves {2}".format(name, age, "Java")
#bio = f"{name:^20} is {age:>10.2f} years old, and {name} loves {'Java'}"
#bio = f"{name:=*^20} is {age:>10.2f} years old, and {name} loves {'Java'}"
#print(bio)


#hello = "hello world"
#for i in hello:
    #print(i)

#hello = "hello world"
#for index, letter in enumerate(hello):
    #print(f"{letter} --> {index}")

#hello = "hello world"
#for index in range(len(hello)):
    #print(f"{hello[index]} --> {index}")

for i in range(1, 21, 2):
    s = "*" * i
    print(f"{s:20}{s:^20}{s:^20}")

