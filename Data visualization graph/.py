import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset from seaborn (a classic sample dataset)
tips = sns.load_dataset("tips")

# Set a style
sns.set(style="whitegrid")

# Create a visualization: Total bill vs tip, colored by time (Lunch/Dinner)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", palette="Set1")
plt.title("Tip Amount vs Total Bill (Lunch vs Dinner)", fontsize=14)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)
plt.legend(title="Meal Time")
plt.tight_layout()
plt.show()
