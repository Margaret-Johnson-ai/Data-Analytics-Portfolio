import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load raw cleaned data with daily death columns
deaths_raw = pd.read_csv('../Final_Exports/Cleaned_US_COVID_Deaths_By_County.csv')
income = pd.read_csv('../Final_Exports/06_Save_Cleaned_Median_Income_CSV.png.csv')

# Sum all daily death columns to get total per county
deaths_raw.iloc[:, 1:] = deaths_raw.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
deaths_raw['Total_Deaths'] = deaths_raw.iloc[:, 1:].sum(axis=1)

# Keep only County and Total_Deaths
deaths = deaths_raw[['County', 'Total_Deaths']]

# Merge datasets
merged = pd.merge(deaths, income, on='County', how='inner')

# Create the bar chart
plt.figure(figsize=(14, 6))
sns.barplot(data=merged.sort_values('Total_Deaths', ascending=False), x='County', y='Total_Deaths', hue='Median_Household_Income')
plt.xticks(rotation=45, ha='right')
plt.title('COVID-19 Total Deaths by County (Colored by Median Household Income)')
plt.tight_layout()

# Save chart image
plt.savefig('COVID_Deaths_vs_Income_By_County.png')

