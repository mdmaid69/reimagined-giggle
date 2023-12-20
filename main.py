import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_perpetuity(payment, rate):
        return payment / rate