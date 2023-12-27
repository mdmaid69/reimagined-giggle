import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal