class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = ['a', 'o', 'e', 'i', 'u', 'y', 'A', 'O', 'E', 'I', 'U', 'Y']
        self.final_text = [x for x in self.text if x in self.vowels]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.final_text) - 1:
            raise StopIteration
        value_to_return = self.final_text[self.index]
        self.index += 1
        return value_to_return

    # def iter_with_gen(self):
    #     return (x for x in self.text if x in self.vowels)
# С генератор става доста по бързо и по-малко код

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# for char in my_string.iter_with_gen():
#     print(char)
