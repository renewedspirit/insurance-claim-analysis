# ![Health Insurance icon](https://www.freeiconspng.com/uploads/health-insurance-plan-icon-24.png)

# Insurance Claim Analysis

This repository contains all the project files for the Capstone Project in Code Institute's, Data Analytics with AI bootcamp.

## Table of Contents

1. [Project Overview & Goal](#1-project-overview--goal)
2. [Tools & Technologies](#2-tools--technologies)
3. [Target Audience](#3-target-audience)
4. [Expected Deliverables](#4-expected-deliverables)
5. [Data Transformation Summary](#5-data-transformation-summary)
6. [Key Findings and Insights](#6-key-findings-and-insights)
7. [How to Run the Project Locally](#7-how-to-run-the-project-locally)
8. [Challenges](#8-challenges)
9. [Next Steps](#9-next-steps)
10. [Data Ethics](#10-data-ethics)
11. [Credits & Acknowledgements](#10-credits-acknowledgements)
<br>
 
## 1. Project Overview & Goal

### Dataset & Source
* This synthethic dataset was sourced from Kaggle under [*Insurance Claim Analysis: Demographic and Health*](https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health). The dataset contants 1340 records and 11 attributes.

* The features of this dataset are information on patient id, age, gender, BMI (Body Mass Index), blood pressure levels, diabetic status, number of children, smoking status, region and insurance claim amount.

* Since the dataset is synthethic this could cause some limitation on the results.

### Business Requirements
* Although this dataset is synthetic it does contain insightful data. By analysing factors such as age, gender and smoking status we can gain a greater understanding of who is most likely to have high insurance claims. This could potentially provide valuable insight which could be used to inform any decision making when taking on potential new customers. Also, any insights yielded could also help public and private medical institutions and physicians. As they would have more information about which type of patients are more vulnerable to high insurance claims and therefore help support their patients in finding alternative ways to lower their claims.

#### Key Research Questions
* The goal for this project is to understand the impact of a patients demographic patterns with their level of isurance claims. 
* Research questions were explored, which then became the basis of the 3 hypotheses created below: 

1. **Do people who smoke claim more in health insurance?**
    
    Hypothesis: People who smoke are more likely to have a higher insurance claim compared with non-smokers.
   
2. **Do patients with chronic diseases increase their insurance claims?**

    Hypothesis: Patients with a high BMI number together with a chronic disease increase their chances of a higher insurance claim.

3. **Does gender have an impact on insurance claims?**

    Hypothesis: Gender does not have an impact on a patient's insurance claim.


<br>

## 2. Tools & Technologies

- **Trello**
- **Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-Learn** 
- **Jupyter Notebook** 
- **GitHub (Version Control)**
- **Streamlit (dashboard app)** 

<br>

## 3. Target Audience 

The dashboard app and interactive tool are intended for:

**1. Health insurance companies onboarding new customers -** Insurance providers can use this dashboard to:
- Identify key factors associated with higher insurance claims for example smoking, BMI, chronic diseases
- Support risk assessment during customer onboarding
- Improve pricing strategies and preventative care recommendations

**2. Public and private healthcare facilities identifying vulnerable patients -** Healthcare providers can use insights from this analysis to:
- Identify patient groups associated with higher healthcare costs
- Detect compounding risk factors such as high BMI combined with chronic disease
- Support early intervention and preventative healthcare planning

By highlighting patterns in insurance claims, this dashboard helps healthcare organisations better understand patient vulnerability and allocate resources more effectively.

<br>

## 4. Expected Deliverables

The final outputs for the project are to include:

- Clean, structured dataset ready for analysis

- Interactive Streamlit dashboard with data visuals and a machine learning component

- Project planning files and README documentation to include summary of findings, insights and conclusions


<br>

## 5. Data Transformation Summary

Before analysis and modelling, the dataset was cleaned and prepared by:
- Handling missing values in key variables
- Creating derived features such as BMI categories
- Encoding categorical variables into binary format for machine learning
- Ensuring all numerical features were suitable for analysis and modelling


<br>


## 6. Key Findings and Insights

This project explored factors influencing healthcare insurance claim amounts using exploratory data analysis, visualisation, and a simple machine learning model.

### Key Findings

- **Hypothesis 1 - Smoking status** was strongly associated with higher insurance claims. Smokers showed both higher median claim amounts and greater variability compared to non-smokers.
- **Hypothesis 2 - High BMI combined with diabetes** resulted in particularly higher average insurance claims. This suggests that there is a potential heightening effect of multiple health risk factors and high insurance claims.
- **Hypothesis 3 - Gender** this showed minimal impact on insurance claim amounts, indicating that claim differences are probably driven more by health-related factors than gender alone.

### Machine Learning Summary

A linear regression model was trained to predict insurance claim amounts using demographic and health-related features.

- The model achieved an **R² score of 0.723**, this indicates that approximately 72% of the variation in claim amounts is explained by the selected features.
- The model produced an **RMSE of £6,319**, meaning predictions are, on average, within this range of the actual claim values.

In summary these results show that the model provides a strong baseline for insurance companies and health care providers an understanding of cost drivers in healthcare insurance claims.

<br>

## 7. Deployment

### How to Run the Project Locally

#### Clone the Repository

```bash
git clone [https://github.com/renewedspirit/insurance-claim-analysis]

cd insurance-claim-analysis
```

#### Install Dependencies

You will need a ```requirements.txt``` file listing pandas, numpy, streamlit, etc.
Open your terminal or a Jupyter cell and run:

```bash
pip install -r requirements.txt
```

#### Run the Streamlit app

```bash
streamlit run app.py
```

#### Run the Notebook

Open both `insurance-claim.ipynb` and `insurance-claim-ml.ipynb` respectively and run all cells sequentially. The notebooks will automatically download the data, run the ETL pipeline, and generate all seaborn/matplotlib visualizations.

### How to Deploy Streamlit App 

This application is deployed publicly using **Streamlit Community Cloud**.

The deployment process is as follows:

1. The project code is hosted in a public GitHub repository.
2. A `requirements.txt` file is included in the repository to specify all Python dependencies required to run the app.
3. Streamlit Community Cloud automatically installs these dependencies in a clean cloud environment.
4. The application is launched using the main entry file `app.py`, with additional pages loaded from the `pages/` directory.

The app is available at:
**https://insurance-claim-analysis-9cxpmku536gnwmw2mksadc.streamlit.app/ml_predictor**

Doing the above helps to make sure that the app can be used publicly, easily accessible, and therefore not reliant on a local Python environment.

<br>

## 8. Challenges

* I had some problems with Python package versions not being compatible with my virtual enivronment. It meant that I needed to unistall my python 3.13 and install 3.12.10. This allowed me to install the libraries I would need to write and run my code. 
* I also had issues with the requirement list when deploying my Streamlit app. I had to remove most of what I had for Streamlit to deploy my app.
* Due to being diagnosed with a condition which affects my brain during the course I struggled to retain information. So I used ChatGPT and Youtube to help me understand Machine Learning. I now feel confident in my understanding and am looking forward to enhancing my project.

<br>

## 9. Next Steps

### Things I would do to further the analysis

* I would like to look at more complex machine learning models like Random Forest to maybe improve on the prediction accuracy
* Incorporating additional health and lifestyle variables like whether having children has an impact on high insurance claims.
* With more time  I would like to enhance the Streamlit dashboard by adding more colour and/or images. Also make it more interactive

<br>

## 10. Data Ethics

* The dataset used for this project is available to the public.
* As the data is synthetic it did not contain personal information.

<br>

## 11. Credits & Acknowledgements

#### During this project I credit in helping me with coding and github requirements:

- Learning material on the Code Institute LMS portal
- Masterclass video recordings from Data Analytics with AI Bootcamp course through Code Institute.
- Code Institute Hackathon Project (Worldwide Travel Analysis) [https://github.com/renewedspirit/Worldwide_Travel_Analysis.git].
- Original author of the dataset - [*Sumit Kumar Shukla*](https://data.world/sumitrock/insurance).
- ChatGPT was used for debugging errors.
- ChatGPT was used to create Machine Learning code and the entire Streamlit app code as I am still learning.
- Youtube - For breaking down into simple terms what is Machine Learning and how it is used  (Cat and Dog example)
- Code Institute specific Capstone support documents which helped me with my project planning

#### Acknowledgements

- I am thankful to my husband son for bearing with me as I worked all hours of the day and night.
- I am thankful for the prayers and support I received from my church, family and friends which helped me to keep going.
- Grateful to my cohort, those who encouraged me to keep going when I was feeling very overwhelmed.
- Guidance from leaders (Paul, John and Emma) of Code Institute. Supporting me as I navigated the project alongside managing my ongoing illness developed during my time on this course and while I was completing this project.

