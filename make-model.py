
import pickle

import numpy as np

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


