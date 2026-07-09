import pandas as pd
import numpy as np

gradient_df = xl("'01_INPUT'!A6:B10", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!D6:F13", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "compare")
lr = float(settings.get("learning_rate", 0.1))
momentum = float(settings.get("momentum", 0.9))
rms_decay = float(settings.get("rms_decay", 0.9))
beta1 = float(settings.get("beta1", 0.9))
beta2 = float(settings.get("beta2", 0.999))
eps = float(settings.get("epsilon", 1e-8))

w_sgd = w_mom = w_adagrad = w_rmsprop = w_adam = 0.0
v_mom = 0.0
adagrad_sum_sq = 0.0
rmsprop_cache = 0.0
m = 0.0
s = 0.0
rows = []
state_rows = []
for _, row in gradient_df.iterrows():
    step = int(row["step"])
    g = float(row["gradient"])

    sgd_update = lr * g
    w_sgd = w_sgd - sgd_update

    v_mom = momentum * v_mom + lr * g
    w_mom = w_mom - v_mom

    adagrad_sum_sq = adagrad_sum_sq + g ** 2
    adagrad_update = lr * g / (np.sqrt(adagrad_sum_sq) + eps)
    w_adagrad = w_adagrad - adagrad_update

    rmsprop_cache = rms_decay * rmsprop_cache + (1 - rms_decay) * (g ** 2)
    rmsprop_update = lr * g / (np.sqrt(rmsprop_cache) + eps)
    w_rmsprop = w_rmsprop - rmsprop_update

    m = beta1 * m + (1 - beta1) * g
    s = beta2 * s + (1 - beta2) * (g ** 2)
    m_hat = m / (1 - beta1 ** step)
    s_hat = s / (1 - beta2 ** step)
    adam_update = lr * m_hat / (np.sqrt(s_hat) + eps)
    w_adam = w_adam - adam_update

    rows.append({
        "step": step,
        "gradient": g,
        "sgd_weight": round(float(w_sgd), 4),
        "momentum_weight": round(float(w_mom), 4),
        "adagrad_weight": round(float(w_adagrad), 4),
        "rmsprop_weight": round(float(w_rmsprop), 4),
        "adam_weight": round(float(w_adam), 4),
    })
    state_rows.append({
        "step": step,
        "gradient": g,
        "sgd_update": round(float(sgd_update), 4),
        "momentum_update": round(float(v_mom), 4),
        "adagrad_sum_sq": round(float(adagrad_sum_sq), 4),
        "adagrad_update": round(float(adagrad_update), 4),
        "rmsprop_cache": round(float(rmsprop_cache), 4),
        "rmsprop_update": round(float(rmsprop_update), 4),
        "adam_m": round(float(m), 4),
        "adam_s": round(float(s), 4),
        "adam_update": round(float(adam_update), 4),
    })

optimizer_compare_df = pd.DataFrame(rows)
optimizer_state_df = pd.DataFrame(state_rows)
path_summary_df = pd.DataFrame([
    {"method": "SGD", "final_weight": round(float(w_sgd), 4)},
    {"method": "Momentum", "final_weight": round(float(w_mom), 4)},
    {"method": "AdaGrad", "final_weight": round(float(w_adagrad), 4)},
    {"method": "RMSProp", "final_weight": round(float(w_rmsprop), 4)},
    {"method": "Adam", "final_weight": round(float(w_adam), 4)},
])
e_exam_point_df = pd.DataFrame([
    {"point": "sgd", "read_as": "現在の勾配だけで更新する"},
    {"point": "momentum", "read_as": "過去の進む向きを速度として残す"},
    {"point": "adagrad", "read_as": "過去の勾配二乗和で更新量を小さくする"},
    {"point": "rmsprop", "read_as": "勾配二乗の移動平均で更新量を調整する"},
    {"point": "adam", "read_as": "一次と二次の移動平均で更新量を調整する"},
])

if display_mode == "state":
    result_df = optimizer_state_df
elif display_mode == "summary":
    result_df = path_summary_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = optimizer_compare_df

result_df
