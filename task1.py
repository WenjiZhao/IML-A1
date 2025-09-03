import pandas as pd
import json
df = pd.read_csv("urbansound8k_features_small.csv")
rows = df.shape[0]
cols = df.shape[1]

class_counts = df['class'].value_counts().to_dict()

info = {
    "Total number of rows:" : rows,
    "Total number of columns:" : cols,
    "Class counts:" : class_counts
}

with open("task1_summary.json", "w", encoding="utf-8") as outfile:
    json.dump(info, outfile, indent=4)

print(json.dumps(info, indent=4))
