import array
def iterate_over_array(array):
        for item in array:
        print(item)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])