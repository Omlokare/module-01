from flask import Flask, request, render_template_string
import pandas as pd

from student_score_predictor import DATA_FILE, load_dataset, train_and_evaluate

app = Flask(__name__)
DATA = load_dataset(DATA_FILE)
MODEL = train_and_evaluate(DATA)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Student Score Predictor</title>
  <style>
    :root { color-scheme: light; font-family: Inter, system-ui, Arial, sans-serif; }
    body { margin: 0; background: #f2f6fb; color: #17233b; }
    main { max-width: 760px; margin: 8vh auto; padding: 0 20px; }
    .card { background: white; border: 1px solid #dce5ef; border-radius: 18px; padding: 32px; box-shadow: 0 14px 40px #19324d12; }
    h1 { margin-top: 0; color: #145ca8; }
    p { line-height: 1.6; color: #48576b; }
    label { display: block; font-weight: 650; margin: 22px 0 8px; }
    input { box-sizing: border-box; width: 100%; border: 1px solid #b8c8d9; border-radius: 10px; font-size: 18px; padding: 12px; }
    button { margin-top: 16px; background: #145ca8; color: white; border: 0; border-radius: 10px; padding: 13px 20px; font-size: 16px; font-weight: 700; cursor: pointer; }
    .result { margin-top: 22px; padding: 16px; background: #eaf5ee; border-radius: 12px; color: #17633b; font-size: 20px; font-weight: 700; }
    .error { margin-top: 18px; color: #a22; font-weight: 600; }
    .note { margin-top: 24px; border-top: 1px solid #e1e7ee; padding-top: 16px; font-size: 13px; }
  </style>
</head>
<body><main><section class="card">
  <h1>Student Score Predictor</h1>
  <p>A small machine learning demo. Enter study hours to see an estimate from a Linear Regression model trained on the included sample dataset.</p>
  <form method="post">
    <label for="hours">Study hours</label>
    <input id="hours" name="hours" type="number" min="0" max="100" step="0.1" value="{{ hours or '' }}" placeholder="For example, 6" required>
    <button type="submit">Estimate score</button>
  </form>
  {% if result is not none %}<div class="result">Estimated score: {{ result }} / 100</div>{% endif %}
  {% if error %}<div class="error">{{ error }}</div>{% endif %}
  <p class="note">Learning demo only. The sample dataset is synthetic and very small. Study time alone does not determine a student's score. Do not use this estimate to make real educational decisions.</p>
</section></main></body></html>
"""

@app.get("/")
def home():
    return render_template_string(PAGE, hours="", result=None, error=None)

@app.post("/")
def predict():
    raw_hours = request.form.get("hours", "").strip()
    try:
        hours = float(raw_hours)
        if hours < 0 or hours > 100:
            raise ValueError
    except ValueError:
        return render_template_string(PAGE, hours=raw_hours, result=None,
                                      error="Enter a number from 0 to 100."), 400

    estimate = float(MODEL.predict(pd.DataFrame({"study_hours": [hours]}))[0])
    estimate = max(0.0, min(100.0, estimate))
    return render_template_string(PAGE, hours=hours, result=f"{estimate:.1f}", error=None)

@app.get("/health")
def health():
    return {"status": "ok"}
