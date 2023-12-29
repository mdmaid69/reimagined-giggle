n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True