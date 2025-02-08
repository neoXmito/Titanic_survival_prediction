---

# **Titanic Survival Prediction 🚢💡**

## **Project Overview**
This project predicts whether a passenger survived the **Titanic disaster** using **machine learning**. The dataset was preprocessed, analyzed, and used to train multiple models. The best-performing model, **LightGBM**, was deployed as a **Streamlit web application**.

---

## **1️⃣ Exploratory Data Analysis (EDA) - Interpretation of Results**  

### **Key Findings**  

#### 🛠 **Missing Data**  
- **177 passengers** had missing **Age** values.  
- **687 passengers** had missing **Cabin** details.  

#### 👥 **Demographics & Passenger Characteristics**  
- Most passengers were between **15-45 years old**.  
- **Males (65%)** outnumbered females.  
- Most passengers traveled with **1 or no siblings/spouses**.  

#### ⚰️ **Survival Analysis**  
- **Only 38% of passengers survived**.  
- **3rd-class passengers were the majority**, but they had lower survival rates.  
- **1st-class passengers had the highest survival rate (~40%)**.  
- **Women had a significantly higher survival rate (68%)**.  

#### 📊 **Correlation Analysis**  
- **Passenger class strongly influenced survival** (higher-class passengers had a better chance).  
- **Women had a higher probability of survival than men**.  

---

## **2️⃣ Preprocessing Pipeline**  

### **Target Variable** 🎯  
- **`Survived`** (1 = Survived, 0 = Did Not Survive)  

### **Handling Missing Values**  
- **`Cabin`** → **Dropped** due to excessive missing data.  
- **`Age`** → **Imputed with the mean**.  
- **`Embarked`** → **Imputed with the most frequent value**.  

### **Dropped Features**  
- **`PassengerId`** (Unique identifier, not predictive).  
- **`Name` and `Ticket`** (High cardinality, not useful for prediction).  

### **Feature Encoding**  
- **One-Hot Encoding** applied to **`Sex`** and **`Embarked`**.  

### **Feature Scaling**  
- **Standard Scaling** applied to **`Age`** and **`Fare`** (mean=0, variance=1).  

---

## **3️⃣ Model Training Report**  

### **Models Trained**  
We experimented with **10 models**:  
✅ **Logistic Regression**  
✅ **Decision Tree**  
✅ **Random Forest**  
✅ **Support Vector Machine (SVM)**  
✅ **K-Nearest Neighbors (KNN)**  
✅ **Naive Bayes**  
✅ **LightGBM**  
✅ **XGBoost**  
✅ **AdaBoost**  
✅ **Neural Network (MLPClassifier)**  

### **🏆 Best Model**  
- **LightGBM (Accuracy: 82%)**  

### **Next Steps**  
- Hyperparameter tuning  
- Feature engineering  
- Handling imbalanced classes  

---

## **4️⃣ Deployment on Streamlit 🚀**  

### **📌 How to Run the App Locally**
#### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **2️⃣ Run the Streamlit App**
```bash
streamlit run streamlit/streamlit_app.py
```

#### **3️⃣ Access the App**
After running the command, open your browser and go to:
```
http://localhost:8501/
```

### **📌 App Features**
- Users can input **passenger details**.
- The model predicts **whether the passenger would survive**.
- **User-friendly interface** built with **Streamlit**.

### **📌 Live Demo**
- 🚀 **[Titanic Survival Prediction App (Streamlit)](https://your-streamlit-app-url.com)**  

---

## **5️⃣ Folder Structure**  

```
📂 Titanic_survival_prediction
│── 📂 competition             # Kaggle competition
│── 📂 dataset               # Raw and processed datasets  
│── 📂 EDA          #  notebook for EDA  
│── 📂 preprocessing       # Encoders, scalers, and imputers  
│── 📂 streamlit           # Streamlit app files  
│── 📂 training            # Saved machine learning models  
│── README.md              # Project documentation  
│── requirements.txt       # Required dependencies  
```

---

## **6️⃣ Requirements & Technologies Used**  

### **📦 Libraries**  
- `pandas`, `numpy` (Data processing)  
- `scikit-learn` (Machine learning)  
- `lightgbm` (Best-performing model)  
- `streamlit` (Web app)  
- `joblib` (Model saving/loading)  

### **🛠 Tools**  
- **Python**  
- **Jupyter Notebook**  
- **Streamlit**  
- **Scikit-learn**  

---

## **7️⃣ Acknowledgments**  
- **Kaggle Titanic Dataset** 🏆  
- **Scikit-learn & LightGBM Developers**  
- **Streamlit for easy deployment**  

---

This **Titanic Survival Prediction** project is a great example of **end-to-end machine learning**, covering **EDA, preprocessing, model training, and deployment**.  

💡 **Feel free to contribute or enhance the model!**  

🚀 **Happy Coding!** 🏆