import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a