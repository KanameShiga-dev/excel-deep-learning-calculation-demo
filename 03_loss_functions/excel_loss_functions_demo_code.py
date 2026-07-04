import pandas as pd
import numpy as np

prediction_df = xl("'01_INPUT'!A6:D10", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!F6:H8", headers=True).dropna(how="all")

prediction_df["prediction"] = prediction_df["prediction"].astype(float)
prediction_df["target"] = prediction_df["target"].astype(float)
settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "loss")
epsilon = float(settings.get("epsilon", 1e-7))

p = np.clip(prediction_df["prediction"].to_numpy(dtype=float), epsilon, 1.0 - epsilon)
t = prediction_df["target"].to_numpy(dtype=float)
mse = (p - t) ** 2
bce = -(t * np.log(p) + (1.0 - t) * np.log(1.0 - p))

loss_by_sample_df = prediction_df.copy()
loss_by_sample_df["mse"] = np.round(mse, 4)
loss_by_sample_df["binary_cross_entropy"] = np.round(bce, 4)
loss_by_sample_df["absolute_error"] = np.round(np.abs(p - t), 4)

loss_summary_df = pd.DataFrame([
    {"loss_type": "MSE", "mean_loss": round(float(mse.mean()), 4)},
    {"loss_type": "Binary Cross Entropy", "mean_loss": round(float(bce.mean()), 4)},
])

e_exam_point_df = pd.DataFrame([
    {"point": "loss", "read_as": "予測と正解のズレを1つの数値にする"},
    {"point": "mse", "read_as": "回帰でよく使う二乗誤差"},
    {"point": "cross_entropy", "read_as": "分類で正解確率が低いほど大きくなる"},
])

if display_mode == "summary":
    result_df = loss_summary_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = loss_by_sample_df

result_df
