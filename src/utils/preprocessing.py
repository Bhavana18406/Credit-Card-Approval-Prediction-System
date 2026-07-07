
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder


class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self, features_with_outliers=["Family member count", "Income", "Employment length"]):
        self.features_with_outliers = features_with_outliers

    def fit(self, df):
        return self

    def transform(self, df):
        if set(self.features_with_outliers).issubset(df.columns):
            Q1 = df[self.features_with_outliers].quantile(0.25)
            Q3 = df[self.features_with_outliers].quantile(0.75)
            IQR = Q3 - Q1
            df = df[~((df[self.features_with_outliers] < (Q1 - 3 * IQR)) | (df[self.features_with_outliers] > (Q3 + 3 * IQR))).any(axis=1)]
            return df
        return df


class FeatureDropper(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_drop=["Has a mobile phone", "Children count", "Job title", "Account age"]):
        self.features_to_drop = features_to_drop

    def fit(self, df):
        return self

    def transform(self, df):
        if set(self.features_to_drop).issubset(df.columns):
            df.drop(self.features_to_drop, axis=1, inplace=True)
            return df
        return df


class TimeConverter(BaseEstimator, TransformerMixin):
    def __init__(self, features_with_days=["Employment length", "Age"]):
        self.features_with_days = features_with_days

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if set(self.features_with_days).issubset(X.columns):
            X[self.features_with_days] = np.abs(X[self.features_with_days])
            return X
        return X


class RetireeHandler(BaseEstimator, TransformerMixin):
    def fit(self, df):
        return self

    def transform(self, df):
        if "Employment length" in df.columns:
            retiree_indices = df[df["Employment length"] == 365243].index
            df.loc[retiree_indices, "Employment length"] = 0
            return df
        return df


class SkewnessReducer(BaseEstimator, TransformerMixin):
    def __init__(self, skewed_features=["Income", "Age"]):
        self.skewed_features = skewed_features

    def fit(self, df):
        return self

    def transform(self, df):
        if set(self.skewed_features).issubset(df.columns):
            df[self.skewed_features] = np.cbrt(df[self.skewed_features])
            return df
        return df


class BinaryEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_encode=["Has a work phone", "Has a phone", "Has an email"]):
        self.features_to_encode = features_to_encode

    def fit(self, df):
        return self

    def transform(self, df):
        if set(self.features_to_encode).issubset(df.columns):
            for feature in self.features_to_encode:
                df[feature] = df[feature].map({1: "Y", 0: "N"})
            return df
        return df


class OneHotEncoderWithNames(BaseEstimator, TransformerMixin):
    def __init__(self, one_hot_features=["Gender", "Marital status", "Dwelling", "Employment status", "Has a car", "Has a property", "Has a work phone", "Has a phone", "Has an email"]):
        self.one_hot_features = one_hot_features

    def fit(self, df):
        return self

    def transform(self, df):
        if set(self.one_hot_features).issubset(df.columns):
            encoder = OneHotEncoder(sparse_output=False)
            encoded = encoder.fit_transform(df[self.one_hot_features])
            feature_names = encoder.get_feature_names_out(self.one_hot_features)
            encoded_df = pd.DataFrame(encoded, columns=feature_names, index=df.index)
            remaining_features = [col for col in df.columns if col not in self.one_hot_features]
            return pd.concat([encoded_df, df[remaining_features]], axis=1)
        return df


class OrdinalEncoderWithNames(BaseEstimator, TransformerMixin):
    def __init__(self, ordinal_features=["Education level"]):
        self.ordinal_features = ordinal_features

    def fit(self, df):
        return self

    def transform(self, df):
        if "Education level" in df.columns:
            encoder = OrdinalEncoder()
            df[self.ordinal_features] = encoder.fit_transform(df[self.ordinal_features])
            return df
        return df


class MinMaxScalerWithNames(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_scale=["Age", "Income", "Employment length"]):
        self.features_to_scale = features_to_scale

    def fit(self, df):
        return self

    def transform(self, df):
        if set(self.features_to_scale).issubset(df.columns):
            scaler = MinMaxScaler()
            df[self.features_to_scale] = scaler.fit_transform(df[self.features_to_scale])
            return df
        return df


class TargetEncoder(BaseEstimator, TransformerMixin):
    def fit(self, df):
        return self

    def transform(self, df):
        if "Is high risk" in df.columns:
            df["Is high risk"] = pd.to_numeric(df["Is high risk"])
            return df
        return df


def create_preprocessing_pipeline():
    return Pipeline([
        ("outlier_remover", OutlierRemover()),
        ("feature_dropper", FeatureDropper()),
        ("time_converter", TimeConverter()),
        ("retiree_handler", RetireeHandler()),
        ("skewness_reducer", SkewnessReducer()),
        ("binary_encoder", BinaryEncoder()),
        ("one_hot_encoder", OneHotEncoderWithNames()),
        ("ordinal_encoder", OrdinalEncoderWithNames()),
        ("minmax_scaler", MinMaxScalerWithNames()),
        ("target_encoder", TargetEncoder())
    ])

