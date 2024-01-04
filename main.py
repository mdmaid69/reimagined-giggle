  def convert_to_binary(n):
        return bin(n)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)