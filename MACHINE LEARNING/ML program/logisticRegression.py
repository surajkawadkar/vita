import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  confusion_matrix

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 0, 1, 1])
print('X=',x)
print('Y=',y)

model = LogisticRegression()

model.fit(x, y)
print('Alpha:',model.intercept_)
print('Beta:',model.coef_)

print('Predicted output:',model.predict(x))
print(model.predict_proba(x))
print('Accuracy:',model.score(x,y))
print('Confusion Matrix:')
print(confusion_matrix(y,model.predict(x)))