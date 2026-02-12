from sklearn.linear_model import LinearRegression 
# y = m * x + b 
# m = 8 and b = 200
# y = 8 * x + 200
x =[[1200], [2000], [1000], [1500], [1400]]
y =[9800, 16200, 8200, 12200, 11400]

model = LinearRegression()
model.fit(x, y)
prediction = model.predict([[3000]])
print(prediction)

