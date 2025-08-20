# chart.py
# Author: Data Scientist
# Email: 21f3002792@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
n_customers = 200
data = pd.DataFrame({
    "Customer Segment": np.random.choice(["Regular", "Premium", "VIP"], size=n_customers, p=[0.5, 0.3, 0.2]),
    "Monthly Spending ($)": np.concatenate([
        np.random.normal(200, 50, int(n_customers*0.5)),
        np.random.normal(500, 80, int(n_customers*0.3)),
        np.random.normal(900, 120, int(n_customers*0.2))
    ])
})

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create boxplot
plt.figure(figsize=(8, 8))
ax = sns.boxplot(
    x="Customer Segment",
    y="Monthly Spending ($)",
    data=data,
    palette="Set2",
    width=0.6
)

ax.set_title("Customer Monthly Spending Distribution", fontsize=18, weight="bold")
ax.set_xlabel("Customer Segment", fontsize=14)
ax.set_ylabel("Spending ($)", fontsize=14)

# Save as 512x512 px
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
