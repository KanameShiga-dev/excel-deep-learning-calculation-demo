import pandas as pd
import numpy as np

activation_input_df = xl("'01_INPUT'!A6:B14", headers=True).dropna(how="all")
softmax_input_df = xl("'01_INPUT'!D6:E9", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!G6:I9", headers=True).dropna(how="all")

activation_input_df["input_value"] = activation_input_df["input_value"].astype(float)
softmax_input_df["logit"] = softmax_input_df["logit"].astype(float)

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "activation")
selected_function = settings.get("selected_function", "relu")
temperature = float(settings.get("temperature", 1.0))
target_class = settings.get("target_class", str(softmax_input_df["class_name"].iloc[0]))
if temperature <= 0:
    raise ValueError("temperature は0より大きい値にしてください")

x = activation_input_df["input_value"].to_numpy(dtype=float)
sigmoid = 1.0 / (1.0 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0.0, x)

activation_df = activation_input_df.copy()
activation_df["sigmoid"] = np.round(sigmoid, 4)
activation_df["tanh"] = np.round(tanh, 4)
activation_df["relu"] = np.round(relu, 4)
activation_df["sigmoid_grad"] = np.round(sigmoid * (1.0 - sigmoid), 4)
activation_df["tanh_grad"] = np.round(1.0 - tanh**2, 4)
activation_df["relu_grad"] = np.where(x > 0, 1.0, 0.0)

gradient_df = activation_df[
    [
        "input_value",
        "sigmoid_grad",
        "tanh_grad",
        "relu_grad",
    ]
].copy()

if selected_function == "sigmoid":
    activation_df["selected_output"] = activation_df["sigmoid"]
    activation_df["selected_gradient"] = activation_df["sigmoid_grad"]
elif selected_function == "tanh":
    activation_df["selected_output"] = activation_df["tanh"]
    activation_df["selected_gradient"] = activation_df["tanh_grad"]
else:
    activation_df["selected_output"] = activation_df["relu"]
    activation_df["selected_gradient"] = activation_df["relu_grad"]

logits = softmax_input_df["logit"].to_numpy(dtype=float) / temperature
shifted = logits - logits.max()
exp_shifted = np.exp(shifted)
probability = exp_shifted / exp_shifted.sum()

softmax_df = softmax_input_df.copy()
softmax_df["temperature"] = temperature
softmax_df["shifted_logit"] = np.round(shifted, 4)
softmax_df["exp_shifted"] = np.round(exp_shifted, 4)
softmax_df["probability"] = np.round(probability, 4)
softmax_df["rank"] = softmax_df["probability"].rank(ascending=False, method="dense").astype(int)

target = (softmax_input_df["class_name"].astype(str) == target_class).astype(float).to_numpy()
if target.sum() != 1:
    raise ValueError("target_class はSoftmax用logit表のclass_nameから1つ選んでください")

softmax_ce_grad_df = softmax_df[["class_name", "logit", "probability"]].copy()
softmax_ce_grad_df["target_class"] = target_class
softmax_ce_grad_df["target"] = target.astype(int)
softmax_ce_grad_df["dLoss_dlogit"] = np.round(probability - target, 4)
softmax_ce_grad_df["read_as"] = np.where(
    softmax_ce_grad_df["target"] == 1,
    "正解クラスは probability - 1",
    "不正解クラスは probability",
)

e_exam_point_df = pd.DataFrame(
    [
        {"point": "nonlinearity", "read_as": "線形変換のscoreをそのまま渡さず、非線形に変える"},
        {"point": "gradient", "read_as": "入力が大きすぎるとSigmoidやtanhの勾配が小さくなる"},
        {"point": "relu", "read_as": "0以下は0、0より大きい値はそのまま通す"},
        {"point": "softmax", "read_as": "複数logitを合計1の確率のような値に変える"},
        {"point": "softmax_ce_grad", "read_as": "SoftmaxとCross Entropyを合わせるとp-yになる"},
    ]
)

if display_mode == "softmax_ce_grad":
    result_df = softmax_ce_grad_df
elif display_mode == "softmax":
    result_df = softmax_df
elif display_mode == "gradient":
    result_df = gradient_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = activation_df

result_df
