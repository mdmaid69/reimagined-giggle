def calculate_area_rectangle(l, w):
        return l * w
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)