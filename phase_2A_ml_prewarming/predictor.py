# predictor.py

from sklearn.linear_model import LinearRegression
import numpy as np

class MLForecaster:
    def __init__(self, window_size):
        self.window_size = window_size
        self.model = LinearRegression()

    def predict_next(self, data):
        if len(data) < self.window_size:
            return data[-1]  # not enough data
        x = np.arange(self.window_size).reshape(-1, 1)
        y = np.array(data[-self.window_size:])
        self.model.fit(x, y)
        return round(self.model.predict([[self.window_size]])[0])
