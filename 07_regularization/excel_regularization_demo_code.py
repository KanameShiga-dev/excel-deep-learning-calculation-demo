import pandas as pd
import numpy as np

loss_log_df = xl("'01_INPUT'!A6:C11", headers=True).dropna(how="all")
weight_df = xl("'01_INPUT'!E6:F9", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!H6:J10", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "loss_log")
l1 = float(settings.get("l1_lambda", 0.01))
l2 = float(settings.get("l2_lambda", 0.05))
patience = int(float(settings.get("patience", 2)))

loss_log_df["train_loss"] = loss_log_df["train_loss"].astype(float)
loss_log_df["valid_loss"] = loss_log_df["valid_loss"].astype(float)
loss_log_df["gap"] = np.round(loss_log_df["valid_loss"] - loss_log_df["train_loss"], 4)
best_valid = loss_log_df["valid_loss"].cummin()
loss_log_df["best_valid_so_far"] = best_valid
loss_log_df["no_improve"] = loss_log_df["valid_loss"] > best_valid.shift(1).fillna(loss_log_df["valid_loss"])
loss_log_df["early_stop_flag"] = loss_log_df["no_improve"].rolling(patience).sum().fillna(0) >= patience

weights = weight_df["weight"].astype(float)
regularization_df = weight_df.copy()
regularization_df["l1_penalty"] = np.round(l1 * np.abs(weights), 4)
regularization_df["l2_penalty"] = np.round(l2 * weights ** 2, 4)

e_exam_point_df = pd.DataFrame([
    {"point": "overfitting", "read_as": "訓練Lossだけ下がり、検証Lossが悪化する状態"},
    {"point": "regularization", "read_as": "大きすぎる重みへペナルティを足す"},
    {"point": "early_stopping", "read_as": "検証Lossが改善しない時に止める"},
])

if display_mode == "regularization":
    result_df = regularization_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = loss_log_df

result_df
