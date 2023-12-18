import array
def pop_from_array(array, i=-1):
        return array.pop(i)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))