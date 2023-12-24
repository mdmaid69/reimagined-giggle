import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)