class MyClass:
    def __init__(self, edate=None, fdate=""):
        if edate:
            print("Constructors", edate)
        else:
            print("Default Constructor")


obj1 = MyClass("01-Dec-2021")

obj2 = MyClass()
