def reverse_list(lst):
        return lst[::-1]
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)