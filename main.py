import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

file = pd.read_csv("hours_vs_scores.csv")
x = file["Hours"]
y  = file["Scores"]

plt.scatter(x,y, color = "red")
plt.xlabel("Time in hours")
plt.ylabel("Scores")
plt.title("The relationship between the amount of hours studying and scores")
plt.show()

#Function to calculate the mean error
m = 1
b = 0
points = len(x)
def predict_value(m, b, x):
    predicted_list = []
    error_list = []
    sum = 0
    for i in range(len(x)):
        y_predicted = m * x[i] + b
        predicted_list.append(y_predicted)
        error = (y_predicted - y[i]) ** 2
        error_list.append(error)
        sum += error
    return sum / len(x)

#Function to calculate the
#This part will be used as global

#Function to calculate gradient m
def gradient_m(m,b,x,y):
    total = 0
    for i in range(len(x)):
        error = (m * x[i] + b) - y[i]
        total += error * x[i]
    return (2/len(x) * total)

#The function to calculate b gradient
def gradient_b(m,b,x,y):
    total = 0 
    for i in range(len(x)):
        error = (m*x[i]+ b) - y[i]
        total += error
    return (2/len(x)*total)

#Minize the error
learningrate = 0.001

#Update for mulas for m and b 
for epoch in range(1000):
    predict_value(m,b,x)
    grad_m = gradient_m(m,b,x,y)
    grad_b = gradient_b(m,b,x,y)
    m = m - learningrate * grad_m
    b = b - learningrate * grad_b

plt.scatter(x, y, color="red")
y_predicted = m * x + b
plt.plot(x, y_predicted, color="blue")
plt.xlabel("Time in hours")
plt.ylabel("Scores")
plt.title("Fitted Line After Gradient Descent")
plt.show()
