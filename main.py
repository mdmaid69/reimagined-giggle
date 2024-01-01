def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
  def calculate_area_triangle(b, h):
        return 0.5 * b * h