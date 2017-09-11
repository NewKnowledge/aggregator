import pandas as pd
from definitions import NUMBERS

interval_to_pd = {
    'year': 'A',
    'month': 'M',
    'week': 'W',
    'day': 'D',
    'hour': 'H',
    'minute': 'T',
    'second': 'S'
}

def best_intervals(start_date, end_date):
    try:
        delta = pd.to_datetime(end_date, coerce=True) - pd.to_datetime(start_date, coerce=True)
        days = delta.days
    except:
        return ['year']
    
    intervals = []
    if days > 356 * 3:
        intervals.append('year')
    if days > 90 and days < 365 * 20:
        intervals.append('month')

    if days > 21 and days < 365 * 5:
        intervals.append('week')
        
    if days > 3 and days < 365 * 2:
        intervals.append('day')
    
    if days <=3:
        seconds = delta.seconds
        if seconds // 3600 >= 3:
            intervals.append('hour')
        if seconds // 60 % 60 >= 3 and seconds // 60 % 60 < 300:
            intervals.append('minute')
        if seconds < 300:
            intervals.append('second')

    return intervals


def agg_by_date(df, datetime_header, number_headers, intervals=None, agg='mean'):
    if agg not in ['mean', 'sum']:
        return None

    df = df[pd.notnull(df[datetime_header])]
    
    dates = pd.to_datetime(df[datetime_header],infer_datetime_format=True)
    indexed = df.set_index(pd.DatetimeIndex(dates))
    series = indexed[number_headers]

    last = df[datetime_header].max()
    first = df[datetime_header].min()

    x_values = {}
    y_values = {}
    
    if intervals:
        has_intervals = True
    else:
        has_intervals = False
        intervals = best_intervals(first,last)

    for interval in intervals:
        grouped = series.groupby(pd.TimeGrouper(freq=interval_to_pd[interval]))
        df_grouped_by_date = getattr(grouped,agg)().reset_index()

        x_values[interval] = df_grouped_by_date[datetime_header].dt.strftime('%Y-%m-%d %H:%M:%S').values
        y_values[interval] = {}
        for number_header in number_headers:
            y_values[interval][number_header] = df_grouped_by_date[number_header].values
        
    output = {
        'datetimes': x_values,
        'aggregated_values': y_values,
        'intervals': intervals
    }
    
    # output results
    return output


def agg_by_category_by_date(df, datetime_header, number_headers, category_headers, 
                                    intervals=None, agg='mean'):
    

    all_column_headers = category_headers + number_headers

    df = df[pd.notnull(df[datetime_header])]

    indexed = df.set_index(pd.DatetimeIndex(df[datetime_header]))
    
    x_values = {}
    y_values = {}
    z_values = {}
    
    last = df[datetime_header].max()
    first = df[datetime_header].min()

    if intervals:
        has_intervals = True
    else:
        has_intervals = False
        intervals = best_intervals(first,last)

    for interval in intervals:
        grouper = pd.TimeGrouper(freq=interval_to_pd[interval])
        grouped = indexed[all_column_headers].groupby([grouper] + category_headers)
        df_grouped_by_date = getattr(grouped,agg)().reset_index()

        x_values[interval] = df_grouped_by_date[datetime_header].dt.strftime('%Y-%m-%d %H:%M:%S').values

        for number_header in number_headers:
            if interval not in y_values:
                y_values[interval] = {}
            y_values[interval][number_header] = df_grouped_by_date[number_header].values

        for category_header in category_headers:
            if interval not in z_values:
                z_values[interval] = {}
            z_values[interval][category_header] = df_grouped_by_date[category_header].values

    output = {
        'datetimes': x_values,
        'aggregated_values': y_values,
        'category_labels': z_values,
        'intervals': intervals
    }
    
    # output results
    return output
