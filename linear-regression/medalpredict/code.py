import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
teams = pd.read_csv("teams.csv")
teams = teams[["team","country","year","athletes","age","prev_medals","medals"]]
#print(teams)

sb.lmplot(x="athletes",y="medals",data=teams,fit_reg=True,ci=None)
print(teams[teams.isnull().any(axis=1)])
teams.plot.hist(y="medals")
plt.show()
