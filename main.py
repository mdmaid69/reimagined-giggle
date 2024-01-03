def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)