def get_primes(nums):
    for num in nums:
        is_number_prime = True
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    is_number_prime = False
            if is_number_prime:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))


# Вариант с допълнителна функция за изчисляване дали е прайм или не
# def is_prime(number):
#     if number <= 1:
#         return False
#     result = True
#     for i in range(2, number):
#         if number % i == 0:
#             result = False
#             break
#     return result
#
# def get_primes(nums):
#     for num in nums:
#         if is_prime(num):
#             yield num
#
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))