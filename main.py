  def calculate_area_triangle(b, h):
        return 0.5 * b * h
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)