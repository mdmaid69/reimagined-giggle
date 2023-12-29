import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import datetime
def get_current_date():
        return datetime.date.today()