# Unequal Burden: COVID-19’s Disproportionate Impact on NJ Healthcare Systems and Underserved Communities

## 📌 Project Overview
This project was created to help me explore how the COVID-19 pandemic affected healthcare systems across New Jersey, especially in low-income and underserved communities. As someone new to data analysis and passionate about public health, I wanted to dig into real-world data to better understand how access to care and hospital resources differed between counties.

Throughout this project, I worked with open datasets to look at hospitalization numbers, death rates, and population data. My goal was to compare these factors across different counties and income levels to see where the healthcare system may have been under the most pressure. I also wanted to use this project to grow my technical skills while asking meaningful questions about equity and preparedness during a public health crisis.

## 🌟 Objectives
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

## 📂 Data Sources
- [US COVID-19 Time Series Deaths by County – Johns Hopkins University GitHub](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv)
- [COVID-19 Outbreaks in NJ Long-Term Care Facilities – NJ Department of Health](https://www.nj.gov/health/covid-19/information/data-and-dashboards/#COVID-19-Dashboard)
- [NJ Median Household Income by County – census.gov](#)

## 🧪 Key Metrics
- Hospitalizations per 10,000 residents
- Deaths per 1,000 confirmed infections
- County income classification (low, medium, high)
- LTC facility-level outbreaks and conclusion dates

## 📊 Visualizations
_Screenshots and charts will be added here after I complete the analysis phase._

## 📈 Results & Findings
_This section will be updated after running the data workflows and analyzing results._

## 💡 Conclusion
Coming soon! I’ll share what I learned, what stood out, and how this project helped me grow as a beginner in data analytics and public health research.

# 📊 COVID-19 Healthcare Impact Data Project

## 🗂️ Project Overview
This project analyzes the impact of COVID-19 on long-term care (LTC) facilities in New Jersey, focusing on confirmed cases and deaths among residents and staff. Using KNIME Analytics Platform, we cleaned, transformed, and prepared the dataset for further insights and visualization.

---

## ✅ Dataset 1: `COVID_outbreak_data.csv`

### 🔄 Data Cleaning & Processing Steps (Step-by-step in KNIME):

1. **Excel Reader Node**: Imported the raw dataset.
2. **RowID Node**: Created a unique RowID for tracking.
3. **Rule-based Row Filter Node**: Removed the top 2 non-data rows (e.g., titles or notes).
4. **Column Renamer Node**: Renamed columns for clarity and consistency:
   - `empty_F` ➔ `Confirmed_Resident_Cases`
   - `empty_G` ➔ `Confirmed_Staff_Cases`
   - `empty_H` ➔ `Confirmed_Resident_Deaths`
   - `empty_I` ➔ `Confirmed_Staff_Deaths`
   - `empty_J` ➔ `Reported_Date`
   - `empty_K` ➔ `Concluded_Date`
   - `NEW JERSEY COVID-19 CASES...` ➔ `County`
5. **Column Filter Node**: Removed unnecessary columns like `E-Number`, `Type`, `Row_Index`.
6. **Missing Value Node**: Replaced missing values in numeric fields with 0.
7. **String to Number Node**: Converted text-based numeric columns to Integer.
8. **CSV Writer Node**: Saved final cleaned dataset as:
   - 📁 `Final_Exports/cleaned_COVID_outbreak_data.csv`

### ✅ Final Columns in Clean Dataset:
- RowID
- Facility_Name
- Municipality
- Confirmed_Resident_Cases
- Confirmed_Staff_Cases
- Confirmed_Resident_Deaths
- Confirmed_Staff_Deaths
- Reported_Date
- County
- Concluded_Date

---

## ✅ Dataset 2: `a51fc77c-2e0d-4f62-9e50-9d850aeba0ab.xlsx`

### 🔄 Data Cleaning & Processing Steps (Overview):

1. **Loaded via Excel Reader Node**.
2. **Initial inspection** to check for usable structure.
3. **Confirmed content as needed and ready for merging** or further independent use.
4. **Saved in Raw_Data folder** for ongoing processing.

> _Full transformation workflow will be added once cleaning steps are finalized._

---

## 📁 Folder Structure:
```
COVID_Healthcare_Impact/
├── Final_Exports/
│   └── cleaned_COVID_outbreak_data.csv
├── Raw_Data/
│   └── a51fc77c-2e0d-4f62-9e50-9d850aeba0ab.xlsx
├── KNIME_Workflows/
│   └── (Documented workflows)
└── README.md
```

---

## 📌 Next Steps
- [ ] Load third dataset: NJ LTC Vaccination & Staffing Rates
- [ ] Clean and transform data
- [ ] Merge datasets if needed
- [ ] Begin analysis and visualization
- [ ] Summarize findings for storytelling

---

## 🔧 Tools Used
- KNIME Analytics Platform 5
- CSV Writer & Reader
- Rule-based Row Filter
- String to Number
- Column Renamer & Filter
- Missing Value Handler

---

## 🧠 Author Notes
This project is part of a data analytics portfolio designed to showcase real-world cleaning, wrangling, and data pipeline management skills using visual workflow tools like KNIME.

️✅ Last updated: May 20, 2025
