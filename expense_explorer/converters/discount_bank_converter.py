import pandas as pd
from .converter import Converter


class DiscountBankConverter(Converter):
    def __init__(self, input_file_path, output_path):
        super(DiscountBankConverter, self).__init__(input_file_path, output_path)

    def _extract(self):
        return self._read_xlsx_to_df()

    def _transform(self, df):
        return df

    def _load(self, df):
        df.to_csv(self.output_path, index=False)

    def _read_xlsx_to_df(self):
        return pd.read_excel(self.input_file_path, skiprows=12, skipfooter=7)