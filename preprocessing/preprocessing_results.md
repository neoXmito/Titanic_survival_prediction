# Preprocessing Interpretation

## Target Variable
- **Target Variable**: `Survived`

The target variable is `Survived`, which represents whether a passenger survived (`1`) or not (`0`).

## Features and Handling Missing Values

1. **Cabin**:
   - The `Cabin` feature has 687 missing values out of 891 total datapoints. Due to the significant amount of missing data, the feature was dropped, as it may not contribute sufficiently to the prediction.

2. **Age**:
   - Missing values in the `Age` feature were replaced with the mean value of the column. This method assumes that missing ages are relatively close to the average, and thus imputing with the mean can be a reasonable solution.

3. **Embarked**:
   - Missing values in the `Embarked` feature (the port where passengers boarded) were replaced with the most frequent value. This is a common strategy for categorical variables with missing values.

## Features to Drop
1. **PassengerId**:
   - The `PassengerId` feature has 891 unique values, making it difficult to encode and likely not contributing to the prediction of survival. Therefore, it was dropped from the dataset, as having too many unique values in this feature doesn't seem to impact the survival prediction.

2. **Name and Ticket**:
   - Both `Name` and `Ticket` features have too many unique values, making encoding cumbersome. Additionally, these features likely don't have predictive power for survival. Thus, both were dropped from the dataset.

## Categorical Variables Encoding

- **One-Hot Encoding** was applied to the categorical variables `Sex` and `Embarked`. This method creates binary columns for each category, allowing the model to interpret the information in a format suitable for training.

## Dataset Split

- The dataset was split into training and testing sets, with 80% of the data used for training and 20% for testing. This allows us to evaluate the model's performance on unseen data.

## Feature Scaling

- The **Age** and **Fare** features were scaled using standard scaling (mean=0, variance=1). Scaling helps to normalize the values of these continuous variables, which can improve the performance of many machine learning algorithms, especially those that rely on distance-based metrics like Logistic Regression or SVM.

