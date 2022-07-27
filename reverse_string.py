def reverse_text(text):
    reversed_text = [str(x) for x in reversed(text)]
    index = 0
    while index < len(reversed_text):
        yield reversed_text[index]
        index += 1


for char in reverse_text("step"):
    print(char, end='')
