
def pcalc(nos , m):
    sum=0
    for i in range (0,nos):
        sum += m[i]
    cgpa=sum/nos

    percentage = (7.1*cgpa)+11
    print("\n CGPA :",cgpa)
    
    return percentage

import pandas as pd
m =pd.read_csv('studentGrades.csv',index_col=0)
print(m)
#m.drop([15],inplace=True)
#m.drop_duplicates(subset="Name", keep='last', inplace=True)
m.replace('',0)
print(m)
import csv
with open('studentGrades.csv', 'a' ,newline ='') as f:
    tw =csv.writer(f)
    #tw.writerows(m.loc[1:][0:])
    #m.insert(5,'Per%',pcalc(4,m.loc['Jagannath']))
