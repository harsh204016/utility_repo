
import streamlit as st
st.markdown("""<style>div[data-testid="stExpander"] div[role="button"] p {
    font-size: 4rem;
} </style>""",unsafe_allow_html=True)

with st.expander("How to handle missing values"):
   st.markdown("""
### Handling Missing Values: A Crucial Step in Data Wrangling

Missing values, often represented by NaN, NULL, or other placeholders, are a common challenge in data analysis. Here's a guide to effectively handle them:

**1. Identify Missing Values:**

The first step is to identify missing values in your dataset. Utilize libraries like pandas to detect and count missing entries in each column.

**2. Understand the Missing Data Pattern:**

Not all missingness is equal!  Understanding the pattern is crucial. Is the data missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR)? This classification helps determine the most appropriate handling strategy.

**3. Removal of Missing Data (Use with Caution):**

If the amount of missing data is small and randomly distributed, removing rows or columns with missing values might be an option. However, be cautious! This approach can lead to information loss.

**4. Imputation Techniques: Filling in the Blanks Strategically**

Imputation involves filling in missing values with estimated values. Here are some common techniques:

    * **Mean, Median, or Mode Imputation:** Replace missing values with the average (mean), middle value (median), or most frequent value (mode) of the respective column.
    * **Forward Fill or Backward Fill:**  In time series data, use the value from the previous (backward fill) or next (forward fill) observation to fill missing values.
    * **Interpolation:** Use linear or polynomial interpolation to estimate missing values based on surrounding data points.
    * **K-Nearest Neighbors (KNN) Imputation:** Leverage the values of nearest neighbors to impute missing values.
    * **Multivariate Imputation:** For complex datasets, use algorithms like Multiple Imputation by Chained Equations (MICE) to impute missing values considering correlations between variables.

**5. Encode Missingness as a Feature (Silence Can Be Informative)**

In some cases, the fact that data is missing can be informative itself. You can create a new binary feature indicating whether a value was missing or not.

**6. Domain Knowledge and Context: The Secret Weapon**

Consider domain knowledge and the context surrounding the missing data when choosing a handling strategy. For example, missing values in income data might have different reasons than missing values in customer surveys.

**7. Evaluate Imputation Impact: Did it Help or Hurt?**

After imputation, evaluate the impact on your data and machine learning models. Monitor performance metrics to ensure imputation doesn't introduce biases or distort results.

By following these steps, you can effectively handle missing values and ensure the quality of your data analysis.

""")


with st.expander("How does gradient boosting differ from random forests?"):
   st.markdown(""" ### Base Learners

**Random Forests:**

* Use a collection of decision trees as base learners.
* Each tree is trained independently on a random subset of data and features.
* Final prediction is made by averaging (regression) or voting (classification) individual tree predictions.

**Gradient Boosting:**

* Uses a sequence of weak learners (often decision trees).
* Each subsequent learner corrects errors made by the previous one.
* Final prediction is made by combining predictions of all weak learners.

### Training Process:

**Random Forests:**

* Trees are trained in parallel, making them suitable for parallel computing and efficient handling of large datasets.

**Gradient Boosting:**

* Trains trees sequentially, with each focusing on errors from previous ones. This makes it slower than random forests but can lead to better performance for complex data relationships.

### Handling of Errors:

**Random Forests:**

* Each tree predicts independently, with no interaction during training. This makes them less prone to overfitting and good at handling noisy data and outliers.

**Gradient Boosting:**

* Focuses on reducing errors by emphasizing poorly predicted data points. This makes it more sensitive to outliers and noise but can lead to higher accuracy with proper tuning.

### Bias-Variance Tradeoff:

**Random Forests:**

* Lower variance but higher bias. This means they may not capture complex relationships as well as gradient boosting, but are less likely to overfit.

**Gradient Boosting:**

* Lower bias but higher variance, making it more susceptible to overfitting without proper hyperparameter tuning. However, careful tuning can lead to superior performance, especially in structured data with complex patterns.

""")


with st.expander("How to handle the imbalanced data"):
   st.markdown("""### Data Augmentation

Data augmentation involves generating more examples for the ML model to train on, such as rotating images so that the dataset includes images of humans turned upside down as well as the normal upright image orientation. Without data augmentation, the model might not be able to correctly recognize images of humans who are laying sideways or doing headstands since the data is imbalanced toward humans in an upright pose.

### Oversampling

Oversampling is a technique to increase the number of data points of a minority class via synthetic generation. As an example, SMOTE (synthetic minority oversampling technique) uses the feature vectors of the minority classes to generate synthetic data points that are located between real data points and their k-nearest neighbors. This could synthetically increase the size of the minority class(es) and improve the performance of the ML model trained on a dataset with oversampling treatment.

### Undersampling

Undersampling does the opposite: it reduces examples from the majority class to balance the number of data points of the majority class and minority class(es). Oversampling is generally preferred in practice since undersampling may cause useful data to be discarded, which is exacerbated when the dataset is already small.

### Ensemble Methods

Ensemble methods can also be used to increase model performance when dealing with an imbalanced dataset. Each model in the ensemble can be trained on a different subset of the data and can help learn the nuances of each class better.

""")

with st.expander("Explain boosting and bagging and what they can help with."):
   st.markdown("""### Bagging
Bagging trains multiple models on different subsets of the training data and combines their predictions to make a final prediction.
### Boosting
Boosting trains a series of models where each model tries to correct the mistakes made by the previous model. The final prediction is made by all the models. Ensemble techniques can help with a variety of issues encountered during ML training. For example, they can help with imbalanced data and reduce overfitting.


""")
   

with st.expander("What is diff btw L1 and L2 regularization?"):
   st.markdown("""L1 regularization, also known as lasso regularization,is a type of regularization that shrinks model parameters toward zero. L2 regularization (also known as ridge regularization) adds a penalty term to the objective function that is proportional to the square of the coefficients of the model. This penalty term shrinks the coefficients toward zero, but unlike L1 (lasso) regularization, it does not make any of the coefficients exactly equal to zero.

L2 regularization can help reduce overfitting and improve the stability of the model by keeping coefficients from becoming too large. Both L1 and L2 regularization are commonly used to prevent overfitting and improve the generalization of ML models.
 """)