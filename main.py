  def square_number(x):
        return x**2
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)