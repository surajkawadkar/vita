import numpy as np
from sklearn.linear_model import LinearRegression


x = np.array([43, 67, 25, 42, 57, 79, 52, 84, 33, 67, 52, 50]).reshape((-1, 2))
y = np.array([99, 65, 79, 75, 87, 81])

print(x)
model = LinearRegression()

model.fit(x, y)

print('intercept (alpha):', model.intercept_)
print('slope (beta):', model.coef_)


#prediction for the training data
y_pred = model.predict(x)
print('predicted response for trining data:', y_pred, sep='\n')


#prediction for new input
x_pred = [45, 72]
x_pred = np.array(x_pred).reshape(-1,2)
y_pred = model.predict(x_pred)
print('predicted response for new input:', y_pred, sep='\n')