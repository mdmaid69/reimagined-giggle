import array
def iterate_over_array(array):
        for item in array:
        print(item)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)