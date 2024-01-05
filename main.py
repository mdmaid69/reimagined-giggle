def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)