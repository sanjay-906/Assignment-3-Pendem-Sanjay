import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("D:\dataset\diabetes.csv")
df
df.columns
features=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
X=df[features]
y=df.BMI

plt.plot(X,y)
plt.show()
#scatterplot
sns.scatterplot(x=df['Pregnancies'],y=df['Glucose'],color='red')
plt.show()
#histogram
plt.hist(df['Pregnancies'],bins=40)
plt.show()
#boxplot
sns.boxplot(df['Pregnancies'],color='green',orient='h')# Write your code here :-)
