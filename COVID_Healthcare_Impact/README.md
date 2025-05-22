# 🦠 COVID-19 Healthcare Impact in New Jersey  
**Phase 1: Data Cleaning & Preparation Completed**

Hi! I’m Margaret Johnson. This project is part of my Data Analytics portfolio and focuses on exploring how COVID-19 impacted counties in New Jersey — especially when viewed through the lens of median household income. 

I’ve completed Phase 1: cleaning and organizing three public datasets. Next, I’ll begin analyzing trends, generating visual insights, and answering the project’s guiding question.

---

## 📚 Table of Contents

- [🎯 Project Objective](#-project-objective)
- [❓ Guiding Research Question](#-guiding-research-question)
- [✅ Current Progress: Phase 1 Completed](#-current-progress-phase-1-completed)
- [📊 Datasets Used](#-datasets-used)
- [🧰 Tools Used](#-tools-used)
- [📂 Project Folder Overview](#-project-folder-overview)
- [🖼️ Screenshot Previews (Phase 1)](#️-screenshot-previews-phase-1)
- [💡 What I Learned](#-what-i-learned)
- [🧭 What’s Coming in Phase 2](#-whats-coming-in-phase-2)
- [🙋🏽‍♀️ About Me](#-about-me)

---

## 🎯 Project Objective

To investigate whether New Jersey counties with lower median household income experienced higher COVID-19 death rates and outbreak severity compared to higher-income counties.

---

## ❓ Guiding Research Question

> **Is there a relationship between median income and COVID-19 death rates across counties in NJ?**

This project is built to reflect real-world challenges in public health analytics — including messy data, merging multiple datasets, and preparing for future correlation analysis.

---

## ✅ Current Progress: Phase 1 Completed

I’ve completed the data preparation and workflow documentation using KNIME, Excel, and GitHub.  
Here's what’s been done so far:

| Task | Status |
|------|--------|
| ✅ Collected 3 public datasets (Deaths, Income, LTC Outbreaks) | [Raw Datasets](./Raw_Datasets) |
| ✅ Cleaned datasets using KNIME workflows | [KNIME Workflow Files](./KNIME_Workflow) |
| ✅ Exported cleaned files | [Final Cleaned Datasets](./Final_Exports) |
| ✅ Documented every step with screenshots | [Visual Workflow Screenshots](./Screenshots) |
| 🔜 Merging datasets for analysis | In Progress |
| 🔜 Creating visualizations and reports | Coming Soon |

---

## 📊 Datasets Used

| Dataset Name | Description | Source Link | Status |
|--------------|-------------|-------------|--------|
| US COVID Deaths by County | Sourced from CDC. Filtered to NJ and cleaned. | [View Dataset](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-County-and-Ra/k8wy-p9cg) | ✅ Cleaned |
| NJ Median Household Income | County-level income data from Census.gov | [View Dataset](https://data.census.gov/table?q=median+household+income+new+jersey+counties) | ✅ Cleaned |
| NJ Long-Term Care Facility Outbreaks | NJDOH dashboard with LTC COVID-19 data | [View Dataset](https://www.nj.gov/health/covid-19/information/data-and-dashboards/) | ✅ Cleaned |


---

## 🧰 Tools Used

- 🧩 **KNIME Analytics Platform** – Data cleaning workflows
- 📊 **Microsoft Excel** – Initial formatting and calculations
- 💻 **GitHub** – Project sharing, documentation, version control
- 📝 **Markdown** – Clear, organized README documentation

---

## 📂 Project Folder Overview

📁 COVID_Healthcare_Impact/
├── Raw_Datasets/ → Original unedited data files
├── KNIME_Workflow/ → Reproducible cleaning workflows (.knwf)
├── Final_Exports/ → Fully cleaned, analysis-ready CSVs
├── Screenshots/ → Visual documentation of cleaning process
└── README.md → This project description file

---

## 🖼️ Screenshot Previews (Phase 1)

Here’s a quick look at what I did in each dataset:

### 📁 Dataset 1 – NJ Long-Term Care Outbreaks

- Raw import and structure preview  
  ![](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/01_Import_LTC_Data_CSV_Reader.png)

- Cleaned and filtered LTC records  
  ![](./Screenshots/Dataset_1-NJ%20Long-Term%20Care%20Facility%20Outbreaks/11_Final_LTC_Cleaned_Table.png)

---

### 📁 Dataset 2 – NJ Median Household Income

- Income data loaded and cleaned  
  ![](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/03_Rename_Columns_Income.png)

- Final clean CSV exported  
  ![](./Screenshots/Dataset_2-NJ%20Median%20Household%20Income/06_Save_Cleaned_Income_CSV.png)

---

### 📁 Dataset 3 – COVID Deaths by County

- Filtered New Jersey-only counties  
  ![](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/02_Filter_New_Jersey_Rows.png)

- Cleaned and saved final dataset  
  ![](./Screenshots/Dataset_3-US%20COVID%20Deaths%20by%20County%20(NJ%20Only)/06_Save_Cleaned_US_Deaths_CSV.png)

---

## 💡 What I Learned

- How to manage multi-source public datasets with inconsistent structures
- How to use KNIME to automate cleanup, filtering, and formatting
- How to version and structure a GitHub project to reflect professionalism
- The importance of documenting every step for transparency and clarity

---

## 🧭 What’s Coming in Phase 2

- Merge final datasets into one unified table
- Calculate death rates per county and income brackets
- Explore trends using charts (scatter plots, bar graphs, correlation heatmaps)
- Share conclusions in a final summary and add visuals to GitHub

---

## 🙋🏽‍♀️ About Me

I’m **Margaret Johnson**, an aspiring Data Analyst pivoting from business operations to tech. I’m passionate about real-world problem-solving, especially in public health and community impact spaces. I'm actively building my portfolio with projects that demonstrate both technical skills and meaningful questions.

📬 Connect with me:  
🌐 [GitHub Portfolio](https://github.com/Margaret-Johnson-ai)  
🎓 Certifications: Google Data Analytics • Google IT Support • DataCamp SQL • AWS in progress

---

> *“Data should tell a story—and I’m learning how to find and share it.”*
