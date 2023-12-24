  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)