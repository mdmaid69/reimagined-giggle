import array
def pop_from_array(array, i=-1):
        return array.pop(i)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])