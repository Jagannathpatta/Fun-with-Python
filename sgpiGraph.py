import matplotlib.pyplot as plt
import pandas as pd
m =pd.read_csv("fourSems.csv",index_col=0)
s1=m["Name"]
s2=m.loc["Jagannath"]
"""s2=m.loc["Vitthal"]
s3=m.loc["Mohan"]
s4=m.loc["Shailesh"]"""
sems =['I','II','III','IV']
sgpi = [8.2 , 8.2 , 9.2 , 9.8]

#plt.xlabel("Semesters")
#plt.ylabel("SGPI")
plt.title("Progress Graph of _________ in Deggree")

#plt.text(2,8.5,"mohan", style='oblique',bbox={'facecolor': 'Blue', 'alpha': 2.5, 'pad': 10})

#plt.hist([score_india, score_pk], color=['orange', 'green'])
#plt.plot(sems,sgpi)
#plt.scatter(sems,sgpi)
plt.hist(s1,s2, color='orange')
plt.show()
