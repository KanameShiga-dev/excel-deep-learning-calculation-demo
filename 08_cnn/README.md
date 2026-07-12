# 第8回 CNN

## この回で学ぶこと

小さな画像行列から特徴マップを作ります。フィルタがどの範囲を見ているか、paddingとstrideで特徴マップのサイズや値がどう変わるかを表で確認します。


## 含まれるファイル

- `excel_cnn_demo.xlsx`
- `excel_cnn_demo_code.py`
- `excel_cnn_slides.pptx`
- `excel_cnn_operation_explainer.pptx`
- `README.md`

## 使い方

1. `excel_cnn_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_cnn_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の画像、フィルタ、`padding`、`stride`、`display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:C8` | `image_df` | 画像行列を変えると、各窓の積和が変わる |
| `01_INPUT E6:F7` | `filter_df` | フィルタを変えると、強く反応する場所が変わる |
| `01_INPUT H6:J9` | `settings_df` | `padding` と `stride` で窓の位置と特徴マップのサイズが変わる |

## 返却されるDataFrame

| display_mode | DataFrame | 読むポイント |
|---|---|---|
| `feature` | `feature_map_df` | 畳み込み後の特徴マップを読む |
| `window` | `conv_window_df` | 各出力セルが、padding後のどの窓から計算されたかを見る |
| `summary` | `conv_summary_df` | image、kernel、padding、stride、feature mapの形を確認する |
| `exam` | `e_exam_point_df` | filter、padding、stride、feature mapの意味を確認する |

## 見るべき変化

`stride` を大きくすると、フィルタが飛び飛びに動くため、特徴マップのサイズが小さくなります。`padding` を1にすると画像の外側に0が足され、端の情報も窓に入りやすくなります。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

