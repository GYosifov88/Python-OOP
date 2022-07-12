def print_row(size, stars):
    for row in range(size - stars):
        print(" ", end='')
    for row in range(1, stars):
        print("*", end=' ')
    print('*')

size = int(input())

for stars in range(1, size):
    print_row(size, stars)
for stars in range(size, 0, -1):
    print_row(size, stars)