# 第1回 線形変換

## この回で学ぶこと

`y = Wx + b` を、小さな入力ベクトル、重み行列、バイアスで確認します。入力、重み、バイアスから `score` が作られる流れを表で追います。

## 含まれるファイル

- `excel_linear_transform_demo.xlsx`
- `excel_linear_transform_demo_code.py`
- `excel_linear_transform_slides.pptx`
- `README.md`

## 使い方

1. `excel_linear_transform_demo.xlsx` を開く。
2. `01_INPUT` の入力ベクトル、重み、バイアス、表示設定を確認する。
3. `excel_linear_transform_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `linear_trace_df` または `output_scores_df` を確認する。
5. Excel上の入力、重み、バイアス、表示モードを変えて、Pythonの返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:C9` | `x_value` | 各出力ユニットの積和とscoreが変わる |
| `01_INPUT E6:G12` | `weight` | どの入力がどの出力に効くかが変わる |
| `01_INPUT I6:J8` | `bias` | weighted_sumに足される基準値が変わる |
| `01_INPUT A13:C15` | `display_mode` | 返却されるDataFrameが変わる |

## Pythonが返すDataFrame

| DataFrame | 内容 |
|---|---|
| `linear_trace_df` | `output_unit`, `input_name`, `x_value`, `weight`, `x_times_w`, `partial_sum`, `bias` |
| `output_scores_df` | `output_unit`, `weighted_sum`, `bias`, `score`, `rank`, `largest_flag` |
| `result_df` | `display_mode` に応じてExcelへ返す表 |

## 注意

この教材は、線形変換の計算を小さな表で確認するための補助教材です。

