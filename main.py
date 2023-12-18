import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)