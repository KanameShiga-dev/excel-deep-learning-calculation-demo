# Excelで体験するディープラーニングの計算しくみ

Excelを入力・確認用のUIとして使い、外部Pythonでディープラーニング基礎の計算を確認する教材シリーズです。

各回では、Excel上の入力値や設定を変え、Python in Excelから外部 `.py` の計算コードを実行し、返ってきた表で結果の変化を確認します。

YouTube再生リスト: https://www.youtube.com/playlist?list=PLCpGjQFeX0kY

## 含まれるもの

各回フォルダには、次のファイルを置いています。

- デモ用Excelファイル: `excel_<theme>_demo.xlsx`
- 外部Pythonコード: `excel_<theme>_demo_code.py`
- 説明スライド: `excel_<theme>_slides.pptx`
- デモ操作解説スライド: `excel_<theme>_operation_explainer.pptx`
- 各回README: `README.md`

動画、字幕、読み上げ原稿、作業メモ、スクリーンショット、ビルド用ファイルは含めていません。

## 全10回

| 回 | テーマ | フォルダ |
|---:|---|---|
| 1 | 線形変換 | [`01_linear_transform`](01_linear_transform/) |
| 2 | 活性化関数 | [`02_activation_functions`](02_activation_functions/) |
| 3 | 損失関数 | [`03_loss_functions`](03_loss_functions/) |
| 4 | 勾配降下法 | [`04_gradient_descent`](04_gradient_descent/) |
| 5 | 誤差逆伝播 | [`05_backpropagation`](05_backpropagation/) |
| 6 | 最適化手法 | [`06_optimizers`](06_optimizers/) |
| 7 | 過学習と正則化 | [`07_regularization`](07_regularization/) |
| 8 | CNN | [`08_cnn`](08_cnn/) |
| 9 | RNN / LSTM | [`09_rnn_lstm`](09_rnn_lstm/) |
| 10 | Attention / Transformer | [`10_attention_transformer`](10_attention_transformer/) |

## 基本的な使い方

1. 各回フォルダのデモ用Excelファイルを開きます。
2. 入力シートで、値や表示設定を確認します。
3. 外部PythonコードをPython in Excelのセルへ貼り付けて実行します。
4. 返された表を見て、入力変更による結果の変化を確認します。
5. 説明スライドとデモ操作解説スライドで、計算の意味と操作手順を確認します。

## 注意

この教材は、ディープラーニングの基礎計算を小さな表で確認するための補助教材です。実務用モデルの学習や推論をそのまま再現するものではありません。
