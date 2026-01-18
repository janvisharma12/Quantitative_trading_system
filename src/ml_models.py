"""
Machine learning models module.

This module represents the ML layer of the project.
Actual model training, evaluation, and backtesting
are implemented in detail inside the Jupyter notebooks.

Saved model artifacts:
- Gradient Boosting model (.pkl)
- LSTM model (.h5)

These files are loaded in notebooks for inference
and strategy evaluation.
"""

def load_xgb_model(path):
    """
    Load a trained Gradient Boosting / XGBoost model.
    """
    import joblib
    return joblib.load(path)


def load_lstm_model(path):
    """
    Load a trained LSTM model.
    """
    from tensorflow.keras.models import load_model
    return load_model(path)
