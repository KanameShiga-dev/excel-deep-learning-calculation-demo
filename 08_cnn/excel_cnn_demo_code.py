import pandas as pd
import numpy as np

image_df = xl("'01_INPUT'!A6:C8", headers=False).dropna(how="all")
filter_df = xl("'01_INPUT'!E6:F7", headers=False).dropna(how="all")
settings_df = xl("'01_INPUT'!H6:J8", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "feature")
image = image_df.astype(float).to_numpy()
kernel = filter_df.astype(float).to_numpy()
rows = []
features = []
for r in range(image.shape[0] - kernel.shape[0] + 1):
    feature_row = []
    for c in range(image.shape[1] - kernel.shape[1] + 1):
        window = image[r:r+kernel.shape[0], c:c+kernel.shape[1]]
        value = float((window * kernel).sum())
        feature_row.append(value)
        rows.append({"out_row": r + 1, "out_col": c + 1, "window_sum_product": round(value, 4)})
    features.append(feature_row)

conv_window_df = pd.DataFrame(rows)
feature_map_df = pd.DataFrame(features, columns=[f"col_{i+1}" for i in range(len(features[0]))])
feature_map_df.insert(0, "row", [f"row_{i+1}" for i in range(len(features))])
e_exam_point_df = pd.DataFrame([
    {"point": "filter", "read_as": "小さな重み行列を画像上で滑らせる"},
    {"point": "feature_map", "read_as": "各場所の積和を並べたもの"},
])

if display_mode == "window":
    result_df = conv_window_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = feature_map_df

result_df
