# 第2回 活性化関数

## この回で学ぶこと

第1回で作った `score` を、Sigmoid、tanh、ReLU、Softmaxで変換します。出力範囲や勾配の大きさに加えて、SoftmaxとCross Entropyを合わせたときの `p - y` も表で確認します。


## 含まれるファイル

- `excel_activation_functions_demo.xlsx`
- `excel_activation_functions_demo_code.py`
- `excel_activation_functions_slides.pptx`
- `README.md`

## 使い方

1. `excel_activation_functions_demo.xlsx` を開く。
2. `01_INPUT` の入力値、Softmax用logit、表示設定を確認する。
3. `excel_activation_functions_demo_code.py` を外部ファイルとして開き、内容をPython in Excelへ貼り付けて実行する。
4. 返ってきた `activation_df`, `softmax_df`, `gradient_df` のいずれかを確認する。
5. Excel上の `input_value`, `logit`, `target_class`, `selected_function`, `temperature`, `display_mode` を変えて、返却表がどう変わるかを見る。


## Excelで変更できるもの

| 場所 | 変更・確認するもの | 見える変化 |
|---|---|---|
| `01_INPUT A6:B14` | `input_value` | Sigmoid、tanh、ReLUの出力と勾配が変わる |
| `01_INPUT D6:E9` | `logit` | Softmaxの確率と順位が変わる |
| `01_INPUT G6:I10` | `selected_function` | `selected_output`, `selected_gradient` が変わる |
| `01_INPUT G6:I10` | `temperature` | Softmax分布の尖り方が変わる |
| `01_INPUT G6:I10` | `target_class` | `softmax_ce_grad_df` の `target` と `dLoss_dlogit` が変わる |
| `01_INPUT G6:I10` | `display_mode` | 返却されるDataFrameが変わる |

## Pythonが返すDataFrame

| DataFrame | 内容 |
|---|---|
| `activation_df` | 入力値ごとのSigmoid、tanh、ReLU、勾配、選択関数の出力 |
| `softmax_df` | classごとのlogit、shifted_logit、exp、probability、rank |
| `softmax_ce_grad_df` | classごとのprobability、target、`dLoss_dlogit = probability - target` |
| `gradient_df` | 入力値ごとの各活性化関数の勾配 |
| `e_exam_point_df` | 確認ポイント |
| `result_df` | `display_mode` に応じてExcelへ返す表 |

## 見るべき変化

`softmax_ce_grad` では、正解クラスの `dLoss_dlogit` は `probability - 1` になります。不正解クラスは `probability` がそのまま勾配になります。これは第3回のCross Entropyとつながる分類学習の基本形です。

## 注意

この教材は、計算の流れを小さな表で確認するための補助教材です。

