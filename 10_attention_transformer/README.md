# 第10回 Attention / Transformer総復習

## この回で学ぶこと

Q/K/V、score、Softmax、Attention weight、contextを確認します。どのKeyに注目し、Valueをどう集めて出力を作るかを表で見ます。この回ではTransformer全体ではなく、Attentionの核になる計算に絞ります。


## 含まれるファイル

- `excel_attention_transformer_demo.xlsx`
- `excel_attention_transformer_demo_code.py`
- `excel_attention_transformer_slides.pptx`
- `excel_attention_transformer_operation_explainer.pptx`
- `README.md`

## 使い方

1. `excel_attention_transformer_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_attention_transformer_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上のQ/K/V、`query_token`、`temperature`、`display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:F9` | `token_df` | Query、Key、Valueを変えるとscore、weight、contextが変わる |
| `01_INPUT H6:J9` | `settings_df` | query token、Softmax温度、返却表が変わる |

## 返却されるDataFrame

| display_mode | DataFrame | 読むポイント |
|---|---|---|
| `qkv` | `qkv_vector_df` | 各tokenのQuery、Key、Valueと、選ばれたQueryを見る |
| `scores` | `attention_score_df` | Queryと各Keyの内積scoreを見る |
| `weights` | `attention_weight_df` | scoreがSoftmaxでAttention weightになる流れを見る |
| `context` | `context_vector_df` | weightでValueを加重平均し、contextを作る流れを見る |
| `exam` | `e_exam_point_df` | Attentionで読むべき用語を確認する |

## 見るべき変化

`query_token` を変えると、同じKeyでもscoreとAttention weightが変わります。`temperature` を小さくすると、大きいscoreへ重みが集中しやすくなります。`context_value` は、各ValueにAttention weightを掛けて足した値です。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

