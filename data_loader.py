import pandas as pd

def load_and_clean_data(filepath):
    # Load CSV
    df = pd.read_csv(filepath)

    # Columns where zero means missing data
    cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

    # Replace zeros with median
    for col in cols_with_zeros:
        median = df[col].median()
        df[col] = df[col].replace(0, median)

    return df






