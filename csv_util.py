import csv


def generate_sanitized_csv(source_filename, dest_filename, columns_to_keep):
    with open(source_filename) as input_csv, open(dest_filename, 'w') as output_csv:
        read_csv = csv.reader(input_csv)
        write_csv = csv.writer(output_csv)

        for row in read_csv:
            cols = [row[i] for i in columns_to_keep]
            # Write row if all columns are non-null
            if all(c for c in cols):
                write_csv.writerow(cols)


def generate_categorical_columns(filename, categorical_columns):
    with open(filename) as input_csv:
        read_csv = csv.reader(input_csv)

        # Skip header
        print(next(read_csv))

        output = [set() for col in range(3)]

        for row in read_csv:
            for arr_idx, col_idx in enumerate(categorical_columns):
                output[arr_idx].add(row[col_idx])

        print(output)


def run_all():
    original_header = ['unit_id', 'street_address', 'city', 'state', 'postal_code', 'neighborhood', 'location_x', 'location_y', 'cross_street_a', 'cross_street_b', 'floor', 'price', 'months_free_incentive_advertised', 'incentives_and_or', 'broker_incentive_type',
                       'broker_incentive_quantity', 'listed_at', 'rented_at', 'layout', 'bathrooms', 'square_footage', 'date_available', 'min_lease_term', 'max_lease_term', 'pet_policy', 'unit_amenities', 'building_amenities', 'unit_description', 'photos', 'floorplans']

    # Customizable
    desired_header = ['neighborhood', 'price', 'layout', 'bathrooms', 'square_footage']
    desired_columns = [original_header.index(h) for h in desired_header]

    # Customizable
    categorical_columns = [desired_header.index('neighborhood'),
                           desired_header.index('layout'),
                           desired_header.index('bathrooms')]

    generate_sanitized_csv('./datasets/historical_rentals.csv',
                           './datasets/hr_sanitized.csv',
                           desired_columns)

    generate_categorical_columns('./datasets/hr_sanitized.csv',
                                 categorical_columns)

run_all()
