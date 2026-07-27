import pandas as pd

class DataCleaner:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def clean_data(self):

        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Remove spaces in column names
        self.df.columns = self.df.columns.str.strip()

        # Fill missing numeric values
        numeric_cols = self.df.select_dtypes(include='number').columns

        for col in numeric_cols:
            self.df[col] = self.df[col].fillna(self.df[col].mean())

        # Fill missing text values
        object_cols = self.df.select_dtypes(include='object').columns

        for col in object_cols:
            self.df[col] = self.df[col].fillna("Unknown")

        return self.df

    def save(self, output_file):
        self.df.to_csv(output_file, index=False)