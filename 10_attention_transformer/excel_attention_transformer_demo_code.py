import pandas as pd
import numpy as np

token_df = xl("'01_INPUT'!A6:D9", headers=True).dropna(how="all")
settings_df = xl("'01_INPUT'!F6:H8", headers=True).dropna(how="all")

settings = dict(zip(settings_df["setting"].astype(str), settings_df["value"].astype(str)))
display_mode = settings.get("display_mode", "weights")
query_token = settings.get("query_token", str(token_df["token"].iloc[0]))
temperature = float(settings.get("temperature", 1.0))

q = token_df.loc[token_df["token"].astype(str) == query_token, ["q1", "q2"]].astype(float).to_numpy()[0]
k = token_df[["q1", "q2"]].astype(float).to_numpy()
v = token_df[["v"]].astype(float).to_numpy().reshape(-1)
scores = (k @ q) / np.sqrt(len(q)) / temperature
weights = np.exp(scores - scores.max())
weights = weights / weights.sum()
context = float((weights * v).sum())

attention_score_df = pd.DataFrame({"query_token": query_token, "key_token": token_df["token"], "score": np.round(scores, 4)})
attention_weight_df = attention_score_df.copy()
attention_weight_df["attention_weight"] = np.round(weights, 4)
attention_weight_df["rank"] = attention_weight_df["attention_weight"].rank(ascending=False, method="dense").astype(int)
context_vector_df = pd.DataFrame([{"query_token": query_token, "context_value": round(context, 4)}])
e_exam_point_df = pd.DataFrame([
    {"point": "QK_score", "read_as": "QueryとKeyの近さをscoreにする"},
    {"point": "softmax", "read_as": "scoreをAttention weightに変える"},
    {"point": "context", "read_as": "weightでValueを加重平均する"},
])

if display_mode == "scores":
    result_df = attention_score_df
elif display_mode == "context":
    result_df = context_vector_df
elif display_mode == "exam":
    result_df = e_exam_point_df
else:
    result_df = attention_weight_df

result_df
