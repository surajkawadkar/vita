import matplotlib.pyplot as plt 
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([43, 21, 25, 42, 57, 59]).reshape((-1, 1))
y = np.array([99, 65, 79, 75, 87, 81])

model = LinearRegression()

model.fit(x, y)

print('intercept (alpha):', model.intercept_)
print('slope (beta):', model.coef_)


#prediction for the training data
y_pred = model.intercept_ + model.coef_ * x
print('predicted response for trining data:', y_pred, sep='\n')

plt.scatter(x,y)
plt.plot(x, model.intercept_ + model.coef_[0]*x, 'r')
plt.show()

#prediction for new input
x_pred = 25
y_pred = model.intercept_ + model.coef_ * x_pred
print('predicted response for new input:', y_pred, sep='\n')