def calculate_roi(gain, cost):
        return (gain - cost) / cost
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time