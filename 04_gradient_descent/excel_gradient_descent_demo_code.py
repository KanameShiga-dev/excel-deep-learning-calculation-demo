import pandas as pd
import numpy as np

data_df = xl("'01_INPUT'!A6:B8", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!D6:F9", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "training")
learning_rate = float(settings.get("learning_rate", 0.1))
initial_weight = float(settings.get("initial_weight", 0.0))
steps = int(float(settings.get("steps", 8)))

x = data_df["x"].astype(float).to_numpy()
y_true = data_df["target"].astype(float).to_numpy()
w = initial_weight
rows = []
for step in range(steps + 1):
    y_pred = w * x
    loss = ((y_pred - y_true) ** 2).mean()
    grad = (2.0 * x * (y_pred - y_true)).mean()
    rows.append({"step": step, "weight": round(w, 4), "prediction_mean": round(float(y_pred.mean()), 4), "loss": round(float(loss), 4), "gradient": round(float(grad), 4)})
    w = w - learning_rate * grad

training_log_df = pd.DataFrame(rows)
update_trace_df = training_log_df.assign(learning_rate=learning_rate)
e_exam_point_df = pd.DataFrame([
    {"point": "gradient", "read_as": "Lossを増やす向きを示す傾き"},
    {"point": "update", "read_as": "weight = weight - learning_rate * gradient"},
    {"point": "learning_rate", "read_as": "大きすぎると振動し、小さすぎると遅い"},
])

if display_mode == "exam":
    result_df = e_exam_point_df
elif display_mode == "update":
    result_df = update_trace_df
else:
    result_df = training_log_df

result_df
