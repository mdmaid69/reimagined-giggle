def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  def calculate_area_triangle(b, h):
        return 0.5 * b * h