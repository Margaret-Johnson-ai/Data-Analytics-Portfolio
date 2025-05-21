# Unequal Burden: COVID-19’s Disproportionate Impact on NJ Healthcare Systems

## 👋 About This Project
As an aspiring data analyst passionate about public health, I built this portfolio project to explore how the COVID-19 pandemic disproportionately impacted New Jersey counties — especially low-income and underserved communities. Using KNIME and real-world datasets, I walked through hands-on cleaning, transformation, and analysis techniques to extract insights from healthcare and demographic data.

---

## 🎯 Project Objectives
- Explore and compare hospitalization and death rates across NJ counties during COVID-19
- Identify how outcomes may differ between low-income and high-income areas
- Visualize geographic differences in healthcare burden
- Practice using data to suggest ways to better prepare for future emergencies

## ❓ Core Questions This Project Answers
1. Which New Jersey counties experienced the most strain on their hospitals relative to their population size?
2. Is there a clear link between hospital capacity and COVID-19 death rates?
3. Were lower-income counties hit harder in terms of access to care and overall outcomes?
4. What can this data tell us about how to improve support and resources for under-resourced areas in future health emergencies?

## 🛠️ Tools Used
- KNIME – for cleaning, joining, and transforming datasets
- Excel – for data review and optional dashboards
- Tableau Public – for visualizations (optional)
- GitHub – for sharing my work and documenting the project

- Analyze hospitalization and death patterns across NJ counties
- Compare outcomes by income level and population density
- Build KNIME pipelines to clean and structure public datasets
- Develop storytelling skills using real data from credible sources

---

## 🧵 Datasets Cleaned & Documented

### 🧼 Dataset 1: COVID-19 NJ Long-Term Care Facilities  
**Source:** [NJ Department of Health – LTC Data](https://www.nj.gov/health/covid-19/long-term-care/index.shtml)  
**File:** `COVID_outbreak_data.csv`

<details>
<summary>📋 Cleaning Steps</summary>

- Imported Excel using Excel Reader  
- Removed top metadata rows  
- Renamed empty columns (e.g., `empty_F` → `Confirmed_Resident_Cases`)  
- Filtered unnecessary columns  
- Replaced missing values with `0`  
- Converted strings to numbers  
- Exported cleaned CSV  

📁 `Final_Exports/cleaned_COVID_outbreak_data.csv`  
🖼️ `Screenshots/01_Load_Excel_Reader.png`, etc.

</details>

---

### 🧼 Dataset 2: NJ Median Household Income by County  
**Source:** [U.S. Census Bureau – ACS Data](https://data.census.gov/)  
**File:** `ACSST5Y2022.S1903-Data.csv`

<details>
<summary>📋 Cleaning Steps</summary>

- Filtered to keep only `NAME` and `S1903_C03_001E`  
- Renamed: `NAME` → `County`, `S1903_C03_001E` → `Median_Household_Income`  
- Removed “, New Jersey” from county names  
- Filtered out metadata rows  
- Cleaned commas/spaces  
- Converted strings to numbers  
- Exported cleaned CSV  

📁 `Final_Exports/NJ_Median_Income_By_County_Cleaned.csv`  
🖼️ `Screenshots/05c_StringManipulation_RemoveCommas.png`

</details>

---

### 🧼 Dataset 3: US COVID-19 Deaths by County (NJ Filtered)  
**Source:** [Johns Hopkins GitHub – COVID Deaths Time Series](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv)  
**File:** `US_COVID_Deaths_By_County.csv`

<details>
<summary>📋 Cleaning Steps</summary>

- Imported CSV via `CSV Reader`  
- Filtered rows where `Province_State = New Jersey`  
- Retained only `Admin2` (County) and daily death columns  
- Renamed `Admin2` to `County`  
- Handled missing values (confirmed none)  
- Exported cleaned CSV  

📁 `Final_Exports/Cleaned_US_COVID_Deaths_By_County.csv`  
🖼️ `Screenshots/06_Save_Cleaned_US_Deaths_CSV.png`

</details>

---

## 📁 Folder Structure

```
COVID_Healthcare_Impact/
├── Final_Exports/
│   ├── cleaned_COVID_outbreak_data.csv
│   ├── NJ_Median_Income_By_County_Cleaned.csv
│   └── Cleaned_US_COVID_Deaths_By_County.csv
├── Raw_Datasets/
│   ├── Original Excel/CSV files
├── Screenshots/
│   └── All KNIME workflow images
├── KNIME_Workflows/
│   └── Project pipelines
└── README.md
```

---

## 📊 Key Metrics Being Analyzed
- Deaths per county (daily and cumulative)
- Median income by county
- LTC resident/staff case outcomes
- Population-adjusted impact measures

---

## 🧠 Reflections
This project helped me improve:
- Real-world dataset cleaning using KNIME
- Understanding of socioeconomic health disparities
- Documenting and showcasing data work on GitHub

I'm excited to continue expanding this project with dashboards, Tableau visualizations, and final analysis findings.

---

✅ **Last updated:** May 21, 2025  
📌 **Maintainer:** Margaret Johnson  
🔗 [View on GitHub](https://github.com/Margaret-Johnson-ai/Data-Analytics-Portfolio/tree/main/COVID_Healthcare_Impact)
