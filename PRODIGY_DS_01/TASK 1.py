import matplotlib.pyplot as plt


import seaborn as sns


import pandas as pd


import numpy as np


np.random.seed(0)

temperature_data = np.random.normal(loc=25, scale=5, size=100)  # mean=25°C, std=5



df = pd.DataFrame({'Temperature': temperature_data})


sns.histplot(df['Temperature'], bins=10, kde=True, color='skyblue')

plt.title('Temperature Distribution')

plt.xlabel('Temperature (°C)')

plt.ylabel('Frequency')

plt.grid(True)

plt.show()
