from pandas.testing import assert_frame_equal
import pandas as pd

from sparkmagic.utils.utils import coerce_pandas_df_to_numeric_datetime


def test_no_coercing():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': u'random', u'temp_diff': u'0adsf'}]
    desired_df = pd.DataFrame(records)

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_date_coercing():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': u'6/1/13', u'temp_diff': u'0adsf'}]
    desired_df = pd.DataFrame(records)
    desired_df["date"] = pd.to_datetime(desired_df["date"])

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_date_coercing_none_values():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': None, u'temp_diff': u'0adsf'}]
    desired_df = pd.DataFrame(records)
    desired_df["date"] = pd.to_datetime(desired_df["date"])

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_date_none_values_and_no_coercing():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': None, u'temp_diff': u'0adsf'},
               {u'buildingID': 1, u'date': u'adsf', u'temp_diff': u'0adsf'}]
    desired_df = pd.DataFrame(records)

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_numeric_coercing():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': u'adsf', u'temp_diff': u'0'}]
    desired_df = pd.DataFrame(records)
    desired_df["temp_diff"] = pd.to_numeric(desired_df["temp_diff"])

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_numeric_coercing_none_values():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': u'asdf', u'temp_diff': None}]
    desired_df = pd.DataFrame(records)
    desired_df["temp_diff"] = pd.to_numeric(desired_df["temp_diff"])

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_numeric_none_values_and_no_coercing():
    records = [{u'buildingID': 0, u'date': u'6/1/13', u'temp_diff': u'12'},
               {u'buildingID': 1, u'date': u'asdf', u'temp_diff': None},
               {u'buildingID': 1, u'date': u'adsf', u'temp_diff': u'0asdf'}]
    desired_df = pd.DataFrame(records)

    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)

    assert_frame_equal(desired_df, df)


def test_df_dict_does_not_throw():
    json_str = """
[{
    "id": 580320,
    "name": "COUSIN'S GRILL",
    "results": "Fail",
    "violations": "37. TOILET area.",
    "words": ["37.",
    "toilet",
    "area."],
    "features": {
        "type": 0,
        "size": 262144,
        "indices": [0,
        45,
        97],
        "values": [7.0,
        5.0,
        1.0]
    },
    "rawPrediction": {
        "type": 1,
        "values": [3.640841752791392,
        -3.640841752791392]
    },
    "probability": {
        "type": 1,
        "values": [0.974440185187647,
        0.025559814812352966]
    },
    "prediction": 0.0
}]
"""
    df = pd.read_json(json_str)
    coerce_pandas_df_to_numeric_datetime(df)


def test_overflow_coercing():
    records = [{'_c0':'12345678901'}]
    desired_df = pd.DataFrame(records)
    desired_df['_c0'] = pd.to_numeric(desired_df['_c0'])
    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)
    assert_frame_equal(desired_df, df)
    

def test_all_null_columns():
    records = [{'_c0':'12345', 'nulla': None}, {'_c0':'12345', 'nulla': None}]
    desired_df = pd.DataFrame(records)
    desired_df['_c0'] = pd.to_numeric(desired_df['_c0'])
    df = pd.DataFrame(records)
    coerce_pandas_df_to_numeric_datetime(df)
    assert_frame_equal(desired_df, df)
