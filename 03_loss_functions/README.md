# 第3回 損失関数

## この回で学ぶこと

予測と正解のズレがLossになる流れを見ます。回帰と分類で、誤差の見方がどう変わるかを確認します。


## 含まれるファイル

- `excel_loss_functions_demo.xlsx`
- `excel_loss_functions_demo_code.py`
- `excel_loss_functions_slides.pptx`
- `README.md`

## 使い方

1. `excel_loss_functions_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_loss_functions_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の値や `display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:D10` | `prediction_df` | 予測と正解 |
| `01_INPUT F6:H8` | `settings_df` | Loss設定 |

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

