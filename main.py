def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
import os
def get_environment_variable(var):
        return os.getenv(var)