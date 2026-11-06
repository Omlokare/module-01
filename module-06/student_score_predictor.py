"""Estimate an exam score from study hours using a simple ML regression model."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


DATA_FILE = Path(__file__).with_name("student_scores.csv")


def load_dataset(path=DATA_FILE):
    """Load the CSV and check for the columns and values this project needs."""
    data = pd.read_csv(path)
    required_columns = {"study_hours", "exam_score"}
    if not required_columns.issubset(data.columns):
        raise ValueError("CSV must contain study_hours and exam_score columns.")
    data = data[["study_hours", "exam_score"]].dropna()
    if data.empty:
        raise ValueError("The dataset has no complete rows to train on.")
    if (data["study_hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")
    if not data["exam_score"].between(0, 100).all():
        raise ValueError("Exam scores must be between 0 and 100.")
    return data


def train_and_evaluate(data):
    """Train the model on one subset and report performance on held-out data."""
    features = data[["study_hours"]]
    target = data["exam_score"]
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r_squared = r2_score(y_test, predictions)
    print("Model evaluation on held-out test data")
    print(f"Mean Absolute Error (MAE): {mae:.2f} points")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f} points")
    print(f"R-squared: {r_squared:.3f}")
    return model


def predict_score(model):
    """Ask for study hours and show the model's estimate."""
    raw_hours = input("Enter study hours for a score estimate (or press Enter for 6): ").strip()
    try:
        hours = float(raw_hours) if raw_hours else 6.0
    except ValueError:
        print("Please enter a number, such as 4.5.")
        return
    if hours < 0:
        print("Study hours cannot be negative.")
        return

    estimate = model.predict(pd.DataFrame({"study_hours": [hours]}))[0]
    estimate = max(0, min(100, estimate))
    print(f"Estimated score for {hours:g} study hours: {estimate:.1f} / 100")
    print("This is a practice estimate from synthetic data, not a real prediction of ability.")


def main():
    try:
        data = load_dataset()
    except (OSError, ValueError, pd.errors.ParserError) as error:
        print(f"Could not load the dataset: {error}")
        return

    model = train_and_evaluate(data)
    predict_score(model)


if __name__ == "__main__":
    main()
