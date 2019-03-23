import calendar
from app.logger import get_logger
from sklearn.base import TransformerMixin

MONTH_REPLACE_MAP = {v.lower(): k for k,v in enumerate(calendar.month_abbr) if v}
BOOL_REPLACE_MAP = {
    'yes': 1,
    'no': 0,
    'unknown': -1
}

log = get_logger(__name__)


class PreProcessor(TransformerMixin):

    @staticmethod
    def binarise_columns(df):
        binary_cols = ['default', 'housing', 'loan', 'y']
        for col in binary_cols:
            if col in df.columns:
                log.info(f'Binarising columns: {col}')
                df[col] = df[col].replace(BOOL_REPLACE_MAP).astype(int)
        return df

    @staticmethod
    def month_abbr_to_ordinal(df):
        log.info('Numerising month')
        df['month'] = df['month'].replace(MONTH_REPLACE_MAP).astype(int)
        return df

    def transform(self, df, *_):
        df = df.copy().pipe(
            self.month_abbr_to_ordinal
        ).pipe(
            self.binarise_columns
        )
        return df

    def fit(self, *_):
        return self
