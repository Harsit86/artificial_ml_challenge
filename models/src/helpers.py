import joblib


def load_model_pipeline(model_pkl):
    return joblib.load(model_pkl)
