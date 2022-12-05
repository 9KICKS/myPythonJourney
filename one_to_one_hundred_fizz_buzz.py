for count in range(100):
    count += 1
    if count % 15 == 0:
        print("fizz buzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)
