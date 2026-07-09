import pandas as pd
import numpy as np

prediction_df = xl("'01_INPUT'!A6:D10", headers=True).dropna(how="all")
class_prob_df = xl("'01_INPUT'!A14:E18", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!F6:H9", headers=True).dropna(how="all")

prediction_df["prediction"] = prediction_df["prediction"].astype(float)
prediction_df["target"] = prediction_df["target"].astype(float)
settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "class_ce")
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

prob_columns = [c for c in class_prob_df.columns if str(c).endswith("_prob")]
class_prob_df[prob_columns] = class_prob_df[prob_columns].astype(float)

class_rows = []
for _, row in class_prob_df.iterrows():
    target_class = str(row["target_class"])
    target_column = f"{target_class}_prob"
    if target_column not in prob_columns:
        raise ValueError(f"target_class '{target_class}' に対応する確率列がありません")

    clipped_probs = np.clip(row[prob_columns].to_numpy(dtype=float), epsilon, 1.0)
    target_probability = float(np.clip(row[target_column], epsilon, 1.0))
    predicted_column = prob_columns[int(np.argmax(clipped_probs))]
    predicted_class = predicted_column.replace("_prob", "")

    class_rows.append({
        "sample_id": row["sample_id"],
        "target_class": target_class,
        "predicted_class": predicted_class,
        "target_probability": round(target_probability, 4),
        "cross_entropy": round(float(-np.log(target_probability)), 4),
        "prob_sum": round(float(row[prob_columns].sum()), 4),
        "is_correct": predicted_class == target_class,
    })

class_ce_df = pd.DataFrame(class_rows)

loss_summary_df = pd.concat([
    loss_summary_df,
    pd.DataFrame([{
        "loss_type": "Cross Entropy",
        "mean_loss": round(float(class_ce_df["cross_entropy"].mean()), 4),
    }]),
], ignore_index=True)

e_exam_point_df = pd.DataFrame([
    {"point": "loss", "read_as": "予測と正解のズレを1つの数値にする"},
    {"point": "mse", "read_as": "回帰でよく使う二乗誤差"},
    {"point": "cross_entropy", "read_as": "正解クラスの確率が低いほど大きくなる"},
    {"point": "target_probability", "read_as": "正解クラスに割り当てた確率"},
])

if display_mode == "summary":
    result_df = loss_summary_df
elif display_mode == "class_ce":
    result_df = class_ce_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = loss_by_sample_df

result_df
