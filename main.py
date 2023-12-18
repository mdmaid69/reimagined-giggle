import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue