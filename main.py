import array
def pop_from_array(array, i=-1):
        return array.pop(i)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])