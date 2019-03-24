import calendar
import pandas as pd
from logger import get_logger
from sklearn.base import TransformerMixin
from sklearn.preprocessing import OneHotEncoder


MONTH_REPLACE_MAP = {v.lower(): k for k,v in enumerate(calendar.month_abbr) if v}
BOOL_REPLACE_MAP = {
    'yes': 1,
    'no': 0,
    'unknown': -1
}

log = get_logger(__name__)


class RawDataTransformer(TransformerMixin):

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



class ModelDataTransfomer(TransformerMixin):

    def __init__(self, *args, **kwargs):
        self._cat_cols = None
        self._cont_cols = None
        self._ohe = None

    def get_feature_names(self):
        return list(self._cont_cols) + list(self._ohe.get_feature_names())

    def transform(self, df, *_):
        log.info('One hot encode categorical features and concat with continuous features.')
        return pd.concat([
            df[self._cont_cols].copy(),
            pd.DataFrame(
                self._ohe.transform(df[self._cat_cols]).todense(),
                columns=self._ohe.get_feature_names(),
                index=df.index
            )
        ], axis=1)

    def fit(self, df, *_):
        if self._ohe is None:
            self._ohe = OneHotEncoder()
            mask = df.dtypes == 'object'
            self._cat_cols = df.columns[mask]
            self._cont_cols = df.columns[~mask]
            self._ohe.fit(df[self._cat_cols])

        return self