import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)