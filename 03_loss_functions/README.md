# 第3回 損失関数

## この回で学ぶこと

予測と正解のズレがLossになる流れを見ます。2値分類のBinary Cross Entropyと、多クラス分類のCross Entropyを小さな表で確認します。


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
5. Excel上の予測値、正解、正解クラスの確率、`display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:D10` | `prediction_df` | 2値分類の予測、正解、BCEが変わる |
| `01_INPUT A14:E18` | `class_prob_df` | 正解クラスの確率とCross Entropyが変わる |
| `01_INPUT F6:H8` | `settings_df` | `result_df` に返す表が変わる |

## 返却されるDataFrame

| display_mode | DataFrame | 読むポイント |
|---|---|---|
| `loss` | `loss_by_sample_df` | 2値分類で、予測と正解のズレがMSE/BCEになる流れを見る |
| `class_ce` | `class_ce_df` | 正解クラスに割り当てた確率が低いほどCross Entropyが大きくなることを見る |
| `summary` | `loss_summary_df` | MSE、Binary Cross Entropy、Cross Entropyの平均Lossを比較する |
| `exam` | `e_exam_point_df` | 用語と表の読み方を確認する |

## 見るべき変化

`class_ce` では、`target_class` に対応する確率列が重要です。たとえば `target_class` が `class_C` の行では、`class_C_prob` を大きくすると `cross_entropy` は小さくなります。逆に正解クラスの確率を小さくすると、Lossは大きくなります。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

