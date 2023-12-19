import array
def iterate_over_array(array):
        for item in array:
        print(item)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])