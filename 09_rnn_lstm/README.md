# 第9回 RNN / LSTM

## この回で学ぶこと

時系列入力とhidden state、ゲートを追います。LSTMのforget gate、input gate、output gateによって、cell stateとhidden stateがどう更新されるかを表で確認します。


## 含まれるファイル

- `excel_rnn_lstm_demo.xlsx`
- `excel_rnn_lstm_demo_code.py`
- `excel_rnn_lstm_slides.pptx`
- `README.md`

## 使い方

1. `excel_rnn_lstm_demo.xlsx` を開く。
2. `01_INPUT` の入力表と設定表を確認する。
3. `excel_rnn_lstm_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `result_df` を確認する。
5. Excel上の入力値、ゲート用パラメータ、`display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:B10` | `sequence_df` | 時系列入力を変えると、各時刻の状態更新が変わる |
| `01_INPUT D6:E20` | `param_df` | forget / input / output gateとcell stateの動きが変わる |
| `01_INPUT G6:I8` | `settings_df` | `result_df` に返す表が変わる |

## 返却されるDataFrame

| display_mode | DataFrame | 読むポイント |
|---|---|---|
| `sequence` | `sequence_trace_df` | 時刻ごとの入力とhidden stateの推移を見る |
| `gate` | `gate_trace_df` | forget gate、input gate、candidate、output gate、cell state、hidden stateを追う |
| `state` | `state_summary_df` | cell stateがoutput gateを通ってhidden stateになる流れを見る |
| `exam` | `e_exam_point_df` | LSTMで見るべき用語を確認する |

## 見るべき変化

forget gateは前のcell stateをどれだけ残すかを決めます。input gateは新しいcandidateをどれだけ入れるかを決めます。output gateはcell stateをどれだけhidden stateとして外に出すかを決めます。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

