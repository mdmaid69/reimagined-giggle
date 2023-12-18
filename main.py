  def calculate_area_rectangle(l, w):
        return l * w
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)