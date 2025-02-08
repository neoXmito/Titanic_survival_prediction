import streamlit as st
import pandas as pd
import joblib 
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# Load the trained LightGBM model
model_path = 'training/best_lgb_model.pkl'  # Update path if needed
model = joblib.load(model_path)

# Load the scaler , encoder and imputers
scaler_path = 'preprocessing/joblib/standard_scaler.pkl'
scaler = joblib.load(scaler_path)

encoder_path = 'preprocessing/joblib/onehot_encoder.pkl'
encoder = joblib.load(encoder_path)

imputer_path_age = 'preprocessing/joblib/mean_imputer_age.pkl'
imputer_age = joblib.load(imputer_path_age)

imputer_path_embarked = 'preprocessing/joblib/most_frequent_imputer_embarked.pkl'
imputer_embarked = joblib.load(imputer_path_embarked)

# Streamlit UI
st.title("🚢 Titanic Survival Prediction")
st.write("This is a simple web app to predict the survival of Titanic passengers.")
st.write("Please fill in the following fields and click the button below to get the prediction.")

# User inputs
PassengerId = st.text_input("Passenger ID")
Pclass = st.selectbox("Passenger Class", [1, 2, 3])
Name = st.text_input("Name")
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.number_input("Age", min_value=0, max_value=150, step=1)
SibSp = st.number_input("Number of Siblings/Spouses Aboard", min_value=0, max_value=20, step=1)
Parch = st.number_input("Number of Parents/Children Aboard", min_value=0, max_value=20, step=1)
Ticket = st.text_input("Ticket Number")
Fare = st.number_input("Fare", min_value=0.0, step=0.1)
Cabin = st.text_input("Cabin Details")
Embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Button to make prediction
if st.button("Predict Survival"):
    # Preprocess the input
    data = pd.DataFrame({
        'Pclass': [Pclass],'Sex': [Sex], 'Age': [Age], 'SibSp': [SibSp], 'Parch': [Parch],'Fare': [Fare], 'Embarked': [Embarked] })
    

    print("Columns in Data Before Imputation:", data.columns)
    print("Columns Expected by Imputer:", imputer_age.feature_names_in_)

    # Handle missing values
 

    # Encode categorical variables
    categorical_features = ['Sex', 'Embarked']
    data_encoded = encoder.transform(data)

    # Get feature names after encoding
    encoded_columns =encoder.transformers_[0][1].get_feature_names_out(categorical_features)
    all_features = list(encoded_columns) + list(data.columns.drop(categorical_features))
    data_encoded = pd.DataFrame(data_encoded, columns=all_features)

    # Scale the features
    features_to_scale = ['Age', 'Fare']
    data_encoded[features_to_scale] = scaler.transform(data_encoded[features_to_scale])
    st.write(data_encoded)

    # Make prediction
    prediction = model.predict(data_encoded)[0]

    # Display result
    st.write("### Prediction Result:")
    if prediction == 1:
        st.success("🎉 The passenger **survived**!")
    else:
        st.error("💀 The passenger **did not survive**.")

    # Display prediction probability
    st.write("### Prediction Probability:")
    proba = model.predict_proba(data_encoded)[0]
    st.write(f"Survival Probability: {proba[1]:.2f}")
    st.write(f"Death Probability: {proba[0]:.2f}")
