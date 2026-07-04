# 第5回 誤差逆伝播

## この回で学ぶこと

forwardからbackwardまで、小さなネットワークで追います。Lossから重みの勾配へ戻る流れを確認します。


## 含まれるファイル

- `excel_backpropagation_demo.xlsx`
- `excel_backpropagation_demo_code.py`
- `excel_backpropagation_slides.pptx`
- `README.md`

## 使い方

1. `excel_backpropagation_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_backpropagation_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の値や `display_mode` を変えて、返却表がどう変わるかを見る。

## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:B8` | `input_df` | 入力と正解 |
| `01_INPUT D6:E10` | `param_df` | 重みとバイアス |
| `01_INPUT G6:I8` | `settings_df` | 表示設定 |

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

