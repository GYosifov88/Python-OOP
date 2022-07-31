def store_result(func):
    def wrapper(*args):
        result = func(*args)
        with open('./results.txt', 'a') as file:
            file.write(f"Function '{func.__name__}' was called. Result: {result}")
            file.write('\n')
        return result
    return wrapper


@store_result
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))


@store_result
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))


@store_result
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())
