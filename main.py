def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time