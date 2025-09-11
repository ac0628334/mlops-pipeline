import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

class DataCleaner(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.imputer = SimpleImputer(strategy="mean")
        self.scaler = StandardScaler()

    def fit(self, X, y=None):
        X_imputed = self.imputer.fit_transform(X)
        self.scaler.fit(X_imputed)
        return self

    def transform(self, X, y=None):
        X_imputed = self.imputer.transform(X)
        return self.scaler.transform(X_imputed)
