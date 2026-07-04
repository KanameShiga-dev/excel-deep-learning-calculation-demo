# 第8回 CNN

## この回で学ぶこと

小さな画像行列から特徴マップを作ります。フィルタがどの範囲を見ているかを表で確認します。


## 含まれるファイル

- `excel_cnn_demo.xlsx`
- `excel_cnn_demo_code.py`
- `excel_cnn_slides.pptx`
- `README.md`

## 使い方

1. `excel_cnn_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_cnn_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の値や `display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:C8` | `image_df` | 画像行列 |
| `01_INPUT E6:F7` | `filter_df` | フィルタ |
| `01_INPUT H6:J8` | `settings_df` | 畳み込み設定 |

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

