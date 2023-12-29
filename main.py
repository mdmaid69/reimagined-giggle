numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a