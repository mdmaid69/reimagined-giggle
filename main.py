sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a