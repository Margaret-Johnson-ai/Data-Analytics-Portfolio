# 🦠 COVID-19 Healthcare Impact: A County-Level Data Analysis Project (New Jersey)

This project explores the impact of COVID-19 on healthcare systems across New Jersey using real-world public health data. It focuses on data cleaning, integration, and visualization to uncover trends related to death rates, hospital utilization, and household income by county.

---

## 📂 Datasets Used

| Dataset                                 | Source                                                                                          | Description                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------|
| US_COVID_Deaths_Cleaned.csv            | [CDC - Provisional COVID-19 Death Counts](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-County-and-Race/k8wy-p9cg) | County-level death counts filtered for NJ       |
| NJ_Hospital_Utilization.csv            | [NJ Department of Health](https://www.nj.gov/health/)                                           | ICU bed availability, general bed usage         |
| NJ_Median_Income_by_County.csv         | [U.S. Census Bureau](https://www.census.gov/data.html)                                          | Median household income by NJ county            |

---

## 📸 Project Screenshots

### 🧼 Dataset 1: NJ Long-Term Care Facility Outbreaks
![Import LTC Data](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/01_Import_LTC_Data_CSV_Reader.png)
![Cleaned LTC Output](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/11_Final_LTC_Cleaned_Table.png)

---

### 🧼 Dataset 2: NJ Median Household Income
![Filter Columns](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/02_Filter_Columns_Income.png)
![Save Cleaned File](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/06_Save_Cleaned_Income_CSV.png)

---

### 🧼 Dataset 3: US COVID Deaths by County (NJ Only)
![Filter NJ Counties](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/02_Filter_New_Jersey_Rows.png)
![Save Cleaned CSV](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/06_Save_Cleaned_US_Deaths_CSV.png)

---

## 🛠 Tools Used

- **KNIME Analytics Platform** – Data wrangling, filtering, and cleaning
- **Python (pandas)** – Data preview and format validation
- **GitHub** – Version control, project documentation, and public portfolio

---

## 🧠 What I Learned

- How to extract and transform complex public datasets into clean, analyzable formats
- How to apply best practices for naming conventions, string manipulation, and value filtering in KNIME
- How to document data cleaning steps with visuals and descriptive commit history for transparency and reproducibility

---

## 🚧 Next Steps (Phase 2: EDA – Exploratory Data Analysis)

- [ ] Create bar charts showing COVID-19 deaths vs. income by county
- [ ] Generate correlation heatmaps between ICU bed use, death rates, and income levels
- [ ] Add all visuals under a new `/EDA_Visuals/` folder
- [ ] Document key takeaways and trends in this README

---

## ✅ Final Note

This project is part of my Data Analytics Portfolio and showcases real-world data wrangling, documentation, and visualization skills. It highlights my ability to clean messy datasets, structure projects for clarity, and communicate findings in a professional way.

Feel free to explore the files, workflows, and screenshots, and follow my GitHub for continued updates as I complete the EDA phase.

