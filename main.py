def find_difference(list1, list2):
        return set(list1) - set(list2)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)