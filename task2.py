import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('urbansound8k_features_small.csv')

subset = df[df['class'].isin(['dog_bark', 'air_conditioner'])]

plt.figure(figsize = (8,8))
sns.violinplot(x = 'class', y = 'contrast0', data = subset)
plt.title("Violin plot of contrast0 for dog_bark and air_conditioner")
plt.ylabel("contrast0")
plt.xlabel("Class")
plt.savefig("task2_violin.png", dpi=300, bbox_inches='tight')
plt.show()
