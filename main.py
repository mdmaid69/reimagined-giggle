import array
def clear_array(array):
        array *= 0
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])