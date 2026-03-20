# 📊 Customer Churn Prediction (End-to-End Project)

## 📌 Problem Statement

Customer churn is a major challenge for telecom companies, leading to revenue loss.
The goal of this project is to identify customers who are likely to churn and enable proactive retention strategies.

---

## 🎯 Objectives

* Analyze customer behavior and churn patterns
* Build a machine learning model to predict churn
* Improve model performance based on business needs
* Provide actionable insights through visualization

---

## 🧠 Approach

### 1. Data Cleaning

* Converted TotalCharges to numeric
* Handled missing values
* Removed irrelevant columns

### 2. Exploratory Data Analysis (EDA)

* Identified key churn drivers:

  * Month-to-month contracts
  * High monthly charges
  * New customers (low tenure)
  * Electronic check users

### 3. Feature Engineering

* Used ColumnTransformer for:

  * One-hot encoding (categorical features)
  * Scaling (numerical features)

### 4. Model Building

* Built pipeline using:

  * Random Forest Classifier
* Ensured no data leakage

---

## 📈 Model Optimization

* Initial Recall (Churn): **46%**
* Final Recall (Churn): **75%** ✅

### Key Improvement:

* Applied **threshold tuning (0.5 → 0.3)**
* Focused on maximizing recall (business critical)

---

## 💡 Key Insights

* 📌 Churn is highest among **month-to-month contract users**
* 📌 **Electronic check users** show higher churn
* 📌 Customers with **low tenure** are more likely to churn
* 📌 Higher monthly charges increase churn probability

---

## 🌐 Deployment

* Built a **Streamlit web app**
* Allows real-time churn prediction

---

## 📊 Dashboard

* Created Power BI dashboard to visualize:

  * Churn by contract
  * Churn by payment method
  * Overall churn rate

---

## 💼 Business Impact

The model helps:

* Identify high-risk customers
* Enable targeted retention strategies
* Reduce revenue loss

---

## 🧑‍💻 Author

Avinash Anthony
