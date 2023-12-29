import datetime
def get_current_date():
        return datetime.date.today()
def calculate_roi(gain, cost):
        return (gain - cost) / cost