# Logist Regression

Logistic Regression is a statistical method used for binary classification. It is used to model the probability of a certain 
class or event occurring. The goal is to find the best-fitting model that will predict the probability of an event occurring.

The logistic regression model can be represented by the following equation:

`p(y=1|x) = 1 / (1 + e^(-beta_0 - beta_1*x_1 - beta_2*x_2 - ... - beta_n*x_n))`

where p(y=1|x) is the probability of the event occurring, x_1, x_2, ..., x_n are the independent variables, 
beta_0, beta_1, beta_2, ..., beta_n are the coefficients that determine the slope of the line for each independent variable.

In terms of implementation, the scikit-learn library in Python provides an easy-to-use implementation of logistic regression 
through the LogisticRegression class. Here is an example of how to use it:

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 1, 1, 0, 1])

# Create an instance of the LogisticRegression class
model = LogisticRegression()

# Fit the model to the data
model.fit(x, y)

# Print the coefficients
print(model.coef_)

# Print the intercept
print(model.intercept_)
```

This will output the coefficients and intercept of the model that best fits the data.
