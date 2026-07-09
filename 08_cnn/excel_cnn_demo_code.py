import pandas as pd
import numpy as np

image_df = xl("'01_INPUT'!A6:C8", headers=False).dropna(how="all")
filter_df = xl("'01_INPUT'!E6:F7", headers=False).dropna(how="all")
settings_df = xl("'01_INPUT'!H6:J9", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "feature")
stride = int(float(settings.get("stride", 1)))
padding = int(float(settings.get("padding", 0)))
image = image_df.astype(float).to_numpy()
kernel = filter_df.astype(float).to_numpy()
if stride < 1:
    raise ValueError("stride は1以上にしてください")
if padding < 0:
    raise ValueError("padding は0以上にしてください")

padded_image = np.pad(image, ((padding, padding), (padding, padding)), mode="constant")
rows = []
features = []
for r in range(0, padded_image.shape[0] - kernel.shape[0] + 1, stride):
    feature_row = []
    for c in range(0, padded_image.shape[1] - kernel.shape[1] + 1, stride):
        window = padded_image[r:r+kernel.shape[0], c:c+kernel.shape[1]]
        value = float((window * kernel).sum())
        feature_row.append(value)
        rows.append({
            "out_row": len(features) + 1,
            "out_col": len(feature_row),
            "padded_row_start": r + 1,
            "padded_col_start": c + 1,
            "window_sum_product": round(value, 4),
        })
    features.append(feature_row)

conv_window_df = pd.DataFrame(rows)
feature_map_df = pd.DataFrame(features, columns=[f"col_{i+1}" for i in range(len(features[0]))])
feature_map_df.insert(0, "row", [f"row_{i+1}" for i in range(len(features))])
conv_summary_df = pd.DataFrame([{
    "image_shape": f"{image.shape[0]}x{image.shape[1]}",
    "kernel_shape": f"{kernel.shape[0]}x{kernel.shape[1]}",
    "padding": padding,
    "stride": stride,
    "padded_shape": f"{padded_image.shape[0]}x{padded_image.shape[1]}",
    "feature_map_shape": f"{len(features)}x{len(features[0])}",
}])
e_exam_point_df = pd.DataFrame([
    {"point": "filter", "read_as": "小さな重み行列を画像上で滑らせる"},
    {"point": "padding", "read_as": "画像の外側に0を足して端も見やすくする"},
    {"point": "stride", "read_as": "フィルタを何マスずつ動かすか"},
    {"point": "feature_map", "read_as": "各場所の積和を並べたもの"},
])

if display_mode == "window":
    result_df = conv_window_df
elif display_mode == "summary":
    result_df = conv_summary_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = feature_map_df

result_df
