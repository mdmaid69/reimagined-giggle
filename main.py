n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps