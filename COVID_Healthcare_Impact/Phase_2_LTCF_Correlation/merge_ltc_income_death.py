import pandas as pd

# === Load Dataset 1: Avg Monthly Deaths + Income ===
base_df = pd.read_csv('../EDA_Visuals/merged_avg_monthly_deaths_income.csv')

# === Load Dataset 2: LTCF Deaths Summary ===
ltcf_df = pd.read_csv('LTCF_Deaths_Summary_By_County.csv')

# === Merge by County ===
merged = pd.merge(base_df, ltcf_df[['County', 'Total_LTCF_Deaths']], on='County', how='inner')

# === Output Check ===
print("\n✅ Merged Data Sample:")
print(merged.head())

# === Correlation Heatmap ===
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.heatmap(
    merged[['Avg_Monthly_Deaths', 'Median_Household_Income', 'Total_LTCF_Deaths']].corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation: LTCF Deaths, Income, Avg COVID Deaths")
plt.tight_layout()
plt.savefig('LTCF_Income_Deaths_Correlation_Heatmap.png')

# === Save Merged Dataset ===
merged.to_csv('LTCF_COVID_Impact_Merged.csv', index=False)
