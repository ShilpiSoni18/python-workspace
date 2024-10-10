import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2020,2021,2022,2023])
grades = np.array([90,85,69,70])
 
 #show data in graph- line(x,y),pie(x),
 # bar (x,y), scatters(x,y)
plt.plot(years,grades,marker = 'o')
plt.title("academic growth")
plt.xlabel("passing year")
plt.ylabel("student marks")
plt.show()