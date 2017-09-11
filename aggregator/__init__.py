from categorical import agg_by_categories
from numeric import range_groups
from timeseries import agg_by_date, agg_by_category_by_date

class AggregateByCategory():
    def fit(self, intype, data):
        pass

    def transform(self, data=None, values=[], groupby=[], aggregation=None):
        return agg_by_categories(data, groupby, values, agg=aggregation)

class AggregateByDateTime():
    def fit(self, intype, data):
        pass

    def transform(self, data=None, values=[], datetime=None, intervals=None, 
                    aggregation=None):
        return agg_by_date(data, datetime, values, intervals=intervals, agg=aggregation)

class AggregateByDateTimeCategory():
    def fit(self, intype, data):
        pass

    def transform(self, data=None, values=[], groupby=[], datetime=None, intervals=None, 
                    aggregation=None):
        return agg_by_category_by_date(data, datetime, values, groupby, intervals=intervals, 
                            agg=aggregation)

class AggregateByNumericRange():
    def fit(self, intype, data):
        pass

    def transform(self, data=None, values=[]):
        return range_groups(data, values)