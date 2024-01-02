import json
print(json.dumps({"name": "John", "age": 30}))
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)