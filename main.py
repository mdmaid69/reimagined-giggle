import datetime
def get_current_date():
        return datetime.date.today()
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a