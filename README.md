🛡️ **Phishing Domain Detection using Machine Learning**

Phishing websites are a major cybersecurity threat that attempt to mimic legitimate websites to steal sensitive user data such as usernames, passwords, and credit card details. This project uses various machine learning algorithms to classify URLs as either **phishing** or **legitimate**.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 **Table of Contents**

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Approach](#approach)
- [Results](#results)
- [Future Work](#future-work)
- [Author](#author)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

🔍 **Overview**

This machine learning project aims to detect phishing domains by analyzing various features extracted from URLs. The goal is to assist users and security systems in identifying malicious websites before they can cause harm.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

❗ **Problem Statement**

Phishing attacks exploit human error and design similarities to trick users into sharing sensitive information. Detecting such domains automatically can prevent large-scale breaches and enhance trust in online systems.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

🧰 **Tech Stack**

- **Language**: Python
- **Libraries**: pandas, numpy, matplotlib, seaborn, sklearn
- **Environment**: Jupyter Notebook / Google Colab
- **Models**: Random Forest, Logistic Regression, Decision Tree, KNN, SVM

--------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 **Dataset**

- **Dataset Name:** PHISHING_DOMAIN_DETECTION.csv
- **Rows:** 19,432
- **Features:** 86 (mostly numeric)
- **Target:** `status` — whether the domain is `phishing` or `legitimate`

  The dataset includes features extracted from URLs, such as:
  - url_length
  - total_of?
  - total_of_www
  - ratio_digits_url
  - phish_hints
  - nb_hyperlinks
  - domain_in_title
  - domain_age
  - google_index
  - page_rank
 
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  ⚙️ **Approach**
  
  1. **Data Cleaning and Preprocessing**
  2. **Exploratory Data Analysis (EDA)**
  3. **Feature Engineering**
  4. **Model Training**
     - Compared several classifiers (Random Forest, KNN, etc.)
  5. **Evaluation using Accuracy, Precision, Recall, and F1 Score**
  6. **Model Comparison**
 
--------------------------------------------------------------------------------------------------------------------------------------------------------------

  📊 **Results**

  - **Best Model**: Random Forest
  - **Accuracy**: 98.69%
  - **Precision/Recall:** 98.44%/98.99%
  - Confusion Matrix, ROC Curve, and AUC were also analyzed.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

  🛠 **Future Work**
  - Use deep learning models like LSTM on URL text
  - Real-time detection with a deployed web app
  - Add more features like WHOIS data and blacklists
  - Extend to multilingual phishing sites

--------------------------------------------------------------------------------------------------------------------------------------------------------------

  👤 **Author**
  
  Ishita Ganatra<br>
  CSE (AI & ML) Student<br>
  🔗 [Linkedin](https://www.linkedin.com/in/ishita-ganatra-06763930b) | [GitHub](https://github.com/ML-Experiments-Lab)
