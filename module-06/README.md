# Module 06: Final AI & Machine Learning Project

## Student Score Predictor

A beginner-friendly machine learning project that estimates an exam score from study hours using a Linear Regression model. The included dataset is synthetic and intended for learning only.

## Try the live web app

When deployed, open the Render service URL. The app accepts study hours and displays a score estimate.

## Run locally as a web app

1. Install Python 3.10 or newer.
2. From the repository root, install dependencies:

   ```bash
   python -m pip install -r module-06/requirements.txt
   ```

3. Start the app:

   ```bash
   cd module-06
   python -m flask --app app run
   ```

4. Open http://127.0.0.1:5000.

## Project files

- `app.py` — Flask web interface and health endpoint.
- `student_score_predictor.py` — data validation, model training, test evaluation, and command-line prediction.
- `student_scores.csv` — small synthetic sample dataset.
- `requirements.txt` — project dependencies.

## Machine learning workflow

1. Load and inspect the CSV with Pandas.
2. Separate the input feature (`study_hours`) from the target (`exam_score`).
3. Split examples into training and test sets.
4. Fit a Scikit-learn Linear Regression model using training data.
5. Evaluate test predictions with MAE, RMSE, and R-squared.
6. Serve estimates through the web app.

## Important limitations

This sample dataset is synthetic, very small, and only demonstrates a workflow. Study time alone does not determine a student's score. Do not use this model to make real educational decisions or judge students.
