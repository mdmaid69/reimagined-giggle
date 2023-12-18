def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def remove_duplicates(lst):
        return list(set(lst))