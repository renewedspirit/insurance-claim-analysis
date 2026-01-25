# ![Health Insurance icon](https://www.freeiconspng.com/uploads/health-insurance-plan-icon-24.png)

# Insurance Claim Analysis

This repository contains all the project files for the Capstone Project in Code Institute's, Data Analytics with AI bootcamp.

## Table of Contents

1. [Project Overview & Goal](#1-project-overview--goal)
2. [Tools & Technologies](#2-tools--technologies)
3. [Target Audience](#3-target-audience)
4. [Expected Deliverables](#4-expected-deliverables)
5. [Data Transformation Summary](#5-data-transformation-summary)
6. [How to Run the Project Locally](#6-how-to-run-the-project-locally)
7. [Challenges](#7-challenges)
8. [Next Steps](#8-next-steps)
9. [Credits & Acknowledgements](#8-credits-acknowledgements)
<br>
 
## 1. Project Overview & Goal

### Dataset & Source
* This synthethic dataset was sourced from Kaggle under [*Insurance Claim Analysis: Demographic and Health*](https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health)The dataset contants 1340 records and 11 attributes.

* The dataset contains information on patient id, age, gender, BMI (Body Mass Index), blood pressure levels, diabetic status, number of children, smoking status, region and insurance claim amount.

### Business Requirements
* Although this dataset is synthetic it does contain insightful information, by looking deep into patients who receive insurance claims and what impact their demographic patterns has on the amount of insurance they claim. By analysing these factors such as age, gender and smoking status we can gain a greater understanding of who is most likely to receive a high insurance claim. This could potentially provide valuable insight which could be used to inform any decision making when taking on potential new customers. Also, any insights yielded could also help public and private medical institutions and physicians. As they would have more information about which type of patients are more vulnerable to high insurance claims and therefore help them support their patients in finding alternative ways to lower their claims.

#### Key Research Questions
The goal for this  project is was explored using the following research questions. 3 questions were asked forming the basis of each hypothesis. 

1. **Do people who smoke claim more in health insurance?**
    
    Hypothesis: People who smoke are more likely to have a higher insurance claim compared with non-smokers.
   
2. **Do patients with chronic diseases increase their insurance claims?**

    Hypothesis: Patients with a high BMI number together with a chronic disease increase their chances of a higher insurance claim.

3. **Does gender have an impact on insurance claims?**

    Hypothesis: Gender does not have an impact on a patient's insurance claim.


<br>

## 2. Tools & Technologies

- **Trello**
- **Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly** 
- **Jupyter Notebook** 
- **GitHub (Version Control)**
- **Power BI (dashboard)** 

<br>

## 3. Target Audience 

The dashboard and interactive tool are intended for:

**1. Health insurance companies onboarding new customers -** Decision makers can now have access to Those looking for travel suggestions based on a budget, continent, climate, or travel style.

**2. Public and private healthcare facilities identifying vulnerable patients -** Phycisions can now have insight into patients who are more likely to make an insurance claim. This insight can be used to help identify patients with or on the verge of having a chronic disease. Providing them with tools and guidance to help eliminate or at least lower their demographic numbers which would then reduce their insurance claim.

<br>

## 4. Expected Deliverables

Our final outputs for the project  will be:

- Clean, structured dataset ready for analysis

- Power BI dashboard with interactive visuals

- Project documentation (e.g. README, Project Proposal etc)

- Final presentation summarising findings, insights, and recommendations

<br>

## 5. Data Transformation Summary

| Original Column / Feature                                                                                               | Transformation Applied                                                                                           | New Column(s) Created                                                       | Purpose / Notes                                                          |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `index`                                                                                                                    | Dropped                                                                                                          | —                                                                           | Not useful for analysis; patient id replaces it.                      |
| ``                                                                                                      | Parsed JSON-like string → extracted monthly averages → calculated annual mean → dropped after feature extraction | ``                                                           | Simplifies climate data into one metric for analysis.                    |
| ``                                                                                                       | Converted from string list into Python list using `ast.literal_eval`→ Split into multiple binary indicator → Dropped after creating columns                                                                     | `is_short_trip`, `is_one_week`, `is_long_trip`, `is_weekend`, `is_day_trip` | Enables filtering, grouping, and correlation analysis.                   |
| `budget_level`                                                                                                          | Encoded categories into numbers (e.g., Budget=1, Mid-range=2, Luxury=3)                                          | —                                                                           | Makes the column usable for numerical analysis.                          |
| Ratings Columns (`culture`, `adventure`, `nature`, `beaches`, `nightlife`, `cuisine`, `wellness`, `urban`, `seclusion`) | Combined using mean                                                                                              | `city_rating`                                                               | Creates overall score; representing appeal.                 |
|`short_description`                                                                                                     | Kept for dashboard dataset, then deleted for analysis                                                                                    | —                                                                           | Needed for Streamlit recommendations.                                    |
| `latitude`, `longitude`                                                                                                 | Kept unchanged for dashboard dataset, then deleted for analysis                                                                                                   | —                                                                           | Used for mapping visualisations (even if not used in notebook analysis). |

<br>

## 6. How to Run the Project Locally

### Clone the Repository

```bash
git clone [https://github.com/renewedspirit/insurance-claim-analysis]

cd insurance-claim-analysis
```

### Install Dependencies

You will need a ```requirements.txt``` file listing pandas, numpy, streamlit, etc.
Open your terminal or a Jupyter cell and run:

```bash
pip install -r requirements.txt
```

### Run the Notebook

Open `spf_analysis.ipynb` and run all cells sequentially. The notebook will automatically download the data, run the ETL pipeline, and generate all seaborn/matplotlib visualizations.

<br>

## 7. Challenges

#### Briefly describe how you have used AI to build your project. *
* Focus on your interactions with how you used AI to return the results you needed.
#### Briefly describe the challenges you faced when using AI to build your project.*
#### Briefly describe how AI benefited you and your project.*
#### Explain the ethical considerations taken into account when building your project.


 
<br>

## 8. Next Steps

### Things I would do to further the analysis

<br>

## 9. Credits & Acknowledgements

#### During this project the following were used to help with coding and github requirements:

- Learning material on the Code Institute LMS portal
- Masterclass video recordings from Data Analytics with AI Bootcamp course through Code Institute.
- Code Institute Hackathon Project (Worldwide Travel Analysis) [https://github.com/renewedspirit/Worldwide_Travel_Analysis.git].
- Original author of the dataset - [*Sumit Kumar Shukla*](https://data.world/sumitrock/insurance).
- ChatGPT for debugging and for helping with blocks of Machine Learning code as I am still learning.

#### Acknowledgements

- Thanks to my husband's with taking on more house work while I worked late into the night and my son for the late pick ups from school. 
- Grateful to my cohort, those who encouraged me to keep going when I was feeling very overwhelmed.
- Guidance from leaders of Code Institute. Supporting me as I navigated the project alongside managing my ongoing illness developed during my time on this course and while I was completing this project.


numpy==1.26.1
pandas==2.1.1
matplotlib==3.8.0
seaborn==0.13.2
ydata-profiling==4.12.0 # can be removed from requirements before deployment
plotly==5.17.0
ppscore==1.1.0 # can be removed from requirements before deployment
streamlit==1.40.2
feature-engine==1.6.1
imbalanced-learn==0.11.0
scikit-learn==1.3.1
xgboost==1.7.6
yellowbrick==1.5 # can be removed from requirements before deployment
Pillow==10.0.1 # can be removed from requirements before deployment