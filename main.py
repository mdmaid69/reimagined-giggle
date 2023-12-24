def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)