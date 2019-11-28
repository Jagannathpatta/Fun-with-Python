"""from goto import with_goto

@with_goto
def range(start, stop):
        i = start
        result = []

        label .begin
        if i == stop:
            goto .end

        result.append(i)
        i += 1
        goto .begin

        label .end
    return result
"""
def pcalc(nos , m):
    """                                            This method takes Two parameters
                                                    nos : no. of semesters
                                                    m: list of marks in semestes."""
    sum=0
    for i in range (0,nos):
        sum += m[i]
    cgpa=sum/nos

    percentage = (7.1*cgpa)+11
    #print("\n CGPA :",cgpa)
    percentage =round(percentage,2)
    return percentage,cgpa

def updateRecord(m,f):
    rollNo = int(input("Enter RollNo. of the Student :"))
    #name = input("Enter name of the studend u want update record of :")
    col = input("Enter name of the col :")
    val = float(input("Enter the new value:"))
    #m.loc[rollNo][col]=val
    print(m)
    r=m.loc[rollNo].tolist()
    print(r)
    if col =='SEM1':
        r.pop(1)
        r.insert(1,val)
        
    elif col =='SEM2':
        r.pop(2)
        r.insert(2,val)
        
    elif col =='SEM3':
        r.pop(3)
        r.insert(3,val)
        
    elif col =='SEM4':
        r.pop(4)
        r.insert(4,val)
        
    elif col =='SEM5':
        r.pop(5)
        r.insert(5,val)
        
    elif col =='SEM6':
        r.pop(6)
        r.insert(6,val)
        
    l=[]
    for i in r[1:]:
        if i > 0 and i<=10:
            l.append(i)
    p=pcalc(len(l),l)
    #m.loc[rollNo]["PER%"]=p[0]
    #r=m.loc[rollNo].tolist()
    #r.append(p[0])
    r.insert(0,rollNo)
    r.insert(8,p[0])
    r.pop()

    import pandas as pd
    rm =pd.read_csv(f)

    import csv
    with open('DDstudentGrades.csv', 'w' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(['RollNo','Name','SEM1','SEM2','SEM3','SEM4','SEM5','SEM6','PER%'])
    for i in range(0,16,1):
        row = rm.iloc[i]
        if row[0] == rollNo:
            row=r
        import csv
        with open('DDstudentGrades.csv', 'a' ,newline ='') as f:
            tw =csv.writer(f)
            tw.writerow(row)
        
    """import csv
    with open(f, 'a' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(r)"""
    #m.drop_duplicates(["Name"],keep='last', inplace=True)
    print("updated record:",r)

def readAllRecords(f):
    import pandas as pd
    m =pd.read_csv(f, index_col=0)
    m =m.sort_values(by=['RollNo'])
    return m

def deleteRecord():
    import pandas as pd
    rm =pd.read_csv('DDstudentGrades.csv')

    import csv
    with open('DDstudentGrades.csv', 'w' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(['RollNo','Name','SEM1','SEM2','SEM3','SEM4','SEM5','SEM6','PER%'])
    for i in range(0,rm.shape[0],1):
        row = rm.iloc[i]
        if row[0] == 8 and row[1] == 'kkk':
            row=[]
        import csv
        with open('DDstudentGrades.csv', 'a' ,newline ='') as f:
            tw =csv.writer(f)
            tw.writerow(row)
    
from IPython.core.display import HTML

import pandas as pd

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.html.table_schema', True) 
f='studentGrades.csv'
m=readAllRecords(f)
print(m)



"""
r=m.loc[35].tolist()
print(m)
print(r[1:13])
print(len(r[1:13]))
l=[]
for i in range (1,len(r[1:13]),2):
    print(type(r[i]))
    if r[i] > 0 and r[i]<=10:
        l.append(r[i])
print(l)"""
#deleteRecord()
#updateRecord(m,f)
"""for i in range(0,16,1):
    r = m.iloc[i]
    if r[0] == 5:
        r=[5,'kkkkkk',10,10,10,10,10,10,100]
    import csv
    with open('DDstudentGrades.csv', 'a' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(r)
"""
