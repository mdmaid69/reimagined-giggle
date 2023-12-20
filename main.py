text = "Hello, world!"
print("Words:", len(text.split()))
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a