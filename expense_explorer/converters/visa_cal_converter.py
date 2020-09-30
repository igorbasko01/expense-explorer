import chardet
import pandas as pd
from .converter import Converter


class VisalCalConverter(Converter):
    def __init__(self, input_file_path, output_path):
        super(VisalCalConverter, self).__init__(input_file_path, output_path)
        self._set_date_col('תאריך העסקה')
        self._set_expense_col('שם בית העסק')
        self._set_amount_col('סכום החיוב')

    def _get_file_encoding(self):
        with open(self.input_file_path, 'rb') as f:
            result = chardet.detect(f.read())
        self.log.info("Detected the following encoding: %s", result['encoding'])
        return result['encoding']

    def _read_csv_to_df(self, encoding=None):
        return pd.read_csv(self.input_file_path, encoding=encoding, sep='\t', skiprows=2, skipfooter=1, engine='python')

    @classmethod
    def _price_to_float(cls, df, indexes=None):
        for index in indexes:
            df.iloc[:, index] = df.iloc[:, index].str.replace('₪|,', '').str.strip(' ').astype(float)

    def _extract(self):
        encoding = self._get_file_encoding()
        contents = self._read_csv_to_df(encoding)
        return contents

    def _transform(self, df):
        self._price_to_float(df, indexes=[2, 3])
        return df
