import pandas as pd
import numpy as np

input_df = xl("'01_INPUT'!A6:C9", headers=True).dropna(how="all")
weight_df = xl("'01_INPUT'!E6:G12", headers=True).dropna(how="all")
bias_df = xl("'01_INPUT'!I6:J8", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!A13:C15", headers=True).dropna(how="all")

input_df["x_value"] = input_df["x_value"].astype(float)
weight_df["weight"] = weight_df["weight"].astype(float)
bias_df["bias"] = bias_df["bias"].astype(float)

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "trace")

merged_df = weight_df.merge(input_df, on="input_name", how="left")
merged_df["x_times_w"] = merged_df["x_value"] * merged_df["weight"]
merged_df["partial_sum"] = merged_df.groupby("output_unit")["x_times_w"].cumsum()

score_df = (
    merged_df.groupby("output_unit", as_index=False)["x_times_w"]
    .sum()
    .rename(columns={"x_times_w": "weighted_sum"})
)
score_df = score_df.merge(bias_df, on="output_unit", how="left")
score_df["score"] = score_df["weighted_sum"] + score_df["bias"]
score_df["rank"] = score_df["score"].rank(ascending=False, method="dense").astype(int)
score_df["largest_flag"] = score_df["rank"].eq(1)

linear_trace_df = merged_df.merge(bias_df, on="output_unit", how="left")
linear_trace_df = linear_trace_df[
    [
        "output_unit",
        "input_name",
        "x_value",
        "weight",
        "x_times_w",
        "partial_sum",
        "bias",
    ]
].round(4)

output_scores_df = score_df[
    ["output_unit", "weighted_sum", "bias", "score", "rank", "largest_flag"]
].round(4)

e_exam_point_df = pd.DataFrame(
    [
        {
            "point": "forward",
            "formula": "y = Wx + b",
            "read_as": "入力xに重みWを掛け、biasを足してscoreを作る",
        },
        {
            "point": "shape",
            "formula": "input count x output count",
            "read_as": "行列の向きと列名を確認する",
        },
        {
            "point": "change",
            "formula": "x or W or b changes score",
            "read_as": "Excelの値を変えるとPythonのscoreが変わる",
        },
    ]
)

if display_mode == "scores":
    result_df = output_scores_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = linear_trace_df

result_df
