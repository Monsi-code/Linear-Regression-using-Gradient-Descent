# Linear-Regression-using-Gradient-Descent
Assuming that you have a set of data going on, and you want to build the machine that look into the data, plotting it on the graph, and then drawing a function that will further predict the value of the data is going to be.

We are going to perform this using pre-knowledge like: y = mx+b, and gradient descent

# The tutorial for the project (I will only explain the mathematics and the logic behind, for the code, take a look at the main.py) 
# Set up
1. In every machine learning, you will first have to collect a set of data (you can download the "hours_vs_scores.csv" file and use it as your training data set). The file of data is going to be saved under the form of csv. what is csv file: https://allthings.how/what-is-a-csv-file-and-how-to-open-or-create-it/ (Check this link out to know what the csv file is)
2. Now that you have the dataset downloaded, create a folder where you want to save your project, and move that csv file into the folder. Next, create the python file, you can name it anyways you want .py (This is where all the code will be in)

# Installing required libraries and modules
1. First of all, make sure you install and import all the necessaries modules and libraries that we will work with including: pandas, matplotlib, numpy.
    1. Pandas: an open-source Python library designed to manipulate and working with data. In our case, we will use it to access our data file in the python script. (https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
    2. Matplotlib: Using for data visualization. Imagine this, you have a set of datas in number, now you want to create the graph and plot those data on the graph --> This is where Matplotlib comes in, it helps you to actually visualize the data and see what is actually going on instead of just reading those boring numbers. (https://matplotlib.org/stable/tutorials/index.html)
    3. numpy: https://numpy.org/doc/stable/user/index.html#user

4. For installation instruction: (make sure you take a look at what version does the modules or library support with your python, usually mentioning at the top of the page)
   1. Pandas: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
   2. matplotlib: https://matplotlib.org/stable/install/index.html
   3. numpy: https://numpy.org/install/
  
# Mathematics
1. The first thing you need to do is to draw a random function. Now imagine, you have a graph with a bunch of red plots illustrate your data set. Your goal now is to draw a random function, takes the y-value (dependent value) of the function and compared it with the actual y-value (the red plot) with corresponding x-value (independent value), therefore you get the differences between your prediction and the actual value. To do this, you need the function formula: y = mx + b, initialize m and b with any value you want, then write the code to perform the equation, the y value for this equation is your predicted value. In the data set that I give you, we have 100 points in there, and that means you have to do this step 100 times, calculating the differences between the predicted value and the actual value for each point. Finally after calculating the error for each point, make sure you create the list and store those value inside the list (basic python review). This is the mathematics, if you want to know specifically how to code, read the file "main.py".
2. When calculated the error for each point, you have to square that error, store it in a list, and at the end, takes all of the error value, add it up together and divdided by 100 (the amounts of points you have). By doing this, you now have the thing that we called "mean squared error".
3. Next step is to calculate the gradient: 
