import array
def get_list_from_array(array):
        return array.tolist()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])