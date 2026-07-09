# 第10回 Attention / Transformer総復習

## この回で学ぶこと

Q/K/V、Attention weight、contextを確認します。どの入力に注目して出力を作るかを表で見ます。


## 含まれるファイル

- `excel_attention_transformer_demo.xlsx`
- `excel_attention_transformer_demo_code.py`
- `excel_attention_transformer_slides.pptx`
- `excel_attention_transformer_operation_explainer.pptx` - デモ操作解説スライド
- `README.md`

## 使い方

1. `excel_attention_transformer_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_attention_transformer_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の値や `display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:D9` | `token_df` | Q/K/V入力 |
| `01_INPUT F6:H8` | `settings_df` | Attention設定 |

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。




