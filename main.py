import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets