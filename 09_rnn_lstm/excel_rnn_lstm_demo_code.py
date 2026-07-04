import pandas as pd
import numpy as np

sequence_df = xl("'01_INPUT'!A6:B10", headers=True).dropna(how="all")
param_df = xl("'01_INPUT'!D6:E14", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!G6:I8", headers=True).dropna(how="all")

params = dict(zip(param_df["parameter"].astype(str), param_df["value"].astype(float)))
settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "sequence")

h = params["h0"]
c = params["c0"]
rows = []
for _, row in sequence_df.iterrows():
    t = int(row["time_step"])
    x = float(row["input_value"])
    forget_gate = 1.0 / (1.0 + np.exp(-(params["wf"] * x + params["uf"] * h)))
    input_gate = 1.0 / (1.0 + np.exp(-(params["wi"] * x + params["ui"] * h)))
    candidate = np.tanh(params["wc"] * x + params["uc"] * h)
    c = forget_gate * c + input_gate * candidate
    h = np.tanh(c)
    rows.append({"time_step": t, "input_value": x, "forget_gate": round(float(forget_gate), 4), "input_gate": round(float(input_gate), 4), "candidate": round(float(candidate), 4), "cell_state": round(float(c), 4), "hidden_state": round(float(h), 4)})

gate_trace_df = pd.DataFrame(rows)
sequence_trace_df = gate_trace_df[["time_step", "input_value", "hidden_state"]].copy()
e_exam_point_df = pd.DataFrame([
    {"point": "hidden_state", "read_as": "過去情報を持ち回る値"},
    {"point": "forget_gate", "read_as": "前のcellをどれだけ残すか"},
    {"point": "input_gate", "read_as": "新しい候補をどれだけ入れるか"},
])

if display_mode == "gate":
    result_df = gate_trace_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = sequence_trace_df

result_df
