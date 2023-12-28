def calculate_volume(length, width, height):
        return length * width * height
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))