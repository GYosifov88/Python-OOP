class reverse_iter:
    def __init__(self, obj):
        self.obj = list(obj)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.obj):
            raise StopIteration
        value_to_return = self.obj[self.index]
        self.index -= 1
        return value_to_return

    
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
