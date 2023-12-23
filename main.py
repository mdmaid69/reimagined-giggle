def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import datetime
def get_today_date():
        return datetime.date.today()