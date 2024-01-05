  def is_odd(n):
        return n % 2 != 0
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)