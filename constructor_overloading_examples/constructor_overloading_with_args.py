class Example:

    def __init__(self, *args):
        if len(args) > 1:
            self.answer = 0
            for i in args:
                self.answer += i

        elif isinstance(args[0], int):
            self.answer = args[0] * args[0]

        elif isinstance(args[0], str):
            self.answer = "Hello! " + args[0] + "."


example1 = Example(1, 2, 3, 6, 8)
print("Sum:", example1.answer)

example2 = Example(6)
print("Square:", example2.answer)

example3 = Example("Python")
print("String:", example3.answer)
