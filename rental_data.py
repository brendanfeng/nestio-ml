import numpy as np
import pandas as pd
import tensorflow as tf
import dateutil
import string

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


def convNa(val):
    if val is None or val == '':
        return '?'
    return val


def convFloor(floor):
    if floor != '?':
        floor = floor.replace(string.ascii_letters, '')
    return floor


def raw_dataframe():
    df = pd.read_csv('./datasets/hr_sanitized.csv',
                     dtype=dtypes,
                     date_parser=dateutil.parser.parser,
                     parse_dates=True,
                     na_values='?',
                     #  converters={'floor': convNa,
                     #              'price': convNa,
                     #              'square_footage': convNa},
                     #  usecols=[5, 10, 11, 16, 17, 18, 20, 24])
                     )

    return df


def load_data(y_name="price", train_fraction=0.7, seed=None):
    data = raw_dataframe()

    # Drop rows with any missing data
    # data = data.dropna()

    # Shuffle the data
    np.random.seed(seed)

    # Randomly allocate a portion (70%) of all data to training set, with the rest going to test set
    x_train = data.sample(frac=train_fraction, random_state=seed)

    # index = internal row number
    x_test = data.drop(x_train.index)

    # Remove prices from the features DataFrames.
    y_train = x_train.pop(y_name)
    y_test = x_test.pop(y_name)

    # x_train = features [training], y_train = price [training]
    # x_test  = features [test]    , y_test  = price [test]
    return (x_train, y_train), (x_test, y_test)


def features_columns():
    neighborhood = tf.feature_column.categorical_column_with_hash_bucket('neighborhood',
                                                                         200)

    layout = tf.feature_column.categorical_column_with_vocabulary_list('layout',
                                                                       vocabulary_list=['Flex 2',
                                                                                        '1 Bedroom w/ HO',
                                                                                        '3 Bedroom',
                                                                                        '1 Bedroom',
                                                                                        '6+ Bedroom',
                                                                                        'Jr 1 Bedroom',
                                                                                        '5 Bedroom',
                                                                                        'Flex 3',
                                                                                        'Flex 4',
                                                                                        'Building',
                                                                                        '4 Bedroom w/ HO',
                                                                                        '3 Bedroomw/ HO',
                                                                                        'Studio',
                                                                                        '2 Bedroom w/ HO',
                                                                                        'Loft',
                                                                                        'Alcove Studio',
                                                                                        'Jr 4',
                                                                                        '4 Bedroom',
                                                                                        '2 Bedroom'])
    bathrooms = tf.feature_column.categorical_column_with_vocabulary_list('bathrooms',
                                                                          vocabulary_list=['2 Bathroom',
                                                                                           '1.5 Bathroom',
                                                                                           '4 Bathroom',
                                                                                           '3.5 Bathroom',
                                                                                           '3 Bathroom',
                                                                                           '1 Bathroom',
                                                                                           '4.5 Bathroom',
                                                                                           '2.5 Bathroom'])

    feature_columns = [
        tf.feature_column.embedding_column(neighborhood, 3),
        tf.feature_column.indicator_column(layout),
        tf.feature_column.indicator_column(bathrooms),
        tf.feature_column.numeric_column('square_footage'),
    ]

    return feature_columns
