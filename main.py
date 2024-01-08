  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)