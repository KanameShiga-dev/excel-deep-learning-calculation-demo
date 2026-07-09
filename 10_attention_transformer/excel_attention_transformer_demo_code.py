import pandas as pd
import numpy as np

token_df = xl("'01_INPUT'!A6:F9", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!H6:J9", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "weights")
query_token = settings.get("query_token", str(token_df["token"].iloc[0]))
temperature = float(settings.get("temperature", 1.0))
if temperature <= 0:
    raise ValueError("temperature は0より大きい値にしてください")

q = token_df.loc[token_df["token"].astype(str) == query_token, ["q1", "q2"]].astype(float).to_numpy()[0]
k = token_df[["k1", "k2"]].astype(float).to_numpy()
v = token_df[["v"]].astype(float).to_numpy().reshape(-1)
scores = (k @ q) / np.sqrt(len(q)) / temperature
weights = np.exp(scores - scores.max())
weights = weights / weights.sum()
weighted_values = weights * v
context = float(weighted_values.sum())

qkv_vector_df = token_df.copy()
qkv_vector_df["selected_as_query"] = qkv_vector_df["token"].astype(str) == query_token
attention_score_df = pd.DataFrame({
    "query_token": query_token,
    "key_token": token_df["token"],
    "q1": round(float(q[0]), 4),
    "q2": round(float(q[1]), 4),
    "k1": np.round(k[:, 0], 4),
    "k2": np.round(k[:, 1], 4),
    "score": np.round(scores, 4),
})
attention_weight_df = attention_score_df.copy()
attention_weight_df["attention_weight"] = np.round(weights, 4)
attention_weight_df["rank"] = attention_weight_df["attention_weight"].rank(ascending=False, method="dense").astype(int)
context_vector_df = pd.DataFrame({
    "query_token": query_token,
    "key_token": token_df["token"],
    "value": np.round(v, 4),
    "attention_weight": np.round(weights, 4),
    "weighted_value": np.round(weighted_values, 4),
    "context_value": round(context, 4),
})
e_exam_point_df = pd.DataFrame([
    {"point": "QK_score", "read_as": "QueryとKeyの近さをscoreにする"},
    {"point": "softmax", "read_as": "scoreをAttention weightに変える"},
    {"point": "context", "read_as": "weightでValueを加重平均する"},
    {"point": "transformer_scope", "read_as": "この回ではTransformer全体ではなくAttentionの核を見る"},
])

if display_mode == "qkv":
    result_df = qkv_vector_df
elif display_mode == "scores":
    result_df = attention_score_df
elif display_mode == "context":
    result_df = context_vector_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = attention_weight_df

result_df
