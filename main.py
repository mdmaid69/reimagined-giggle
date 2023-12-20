def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r