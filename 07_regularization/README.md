# 第7回 過学習と正則化

## この回で学ぶこと

訓練Lossと検証Loss、正則化項、停止判定を見ます。モデルが訓練データに寄りすぎる様子を確認します。


## 含まれるファイル

- `excel_regularization_demo.xlsx`
- `excel_regularization_demo_code.py`
- `excel_regularization_slides.pptx`
- `excel_regularization_operation_explainer.pptx` - デモ操作解説スライド
- `README.md`

## 使い方

1. `excel_regularization_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_regularization_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の値や `display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:C11` | `loss_log_df` | Lossログ |
| `01_INPUT E6:F9` | `weight_df` | 重み |
| `01_INPUT H6:J10` | `settings_df` | 正則化設定 |

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。




