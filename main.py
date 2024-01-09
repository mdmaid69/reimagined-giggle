import array
def get_array_slice(array, i, j):
        return array[i:j]
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])