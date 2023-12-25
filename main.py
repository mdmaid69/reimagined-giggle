def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import datetime
def get_current_date():
        return datetime.date.today()