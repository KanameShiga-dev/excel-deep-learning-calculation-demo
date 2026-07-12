# 第6回 最適化手法

## この回で学ぶこと

同じ勾配でも、更新方法によってパラメータの動き方が変わることを見ます。SGD、Momentum、AdaGrad、RMSProp、Adamを同じ勾配列で比較します。


## 含まれるファイル

- `excel_optimizers_demo.xlsx`
- `excel_optimizers_demo_code.py`
- `excel_optimizers_slides.pptx`
- `excel_optimizers_operation_explainer.pptx`
- `README.md`

## 使い方

1. `excel_optimizers_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_optimizers_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の勾配列、学習率、各手法の設定、`display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:B10` | `gradient_df` | 同じ勾配列に対する各手法の更新が変わる |
| `01_INPUT D6:F13` | `settings_df` | 学習率、Momentum、RMSProp、Adamの設定が変わる |

## 返却されるDataFrame

| display_mode | DataFrame | 読むポイント |
|---|---|---|
| `compare` | `optimizer_compare_df` | 同じstepで、手法ごとのweightがどう離れていくかを見る |
| `state` | `optimizer_state_df` | AdaGradの二乗和、RMSPropの移動平均、Adamの一次/二次状態を見る |
| `summary` | `path_summary_df` | 最終step時点のweightを手法別に比較する |
| `exam` | `e_exam_point_df` | 各手法が勾配をどう使うかを確認する |

## 見るべき変化

`gradient` が同じでも、AdaGradは過去の勾配二乗和が増えるほど更新量が小さくなります。RMSPropは勾配二乗の移動平均を使うため、古い勾配の影響を徐々に薄めます。Adamは勾配の向きと大きさの移動平均を組み合わせて更新量を調整します。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

