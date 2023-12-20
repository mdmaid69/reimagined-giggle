n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps