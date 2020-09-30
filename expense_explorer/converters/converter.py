import logging


class Converter(object):
    def __init__(self, input_file_path, output_path):
        self.log = logging.getLogger(self.__class__.__name__)
        self.input_file_path = input_file_path
        self.output_path = output_path
        self.input_columns = {}

    def _set_date_col(self, col_name):
        self.input_columns[col_name] = 'Date'

    def _set_expense_col(self, col_name):
        self.input_columns[col_name] = 'Expense'

    def _set_amount_col(self, col_name):
        self.input_columns[col_name] = 'Amount'

    def _extract(self):
        raise NotImplementedError()

    def _transform(self, df):
        raise NotImplementedError()

    def _load(self, df):
        df_out = df[[self.input_columns.keys()]]
        df_out.rename(columns=self.input_columns, inplace=True)
        df_out.to_csv(self.output_path, index=False)

    def run(self):
        df = self._extract()
        df = self._transform(df)
        self._load(df)