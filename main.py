  def convert_to_hex(n):
        return hex(n)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)