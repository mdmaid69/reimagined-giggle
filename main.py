import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import logging
def setup_logging(level):
        logging.basicConfig(level=level)