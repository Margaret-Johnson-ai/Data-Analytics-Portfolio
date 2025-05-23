# 🩺 COVID-19 Healthcare Impact in New Jersey  
_A Data Cleaning & Analysis Project_

---

## 🎯 Project Purpose

This project investigates how COVID-19 impacted healthcare systems and outcomes across counties in New Jersey. By combining data from federal and state health sources, the goal is to uncover how death rates, hospital resource usage, and county income levels are interrelated.

---

## ❓ Key Questions to Answer During Analysis

- What counties experienced the **highest COVID-19 death rates**?
- Is there a relationship between **income level** and **COVID-19 mortality**?
- Did counties with **higher ICU utilization** experience more fatalities?
- Which counties were **most vulnerable** based on combined metrics?

These questions will be addressed during the Exploratory Data Analysis (EDA) phase.

---

## 📂 Datasets Used

| Dataset                                 | Source                                                                                          | Description                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `US_COVID_Deaths_Cleaned.csv`          | [CDC - COVID-19 Deaths by County](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-County-and-Race/k8wy-p9cg) | County-level death counts filtered for NJ       |
| `NJ_Hospital_Utilization.csv`          | [NJ Department of Health](https://www.nj.gov/health/)                                           | ICU/general bed occupancy trends                |
| `NJ_Median_Income_by_County.csv`       | [U.S. Census Bureau](https://www.census.gov/data.html)                                          | Median household income by NJ county            |

---

## 🛠 Tools Used

- **KNIME Analytics Platform** – for data cleaning, workflow design, and automation  
- **Python** – for CSV validation and previewing cleaned datasets  
- **GitHub** – for version control, project portfolio, and documentation  
- **Command Prompt (CMD)** – for Git operations and local repository management  
- **Notepad** – for quick edits to markdown files and manual code updates

---

## 📸 Project Screenshots

### 🧼 Dataset 1: NJ Long-Term Care Facility Outbreaks

![Raw Excel Preview](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/01_Raw_LTC_Excel_Preview.png.png)  
![Import LTC Data](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/01_Import_LTC_Data_CSV_Reader.png.png)  
![Filter NJ Rows](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/02_Filter_LTC_New_Jersey_Rows.png.png)  
![Save Raw CSV](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/02_Save_Raw_CSV_Proper_Format.png.png)  
![Filtered Output](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/03_Filtered_NJ_LTC_Records_Output.png.png)  
![Raw Structure](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/04_LTC_Raw_Structure_Preview.png.png)  
![RowID](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/05_Add_RowID_LTC_Data.png.png)  
![Rename Columns](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/06_Rename_LTC_Columns.png.png)  
![Renamed Output](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/07_Renamed_LTC_Columns_Output.png.png)  
![Cleaned Data](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/08_Filtered_LTC_Cleaned_Output.png.png)  
![Missing Values](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/09_Missing_Values_LTC.png.png)  
![Data Type Conversion](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/10_DataType_Converted_LTC.png.png)  
![Final Table](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/11_Final_LTC_Cleaned_Table.png.png)

---

### 🧼 Dataset 2: NJ Median Household Income

![Load CSV](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/01_Load_Median_Income_CSV.png.png)  
![Filter Columns](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/02_Filter_Columns_Income.png.png)  
![Rename Columns](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/03_Rename_Columns_Income.png.png)  
![Regex Clean Names](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/04_Clean_County_Names_Regex.png.png)  
![Remove Header Rows](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/05a_Remove_Header_Rows.png.png)  
![Filter Valid Rows](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/05b_Filter_Valid_Income_Rows.png.png)  
![Remove Commas](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/05c_Remove_Commas_StringManipulation.png.png)  
![Convert to Numbers](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/05d_Convert_Income_To_Number.png.png)  
![Save CSV](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/06_Save_Cleaned_Income_CSV.png.png)

---

### 🧼 Dataset 3: US COVID Deaths by County (NJ Only)

![Read CSV](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/01_Read_US_COVID_Deaths_CSV.png.png)  
![Filter NJ Rows](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/02_Filter_New_Jersey_Rows.png.png)  
![Remove Columns](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/03_Remove_Unnecessary_Columns_Deaths.png.png)  
![Rename Admin2](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/04_Rename_Admin2_To_County.png.png)  
![Missing Values](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/05_Handle_Missing_Values_Deaths.png.png)  
![Save Cleaned CSV](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/06_Save_Cleaned_US_Deaths_CSV.png.png)

---

## 📊 Exploratory Data Analysis (EDA)

### COVID-19 Total Deaths vs. Median Household Income

![COVID Deaths vs Income](EDA_Visuals/COVID_Deaths_vs_Income_By_County.png)

- Counties with **lower median household incomes** experienced **higher total COVID-19 deaths**.
- The bar chart reveals a potential **negative correlation** between income level and pandemic outcomes.
- This insight highlights how **socioeconomic factors** may influence vulnerability during health crises.

**Data Sources:**
- [CDC COVID-19 Deaths by County](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-County-and-Ra/k8wy-p9cg)
- [U.S. Census Bureau – Median Household Income](https://www.census.gov/)

---

## 🧠 What I Learned

- How to structure, filter, and clean public health datasets in KNIME  
- How to apply logic nodes, string manipulation, and regex in workflows  
- How to document the full process using GitHub with screenshots and commits  
- How to visualize real-world healthcare patterns using Python and Seaborn

---

## 🚧 Next Steps (Phase 2: Exploratory Data Analysis – EDA)

✅ Bar chart: COVID deaths vs income by county  
- [ ] Correlation heatmaps: death rate, ICU use, income  
- [ ] Identify county-level risk clusters  
- [ ] Add remaining visuals to `EDA_Visuals/` and document findings

---

## 📌 Summary

This project demonstrates practical skills in real-world data cleaning, exploratory analysis, documentation, and portfolio storytelling. I've completed the first visual insight showing the relationship between county income and COVID-19 deaths, and will continue analyzing healthcare impact using additional statistical and visual tools.

Stay tuned for heatmaps, correlations, and deeper insights in the next push!
