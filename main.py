def calculate_average(lst):
        return sum(lst) / len(lst)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)