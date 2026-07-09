# 第7回 過学習と正則化

## この回で学ぶこと

訓練Lossと検証Loss、L1/L2、Dropout、Early Stoppingを見ます。モデルが訓練データに寄りすぎる様子と、それを抑える代表的な工夫を確認します。


## 含まれるファイル

- `excel_regularization_demo.xlsx`
- `excel_regularization_demo_code.py`
- `excel_regularization_slides.pptx`
- `README.md`

## 使い方

1. `excel_regularization_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_regularization_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上のLoss、重み、ユニット出力、`dropout_rate`、`dropout_seed`、`display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:C11` | `loss_log_df` | 訓練Loss、検証Loss、汎化ギャップ、停止判定が変わる |
| `01_INPUT E6:F9` | `weight_df` | L1/L2のペナルティが変わる |
| `01_INPUT A14:B18` | `activation_df` | Dropoutで残る/落ちるユニット出力が変わる |
| `01_INPUT H6:J12` | `settings_df` | 正則化係数、Dropout率、表示表が変わる |

## 返却されるDataFrame

| display_mode | DataFrame | 読むポイント |
|---|---|---|
| `loss_log` | `loss_log_df` | 訓練Lossと検証Lossの差、Early Stoppingの判定を見る |
| `regularization` | `regularization_df` | 重みごとのL1/L2ペナルティを見る |
| `dropout` | `dropout_trace_df` | maskが0のユニットは落ち、maskが1のユニットだけが残ることを見る |
| `exam` | `e_exam_point_df` | 過学習、正則化、Dropout、Early Stoppingの読み方を確認する |

## 見るべき変化

`dropout_rate` を大きくすると、落ちるユニットが増えやすくなります。`dropout_seed` を変えると、同じ `dropout_rate` でもどのユニットを落とすかが変わります。`scaled_activation` は、残ったユニットの出力をkeep probabilityで補正した値です。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

