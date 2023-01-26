hello = "Hello there!!!"

found = 0
while True:
    found = hello.find("e", found)
    if found == -1:
        break
    print(found)

    found += 1

#print(hello.find("l"))
#print(hello.rfind("e"))

# print(hello.upper())
# print(hello.lower())
# print(hello.title())
# print(hello.capitalize())
# print(hello.casefold())
# print(hello.swapcase())

#print(hello.lower().count("e"))
#print(hello.center(20, "*"))
#print(hello.ljust(20, "*"))
#print(hello.rjust(20, "*"))

#print(hello.endswith("!!!"))
#print(hello.replace("l", "q", 1))
#print(hello.lstrip())
#print(hello.zfill(20))
#print(hello.split("e"))
#print(hello.partition("e"))
#print(hello.rpartition("e"))
#print("-".join(["a", "b", "c"]))

#bin_ = "10110001100101111078"
#print(bin_.replace("1", "x").replace("0", "1").replace("x", "0"))
#print(bin_.translate(str.maketrans("01", "10")))
#print(bin_.translate(str.maketrans("01", "10", "8")))
