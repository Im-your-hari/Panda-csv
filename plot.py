import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("card.csv")
#print(df)

plt.bar(df.Period, df.Data_value,color='r')
#plt.legend()
plt.grid(1)
plt.xlabel("Period")
plt.ylabel("Data_value")
plt.show()