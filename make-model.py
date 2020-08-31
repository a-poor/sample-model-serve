
import pickle

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

# Load the data
iris = load_iris()
data = iris["data"]
X = data[:,2].reshape((-1,1))
y = data[:,3]

# Create the model
model = LinearRegression().fit(X,y)
score = model.score(X,y)

# Save the model
with open("model.pkl","wb") as f:
    pickle.dump(model,f)

# Plot the data & model
X_ = np.linspace(X.min(),X.max(),100).reshape((-1,1))
y_ = model.predict(X_)
plt.scatter(X,y,label="data points")
plt.plot(X_,y_,label="model predictions")
plt.xlabel(iris["feature_names"][2])
plt.ylabel(iris["feature_names"][3])
plt.title("Iris Dataset Petal-Width Model Prediction")
plt.legend()
plt.savefig("plots/iris_data.png")


