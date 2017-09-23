import pandas as pd
import numpy as np

def range_groups(df, number_headers, bins=None):
    max_bins = 20

    df_desc = df[number_headers].describe().reset_index()
    df_nums = df[number_headers]
    df_nums = df_nums.dropna()

    if not bins:
        lowest_min_header = None
        lowest_min_value = None
        highest_max_header = None
        highest_max_value = None

        for number_header in number_headers:
            min_val = df_desc.loc[df_desc['index'] == 'min'][number_header].values[0]
            max_val = df_desc.loc[df_desc['index'] == 'max'][number_header].values[0]

            if not lowest_min_value or min_val < lowest_min_value:
                lowest_min_header = number_header
                lowest_min_value = min_val

            if not highest_max_value or max_val > highest_max_value:
                highest_max_header = number_header
                highest_max_value = max_val

        high_low = np.concatenate([df_nums[lowest_min_header].values,df_nums[highest_max_header].values])
        high_low = high_low[~np.isnan(high_low)]
        counts,bins = np.histogram(high_low,bins='auto')

        if len(counts) > max_bins:
            bins = max_bins

    ys = {}
    x_values = None
    for number_header in number_headers:
        count,division = np.histogram(df_nums[number_header].values,bins=bins)

        if not x_values:
            x_values = []
            for i,d in enumerate(division):
                if i == len(division) - 1:
                    break

                x_values.append('{0:.2f}'.format(d) + u' to ' + '{0:.2f}'.format(division[i+1]))

        y_values = list(count)
        ys[number_header] = y_values

    output = np.array([
        x_values,
        y_values
    ],dtype='O')
    
    return output
