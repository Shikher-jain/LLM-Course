"""
This module provides basic utilities for data processing,
including cleaning text, computing statistics, and simple ML inference.
"""

import re
from typing import List
import numpy as np


def clean_text(text: str) -> str:
    """
    Cleans input text by removing special characters and extra spaces.

    Args:
        text (str): Raw input string

    Returns:
        str: Cleaned text
    """
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def compute_mean(values: List[float]) -> float:
    """
    Computes the mean of a list of numbers.

    Args:
        values (List[float]): List of numeric values

    Returns:
        float: Mean value
    """
    if not values:
        raise ValueError("List is empty")
    return float(np.mean(values))


class SimpleModel:
    """
    A mock ML model for demonstration purposes.
    """

    def __init__(self, weight: float = 0.5):
        self.weight = weight

    def predict(self, x: float) -> float:
        """
        Predicts output using a simple linear equation.

        Args:
            x (float): Input feature

        Returns:
            float: Predicted value
        """
        return self.weight * x


def run_inference(data: List[float]) -> List[float]:
    """
    Runs inference on a list of values using SimpleModel.

    Args:
        data (List[float]): Input data

    Returns:
        List[float]: Predictions
    """
    model = SimpleModel(weight=0.8)
    return [model.predict(x) for x in data]


if __name__ == "__main__":
    sample_text = "Hello!!!   This is a TEST text...   "
    cleaned = clean_text(sample_text)
    print("Cleaned Text:", cleaned)

    values = [1, 2, 3, 4, 5]
    print("Mean:", compute_mean(values))

    predictions = run_inference(values)
    print("Predictions:", predictions)