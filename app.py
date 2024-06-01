import streamlit as st

tab1, tab2, tab3 = st.tabs(['Statistics','Linux','Misc'])

with tab2:

    with st.expander("basic linux commands"):
        st.markdown("- check top 10 process running with memory%: **ps aux --sort=-%mem | head**")
        st.markdown("- kill any process with pid: **kill pid**")
        st.markdown("- check total , used , free, shared memory : **free -h**")

with tab1:
    st.header("stats concepts")

    with st.expander("P-value"):
        st.markdown("""
                    When we do an experiment or study, we often want to know if our results are meaningful or if they happened by chance. The p-value helps us figure this out.

First, we make a hypothesis, called the **null hypothesis**." This usually says that there is no effect or no difference. For example, "This new drug has no effect on patients."

Then, we collect data and do some calculations. The p-value tells us the probability of getting results as extreme as ours, assuming the null hypothesis is true.

- A low p-value **(typically less than 0.05)** means our results are unlikely to have happened by chance.**We might reject the null hypothesis and say our results are significant.(LR)**
- A **high** p-value means our results are more likely to have happened by chance. **We do not reject the null hypothesis**.
                    
**Example:** With a p-value of 0.02, which is less than 0.05, you would reject the null hypothesis and conclude that the new teaching method likely improves test scores.
                    With a p-value of 0.02, which is less than 0.05, you would reject the null hypothesis and conclude that the new teaching method likely improves test scores.

## Where we can use p-value in Machine Learning?
- ## Feature selection 
    When you have many features (variables), you can use p-values to determine which ones are statistically significant and should be included in the model.
                    
    **Example:** Let's say you are building a linear regression model to predict house prices based on features like size, number of bedrooms, and location. 
            After fitting the model, you get the following p-values for the coefficients:

Size: p-value = 0.01
Number of Bedrooms: p-value = 0.20
Location: p-value = 0.03        

                    Size (p-value = 0.01):

This p-value is less than 0.05, which indicates that the feature "Size" is statistically significant. Therefore, we should include "Size" in the model.

                    Number of Bedrooms (p-value = 0.20):

This p-value is greater than 0.05, indicating that the feature "Number of Bedrooms" is not statistically significant. We might consider excluding this feature from the model, as it may not contribute much to predicting house prices.

                    Location (p-value = 0.03):

This p-value is also less than 0.05, suggesting that the feature "Location" is statistically significant. Thus, we should include "Location" in the model.                                
                    
- ## Model Evaluation
When evaluating model performance, especially with hypothesis testing, p-values can indicate if the model's predictions are significantly better than random chance.
For example, in classification problems, you might use p-values in a chi-square test to determine if the observed frequencies of predicted classes significantly differ from expected frequencies.
- ## Hypothesis Testing
In machine learning experiments, p-values can help you compare models or algorithms.
For instance, if you are comparing the performance of two different algorithms, you might perform a statistical test to determine if the difference in their performance metrics (like accuracy) is significant. A p-value less than 0.05 would suggest a significant difference.
                    """)

    with st.expander("Normal Distribution"):
        st.markdown("""
The normal distribution is a fundamental concept in statistics and is often referred to as a bell curve because of its shape. 

## Characteristics of a Normal Distribution
- **Symmetrical Shape**: The normal distribution is perfectly symmetrical around its mean (average). This means the left and right sides of the curve are mirror images of each other.
- **Mean, Median, and Mode**: In a normal distribution, the mean, median, and mode are all the same and located at the center of the distribution.
- **Defined by Mean and Standard Deviation**: The shape and position of the normal distribution are defined by two parameters:the mean (μ) and the standard deviation (σ).The mean (μ) determines the center of the distribution.
The standard deviation (σ) determines the spread or width of the distribution. A smaller standard deviation results in a narrower curve, while a larger standard deviation results in a wider curve.
- Empirical Rule (68-95-99.7 Rule):

    1.About 68% of the data falls within one standard deviation of the mean (μ ± σ).\n
    2.About 95% of the data falls within two standard deviations of the mean (μ ± 2σ).\n
    3.About 99.7% of the data falls within three standard deviations of the mean (μ ± 3σ).
                    

Real-World Examples:
- Heights of People: The heights of adults in a population tend to follow a normal distribution.
- Test Scores: Scores on standardized tests like the SAT often follow a normal distribution.
- Measurement Errors: In many scientific experiments, the errors in measurements tend to be normally distributed.

                    
### use of Normal distribution in ML:
1. Feature Distribution:
Many machine learning algorithms assume that the input features follow a normal distribution. If the data is normally distributed, these algorithms can perform better.
Techniques like normalization (scaling data to have a mean of 0 and a standard deviation of 1) can help transform features to follow a normal distribution.
2. Parameter Estimation:
In algorithms like linear regression, normal distribution assumptions help in estimating parameters efficiently. For example, the ordinary least squares method assumes that the errors (residuals) are normally distributed.
3. Central Limit Theorem:
This theorem states that the sum of a large number of independent and identically distributed random variables tends to follow a normal distribution. This is crucial for the validity of many statistical methods used in machine learning, especially hypothesis testing and confidence interval estimation.
4. Gaussian Naive Bayes:
This is a classification algorithm based on Bayes' theorem, which assumes that the features follow a normal distribution. The assumption simplifies the computation of probabilities and makes the algorithm efficient.
5. Performance Metrics:
Many performance metrics (like the mean squared error in regression) are based on the assumption of normality. Understanding the distribution of errors can help in diagnosing model performance.
6. Anomaly Detection:
In anomaly detection, assuming normal distribution helps in identifying outliers. Data points that deviate significantly from the normal distribution can be considered anomalies.
7. Probabilistic Models:
Probabilistic models, such as Gaussian Mixture Models (GMMs), rely on the normal distribution to model the probability density of the data. GMMs are used in clustering, density estimation, and anomaly detection.
8. Dimensionality Reduction:
Techniques like Principal Component Analysis (PCA) assume that the data is normally distributed around the principal components. This assumption helps in identifying the directions of maximum variance and reducing the dimensionality of the data.
Example:
Suppose you are using linear regression to predict house prices based on features like size, number of bedrooms, and location. Here’s how the normal distribution comes into play:

Parameter Estimation: The linear regression model estimates coefficients assuming that the errors (differences between actual and predicted prices) are normally distributed. This assumption helps in making reliable predictions and calculating confidence intervals for the coefficients.

Feature Scaling: Before fitting the model, you might scale the features to have a mean of 0 and a standard deviation of 1, making them resemble a normal distribution. This step ensures that the model treats all features equally, leading to better performance.

Error Analysis: After fitting the model, you analyze the residuals (errors). If the residuals are normally distributed, it indicates that the model fits the data well. If not, it might suggest that the model is missing some patterns in the data.

Also, based on specific ML algorithms

1. **Linear Regression**:
Assumption: The residuals (errors) of the model should be normally distributed.
Why: This assumption allows for the estimation of regression coefficients using the ordinary least squares method. It also helps in making reliable predictions and calculating confidence intervals and p-values for the coefficients.
2. **Logistic Regression**:
Assumption: While logistic regression does not require the predictors to be normally distributed, the method of maximum likelihood estimation (used to find the coefficients) assumes large sample sizes where the distribution of the sample mean is approximately normal (Central Limit Theorem).
3. **Gaussian Naive Bayes**:
Assumption: The algorithm assumes that the features follow a normal (Gaussian) distribution.
Why: This assumption simplifies the calculation of the likelihood of the data given the class. The Gaussian distribution is used to estimate the probability density function for continuous features.
4. **Linear Discriminant Analysis (LDA)**:
Assumption: The algorithm assumes that the data from each class is normally distributed with a common covariance matrix.
Why: This assumption allows LDA to find the linear combinations of features that best separate the classes.
5. Quadratic Discriminant Analysis (QDA):
Assumption: Similar to LDA, QDA assumes that the data from each class is normally distributed, but each class can have its own covariance matrix.
Why: This provides more flexibility in modeling the distribution of each class compared to LDA.
6. Gaussian Mixture Models (GMMs):
Assumption: The data is assumed to be generated from a mixture of several Gaussian distributions with unknown parameters.
Why: GMMs are used for clustering, density estimation, and anomaly detection. Each component of the mixture represents a cluster and follows a Gaussian distribution.
7. Principal Component Analysis (PCA):
Assumption: PCA assumes that the data is normally distributed around the principal components.
Why: This assumption helps in identifying the directions of maximum variance. PCA transforms the data into a new coordinate system where the greatest variance comes to lie on the first coordinate (principal component), the second greatest variance on the second coordinate, and so on.
8. Multivariate Normal Distribution in Bayesian Methods:
Assumption: In Bayesian statistics, prior and posterior distributions can often be assumed or modeled as multivariate normal distributions.
Why: The normal distribution's properties simplify the computation of the posterior distribution. Many Bayesian algorithms rely on these properties to update beliefs about the data.
9. Support Vector Machines (SVMs) with RBF Kernel:
Assumption: Although SVMs do not assume normal distribution, the Radial Basis Function (RBF) kernel is based on the Gaussian function.
Why: The RBF kernel maps the input data into an infinite-dimensional space where it becomes easier to find a linear separation between different classes. The shape of the Gaussian function helps in defining the similarity between data points.

**Summary**:
Linear Regression and Logistic Regression: Residuals should be normally distributed for reliable estimation and inference.
Gaussian Naive Bayes: Assumes features are normally distributed for probability estimation.
LDA and QDA: Assume normal distribution of features for each class to model decision boundaries.
GMMs: Use multiple Gaussian distributions to model data for clustering and density estimation.
PCA: Assumes data is normally distributed around principal components for dimensionality reduction.
Bayesian Methods: Often use multivariate normal distributions for prior and posterior beliefs.
SVM with RBF Kernel: Uses Gaussian function to map data to a higher-dimensional space.
                                                            
                    """)