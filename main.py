def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c