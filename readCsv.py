import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
m =pd.read_csv("studentGrades.csv")
m.rename({"Unnamed: 5":"PER%"},axis=1,inplace=True)
print(m)
m.describe()
Y = m['PER%']
sems =['S3GP','S4GP']
X =m[sems]
p = DecisionTreeRegressor(random_state=1)
p.fit(X,Y)
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(p.predict(X.head()))
train_x , val_x ,train_y ,val_y = train_test_split(X,Y,random_state=1)
q= DecisionTreeRegressor(random_state=1)
q.fit(train_x,train_y)
pv = q.predict(val_x)

print("pv",pv)
print("valy",val_y)

v_mae = mean_absolute_error(pv,val_y)
print("vmae",v_mae)






"""r=m.loc[1]#.tolist()
print(len(r))
l=[]
for i in r[1:]:
    print(type(i))
    #if type(i)!="str":
    if i > 0 and i<=10:
        l.append(i)
        
print(l)

print(m.loc[13][1:7])
print(m.loc[13][1:7].sum())



#m.drop(["Aftab"],axis=0,inplace=True)

import csv
with open('studentGrades.csv', 'a' ,newline ='') as f:
    tw =csv.writer(f)
    m.drop(["Aftab"],axis=0,inplace=True)
    tw.dialect(

def pcalc(roll ,nos, m):
    sum=m.loc[roll][1:7].sum()
    #for i in range (0,nos):
       # sum += m[i]
    cgpa=sum/nos

    percentage = (7.1*cgpa)+11
    print("\n CGPA :",cgpa)
    
    return percentage
#m.insert(5,m.p['Jagannath'],90.4)

pcalc(4,4,m)
"""
