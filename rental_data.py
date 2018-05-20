import numpy as np
import pandas as pd
import tensorflow as tf
import dateutil

dtypes = {
    'unit_id': np.int32,  # 0
    'street_address': str,
    'city': str,
    'state': str,
    'postal_code': str,  # 4
    'neighborhood': str,  # 5
    'location_x': np.float32,  # 6
    'location_y': np.float32,  # 7
    'cross_street_a': str,
    'cross_street_b': str,
    'floor': np.int32,  # 10
    'price': np.float32,  # 11
    'months_free_incentive_advertised': np.int32,
    'incentives_and_or': str,
    'broker_incentive_type': str,
    'broker_incentive_quantity': np.int32,
    'listed_at': str,  # 16
    'rented_at': str,  # 17
    'layout': str,  # 18
    'bathrooms': str,  # 19
    'square_footage': np.int32,  # 20
    'date_available': str,
    'min_lease_term': np.int32,  # 22
    'max_lease_term': np.int32,  # 23
    'pet_policy': str,  # 24
    'unit_amenities': str,
    'building_amenities': str,
    'unit_description': str,
    'photos': str,
    'floorplans': str
}


def raw_dataframe():
    df = pd.read_csv('historical_rentals.csv',
                     dtype=dtypes,
                     date_parser=dateutil.parser.parser,
                     usecols=[5, 7, 11, 17, 18, 24])

    return df


def load_data(y_name="price", train_fraction=0.7, seed=None):
    data = raw_dataframe()

    # Drop rows with any missing data
    data = data.dropna()

    # Shuffle the data
    np.random.seed(seed)

    # Allocate a random portion (70%) of all data to training set, with rest going to test set
    x_train = data.sample(frac=train_fraction, random_state=seed)
    # index = row number
    x_test = data.drop(x_train.index)

    # Extract the label from the features DataFrame.
    y_train = x_train.pop(y_name)
    y_test = x_test.pop(y_name)

    # x_train = features, y_train = price
    return (x_train, y_train), (x_test, y_test)


load_data()
