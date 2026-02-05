import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

movies = pd.DataFrame({
    'title':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'year':[2000, 2001, 2004, 2009, 2008, 2010, 2013, 2015],
    'genre':['comedie', 'action', 'drama', 'documentry', 'action', 'drama', 'comedie',
             'documentry'],
    'runtime':[85, 87, 120, 96, 110, 109, 115, 94],
    'rating':[1, 4, 6, 5, 9, 3, 8, 5],
    'vote':[150000, 230000, 120000, 210000, 80000, 30000, 20000, 50000],
    'boxoffice':[120, 340, 290, 840, 570, 390, 45, 56]
    })
sns.scatterplot(data=movies, x="boxoffice", y="rating")
plt.title("title vs rating")
plt.show()
movies.head()
med = movies['boxoffice'].median()
mean = movies['boxoffice'].mean()

print(med)
print(mean)
movies.info()