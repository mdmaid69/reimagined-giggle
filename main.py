def calculate_average(lst):
        return sum(lst) / len(lst)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)