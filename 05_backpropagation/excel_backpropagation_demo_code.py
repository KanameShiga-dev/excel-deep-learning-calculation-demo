import pandas as pd
import numpy as np

input_df = xl("'01_INPUT'!A6:B8", headers=True).dropna(how="all")
param_df = xl("'01_INPUT'!D6:E10", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!G6:I8", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "forward")
params = dict(zip(param_df["parameter"].astype(str), param_df["value"].astype(float)))
x = float(input_df.loc[input_df["name"] == "x", "value"].iloc[0])
target = float(input_df.loc[input_df["name"] == "target", "value"].iloc[0])
w1, b1, w2, b2 = params["w1"], params["b1"], params["w2"], params["b2"]

z1 = x * w1 + b1
a1 = max(0.0, z1)
y = a1 * w2 + b2
loss = 0.5 * (y - target) ** 2

dL_dy = y - target
dL_dw2 = a1 * dL_dy
dL_db2 = dL_dy
dL_da1 = w2 * dL_dy
da1_dz1 = 1.0 if z1 > 0 else 0.0
dL_dz1 = dL_da1 * da1_dz1
dL_dw1 = x * dL_dz1
dL_db1 = dL_dz1

forward_trace_df = pd.DataFrame([
    {"node": "z1", "formula": "x*w1+b1", "value": round(z1, 4)},
    {"node": "a1", "formula": "ReLU(z1)", "value": round(a1, 4)},
    {"node": "y", "formula": "a1*w2+b2", "value": round(y, 4)},
    {"node": "loss", "formula": "0.5*(y-target)^2", "value": round(loss, 4)},
])
backward_trace_df = pd.DataFrame([
    {"gradient": "dL/dy", "value": round(dL_dy, 4)},
    {"gradient": "dL/dw2", "value": round(dL_dw2, 4)},
    {"gradient": "dL/db2", "value": round(dL_db2, 4)},
    {"gradient": "dL/dw1", "value": round(dL_dw1, 4)},
    {"gradient": "dL/db1", "value": round(dL_db1, 4)},
])
e_exam_point_df = pd.DataFrame([
    {"point": "chain_rule", "read_as": "後ろの勾配にlocal gradientを掛ける"},
    {"point": "relu_gate", "read_as": "z1が0以下なら前へ勾配を通さない"},
])

if display_mode == "backward":
    result_df = backward_trace_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = forward_trace_df

result_df
