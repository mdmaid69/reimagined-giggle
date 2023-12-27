import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def reverse_list(lst):
        return lst[::-1]