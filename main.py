def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)