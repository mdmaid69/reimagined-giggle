import collections
def create_user_string():
        return collections.UserString()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)