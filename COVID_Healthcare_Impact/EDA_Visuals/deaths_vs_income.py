import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
deaths_raw = pd.read_csv('../Final_Exports/Cleaned_US_COVID_Deaths_By_County.csv')
income = pd.read_csv('../Final_Exports/06_Save_Cleaned_Median_Income_CSV.png.csv')

# Convert death columns to numeric
deaths_raw.iloc[:, 1:] = deaths_raw.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# ✅ Convert cumulative totals to daily new deaths
deaths_raw.iloc[:, 1:] = deaths_raw.iloc[:, 1:].diff(axis=1)

# Melt to long format: County | Date | Deaths
deaths_long = deaths_raw.melt(id_vars='County', var_name='Date', value_name='Deaths')
deaths_long['Date'] = pd.to_datetime(deaths_long['Date'], errors='coerce')
deaths_long = deaths_long.dropna(subset=['Date'])

# Extract Year and Month
deaths_long['Year'] = deaths_long['Date'].dt.year
deaths_long['Month'] = deaths_long['Date'].dt.month

# Group by County + Year + Month
monthly_deaths = deaths_long.groupby(['County', 'Year', 'Month'])['Deaths'].sum().reset_index()

# Create YearMonth label (optional)
monthly_deaths['YearMonth'] = monthly_deaths['Year'].astype(str) + '-' + monthly_deaths['Month'].astype(str).str.zfill(2)

# Calculate average monthly deaths per county
avg_deaths = monthly_deaths.groupby('County')['Deaths'].mean().reset_index()
avg_deaths.rename(columns={'Deaths': 'Avg_Monthly_Deaths'}, inplace=True)

# ✅ Clean and standardize county names
avg_deaths['County'] = avg_deaths['County'].str.strip().str.replace(' County', '', regex=False).str.lower()
income['County'] = income['County'].str.strip().str.replace(' County', '', regex=False).str.lower()

# Merge with income
merged = pd.merge(avg_deaths, income, on='County', how='inner')
merged['Median_Household_Income'] = pd.to_numeric(merged['Median_Household_Income'], errors='coerce')
merged = merged.dropna(subset=['Median_Household_Income'])

# 🔍 Debug
print("Merged DataFrame shape:", merged.shape)
print("Sample merged data:")
print(merged.head(10))

# 📊 Final Bar Chart: Realistic Avg Monthly Deaths with Caption
plt.figure(figsize=(14, 6))
sorted_data = merged.sort_values('Avg_Monthly_Deaths', ascending=False).reset_index(drop=True)

bar = sns.barplot(data=sorted_data, x='County', y='Avg_Monthly_Deaths', color='#4C72B0')

# Add data labels
for i, value in enumerate(sorted_data['Avg_Monthly_Deaths']):
    bar.text(i, value + 1, f"{int(value)} deaths", ha='center', va='bottom', fontsize=9)

# Set labels and title
plt.xticks(rotation=45, ha='right')
plt.ylabel('Avg Monthly COVID-19 Deaths (2020–2023)')
plt.xlabel('County')
plt.title('Average Monthly COVID-19 Deaths by NJ County')

# Add explanatory index below the chart
plt.figtext(0.5, -0.08,
    "Each bar represents the average number of newly reported COVID-19 deaths per month from 2020 to 2023.\nData grouped by county using cleaned CDC & Census datasets.",
    wrap=True, horizontalalignment='center', fontsize=9, style='italic')

plt.tight_layout()
plt.savefig('Realistic_Avg_Monthly_Deaths_BarChart.png', bbox_inches='tight')

# 📈 Scatter Plot: Income vs. Deaths
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged, x='Median_Household_Income', y='Avg_Monthly_Deaths', hue='County', s=100)

plt.title('Income vs. Avg Monthly COVID-19 Deaths (by County)')
plt.xlabel('Median Household Income ($)')
plt.ylabel('Average Monthly COVID-19 Deaths')
plt.tight_layout()
plt.savefig('Income_vs_Deaths_Scatter.png')
