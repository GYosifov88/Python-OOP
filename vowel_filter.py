from functools import wraps


def vowel_filter(function):
    vowels = 'aeouiy'
    @wraps(function)
    def wrapper():
        result = function()
        filtered = [c for c in result if c.lower() in vowels]
        return filtered
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
