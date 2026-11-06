# Module 06: Final AI & Machine Learning Project

## Student Score Predictor

A beginner-friendly machine learning project that trains a regression model to estimate an exam score from study hours. The included dataset is synthetic and intended for learning only.

## Project files

- `student_score_predictor.py` — loads the data, validates it, trains and evaluates a Linear Regression model, then accepts a study-hours value for prediction.
- `student_scores.csv` — small sample dataset used by the project.
- `requirements.txt` — Python packages needed to run the project.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder and install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run the project:

   ```bash
   python student_score_predictor.py
   ```

4. Enter study hours when prompted, or press Enter to use the example value.

## Machine learning workflow

1. Load and inspect the CSV with Pandas.
2. Separate the input feature (`study_hours`) from the target (`exam_score`).
3. Split the examples into training and test sets.
4. Fit a Scikit-learn Linear Regression model using training data.
5. Evaluate test predictions with MAE, RMSE, and R-squared.
6. Use the trained model to estimate a score for a new number of study hours.

## Important limitations

This sample dataset is synthetic, very small, and only demonstrates a workflow. Study time alone does not determine a student's score. Do not use this model to make real educational decisions or judge students.

## Ideas to improve it

- Add more realistic, consented sample data.
- Compare Linear Regression with another model.
- Plot actual scores and the fitted line.
- Add more relevant features, while considering fairness and privacy.
