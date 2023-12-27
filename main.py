n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a