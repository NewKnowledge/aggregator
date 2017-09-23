import pandas as pd
import numpy as np

def agg_by_categories(df, category_headers, number_headers, agg='mean'):

    all_headers = number_headers + category_headers

    temp_grouped = df[all_headers].groupby(category_headers)
    grouped = getattr(temp_grouped,agg)().reset_index()

    categories = {}
    numbers = {}

    for category_header in category_headers:
        categories[category_header] = grouped[category_header].values

    for number_header in number_headers:
        numbers[number_header] = grouped[number_header].values

    output = np.array([
        categories,
        numbers
    ],dtype='O')
    
    # output results
    return output