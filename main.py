i = 0
while i < 5:
        print(i)
        i += 1
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a