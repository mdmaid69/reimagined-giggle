def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  def reverse_list(lst):
        return lst[::-1]