def calculate_area_circle(r):
        return 3.14 * r**2
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)