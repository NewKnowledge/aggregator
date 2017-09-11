import pandas as pd

from aggregator import (AggregateByCategory, AggregateByDateTime, 
                            AggregateByDateTimeCategory, AggregateByNumericRange)


def test_api():
    df = pd.read_csv('tests/data/trainData.csv')

    abc = AggregateByCategory()
    abc.fit(None, df)
    abc.transform(data=df, values=['At_bats','Runs'], groupby=['Position'], 
                    aggregation='mean')

    abdt = AggregateByDateTime()
    abdt.fit(None, df)
    abdt.transform(data=df, datetime='datetime', intervals=['year'], 
                    values=['At_bats','Runs'], aggregation='mean')

    abdtc = AggregateByDateTimeCategory()
    abdtc.fit(None, df)
    abdtc.transform(data=df, datetime='datetime', intervals=['year'], 
                    values=['At_bats','Runs'], groupby=['Position'], 
                    aggregation='mean')

    abn = AggregateByNumericRange()
    abn.fit(None, df)
    abn.transform(data=df, values=['At_bats','Runs'])