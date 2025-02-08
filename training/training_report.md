# Model Training Report

## Overview
In this experiment, we trained and evaluated 10 different machine learning models for binary classification on our preprocessed dataset. The goal was to identify the best-performing model based on accuracy.

## Models Trained
We trained the following models:

- **Logistic Regression** (`LogisticRegression()`)
- **Decision Tree** (`DecisionTreeClassifier()`)
- **Random Forest** (`RandomForestClassifier()`)
- **Support Vector Machine (SVM)** (`SVC()`)
- **K-Nearest Neighbors (KNN)** (`KNeighborsClassifier()`)
- **Naive Bayes** (`GaussianNB()`)
- **LightGBM** (`lgb.LGBMClassifier()`)
- **XGBoost** (`xgb.XGBClassifier()`)
- **AdaBoost** (`AdaBoostClassifier()`)
- **Neural Network** (`MLPClassifier()`)

## Best Model
After evaluating all models, the **best-performing model** was **LightGBM**, achieving an **accuracy of 82%**.

## Next Steps
To further improve accuracy, we can explore:
- Hyperparameter tuning for all models
- Feature engineering to enhance predictive power
- Collecting more data or handling imbalanced classes

This report summarizes the training process and results. The saved LightGBM model can be used for predictions on new data.

