import json
print(json.dumps({"name": "John", "age": 30}))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)