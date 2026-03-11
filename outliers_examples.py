import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df= pd.read_csv('meus_dados_titanic.csv')

sns.boxplot(x= df['age'])
plt.show()
