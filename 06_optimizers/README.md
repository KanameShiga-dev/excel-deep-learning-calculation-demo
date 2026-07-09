# 第6回 最適化手法

## この回で学ぶこと

同じ勾配でも、更新方法によってパラメータの動き方が変わることを見ます。


## 含まれるファイル

- `excel_optimizers_demo.xlsx`
- `excel_optimizers_demo_code.py`
- `excel_optimizers_slides.pptx`
- `excel_optimizers_operation_explainer.pptx` - デモ操作解説スライド
- `README.md`

## 使い方

1. `excel_optimizers_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_optimizers_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の値や `display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:B10` | `gradient_df` | 勾配列 |
| `01_INPUT D6:F12` | `settings_df` | 最適化設定 |

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。




