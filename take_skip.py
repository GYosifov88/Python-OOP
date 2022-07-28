class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.count:
            raise StopIteration
        value_to_return = self.start
        self.start += self.step
        self.counter += 1
        return value_to_return


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
