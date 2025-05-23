import pandas as pd

# === Load LTCF Outbreak Dataset ===
ltcf_df = pd.read_csv('../Final_Exports/cleaned_COVID_outbreak_data.csv')

# === Step 1: Group LTCF Deaths by County ===
ltcf_grouped = ltcf_df.groupby('County')[['Confirmed_Resident_Deaths', 'Confirmed_Staff_Deaths']].sum().reset_index()

# Add total LTCF deaths
ltcf_grouped['Total_LTCF_Deaths'] = ltcf_grouped['Confirmed_Resident_Deaths'] + ltcf_grouped['Confirmed_Staff_Deaths']

# Standardize county names for merging later
ltcf_grouped['County'] = ltcf_grouped['County'].str.strip().str.lower().str.replace(' county', '', regex=False)

# === Output Debug Info ===
print("Grouped LTCF Deaths by County:")
print(ltcf_grouped.head())

# Optional: Save to CSV to verify manually
ltcf_grouped.to_csv('LTCF_Deaths_Summary_By_County.csv', index=False)
