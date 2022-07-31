from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        # result = func(*args)
        end = time()
        # Вариант е да връщаме резултата от функцията, а времето да пазим
        # във файл, функцията я изпълнява в резулт който връщаме:
        # with open ('./result.txt', 'a') as file:
        #     file.write(f'{func.__name__} was called with {args}. Elapsed: {end-start}')
        # return result
        return end - start
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total

print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result

print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1

print(loop())

