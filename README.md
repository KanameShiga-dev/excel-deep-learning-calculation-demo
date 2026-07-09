# Excelで体験するディープラーニングの計算しくみ

## シリーズの位置づけ

このシリーズは、Excelを学習者向けUI、外部Pythonを計算本体として使い、ディープラーニングで頻出する基礎計算を小さな表で体験する全10回の教材シリーズです。

順伝播、損失、勾配、最適化、正則化、CNN、RNN、Attentionなど、ディープラーニングの学習でつまずきやすい計算の流れを、Excelの表とPythonの計算結果を対応づけながら確認します。

## 対象者

- ディープラーニングの基礎を学びたい人
- 順伝播、損失、勾配、最適化などの計算の土台を作りたい人
- 数式だけでは処理の流れを追いにくい人
- Pythonコードだけでは中間計算を見失いやすい人
- Excel上の入力とPythonの出力を対応づけて理解したい人

## 制作方針

- Excelは入力、設定、確認のUIとして使う。
- 計算本体は外部 `.py` のPythonコードで行う。
- 外部 `.py` は学習者向け入力値、設定値、確認表を `xl(...)` でWorkbookから読む。
- Pythonコード内だけに、Excel上の入力値と同じ固定データを再定義しない。
- 各回で「Excelのどこを変えると、Pythonの出力がどう変わるか」を明確にする。
- 各回で「どの入力を変えると、どの表がどう変わるか」を確認できるようにする。

## 公開対象

GitHub公開対象は各回ごとに最小セットのみとします。

- `excel_<theme>_demo.xlsx`
- `excel_<theme>_demo_code.py`
- `excel_<theme>_slides.pptx`
- `README.md`

公開対象に含めないもの:

- 動画
- 字幕
- 読み上げ原稿
- 作業メモ
- スクリーンショット
- `.build/`
- 一時ファイル
- 重複コピー

## 全10回ロードマップ

| 回 | テーマ | 基礎範囲 | 主な体験 |
|---|---|---|---|
| 1 | 線形変換 | 順伝播型ネットワーク、行列計算 | `y = Wx + b` の積和とバイアスを表で追う |
| 2 | 活性化関数 | 非線形変換、出力範囲、勾配 | Sigmoid, tanh, ReLU, Softmaxの違いを見る |
| 3 | 損失関数 | 学習目的関数、分類/回帰の誤差 | 予測と正解のズレがLossになる流れを見る |
| 4 | 勾配降下法 | 最適化の基礎、学習率 | パラメータ更新とLoss推移を見る |
| 5 | 誤差逆伝播 | Chain Rule、勾配計算 | forwardからbackwardまで小ネットワークで追う |
| 6 | 最適化手法 | SGD, Momentum, AdaGrad, RMSProp, Adam | 同じ勾配でも更新量が変わることを見る |
| 7 | 過学習と正則化 | 汎化、L1/L2、Dropout、Early Stopping | 訓練Lossと検証Lossの違いを見る |
| 8 | CNN | 畳み込みニューラルネットワーク | 小さな画像行列から特徴マップを作る |
| 9 | RNN / LSTM | リカレントニューラルネットワーク | 時系列入力とhidden state、ゲートを追う |
| 10 | Attention / Transformer総復習 | Transformer、Attention | Q/K/V、Attention weight、contextを確認する |

## 各回の状態

| 回 | テーマ | 状態 | 備考 |
|---|---|---|---|
| 1 | 線形変換 | 作成済み | `y = Wx + b` の積和とバイアスを確認 |
| 2 | 活性化関数 | 作成済み | Sigmoid、tanh、ReLU、Softmax、`p - y` を確認 |
| 3 | 損失関数 | 作成済み | MSE、Binary Cross Entropy、Cross Entropyを確認 |
| 4 | 勾配降下法 | 作成済み | 学習率、更新式、Loss推移を確認 |
| 5 | 誤差逆伝播 | 作成済み | forwardからbackwardへの勾配の流れを確認 |
| 6 | 最適化手法 | 作成済み | SGD、Momentum、AdaGrad、RMSProp、Adamを比較 |
| 7 | 過学習と正則化 | 作成済み | L1/L2、Dropout、Early Stoppingを確認 |
| 8 | CNN | 作成済み | filter、padding、stride、特徴マップを確認 |
| 9 | RNN / LSTM | 作成済み | forget/input/output gateと状態更新を確認 |
| 10 | Attention / Transformer | 作成済み | Q/K/V、score、weight、contextを確認 |
