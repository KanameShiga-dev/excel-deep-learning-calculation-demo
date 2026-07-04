import pandas as pd
import numpy as np

gradient_df = xl("'01_INPUT'!A6:B10", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!D6:F12", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "compare")
lr = float(settings.get("learning_rate", 0.1))
momentum = float(settings.get("momentum", 0.9))
beta1 = float(settings.get("beta1", 0.9))
beta2 = float(settings.get("beta2", 0.999))
eps = float(settings.get("epsilon", 1e-8))

w_sgd = w_mom = w_adam = 0.0
v = 0.0
m = 0.0
s = 0.0
rows = []
for _, row in gradient_df.iterrows():
    step = int(row["step"])
    g = float(row["gradient"])
    w_sgd = w_sgd - lr * g
    v = momentum * v + lr * g
    w_mom = w_mom - v
    m = beta1 * m + (1 - beta1) * g
    s = beta2 * s + (1 - beta2) * (g ** 2)
    m_hat = m / (1 - beta1 ** step)
    s_hat = s / (1 - beta2 ** step)
    adam_update = lr * m_hat / (np.sqrt(s_hat) + eps)
    w_adam = w_adam - adam_update
    rows.append({"step": step, "gradient": g, "sgd_weight": round(w_sgd, 4), "momentum_weight": round(w_mom, 4), "adam_weight": round(w_adam, 4), "adam_update": round(float(adam_update), 4)})

optimizer_compare_df = pd.DataFrame(rows)
optimizer_state_df = optimizer_compare_df[["step", "gradient", "adam_update"]].copy()
e_exam_point_df = pd.DataFrame([
    {"point": "sgd", "read_as": "現在の勾配だけで更新する"},
    {"point": "momentum", "read_as": "過去の進む向きを速度として残す"},
    {"point": "adam", "read_as": "一次と二次の移動平均で更新量を調整する"},
])

if display_mode == "state":
    result_df = optimizer_state_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = optimizer_compare_df

result_df
