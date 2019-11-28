import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.html.table_schema', True)
import numpy as np
import seaborn as sns
from IPython.display import HTML



def inputSemMarks():
    nos=int(input("\nEnter the no of semesters :"))
    l =[]
    for i in range(1,nos+1):
        print("Enter sgpi in sem",i)
        e=float(input())
        l.append(e)
    return nos,l

def pcalc(nos , m):
    """                                            This method takes Two parameters
                                                    nos : no. of semesters
                                                    m: list of marks in semestes."""
    sum=0
    for i in range (0,nos):
        sum += m[i]
    cgpa=sum/nos
    cgpa = round(cgpa,2)
    percentage = (7.1*cgpa)+11
    #print("\n CGPA :",cgpa)
    percentage =round(percentage,2)
    return percentage,cgpa

def addRecord(r,nos,f):   
    """                                     This method takes a list as an argument and
                                            adds the list into a csv file."""
    
    import csv
    with open(f, 'a' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(r)
    
    print(r)

def drawGraph(nos,l,name):
    plt.style.use('ggplot')
    semesters =['I','II','III','IV','V','VI']
    sems =semesters[:nos]
    sgpi = l #[8.2 , 8.2 , 9.2 , 9.8]
    """                                             This method takes Two parameters
                                                    nos : units on the x axis
                                                    l : list of size nos.
                                                    and returns the graph plot."""
    p =pcalc(nos,l)
    plt.xlabel("Semesters")
    plt.ylabel("SGPI")
    plt.title("Progress Graph of "+name+" in Degree")
    #plt.text(1.5,l[nos-2],name+" "+str(p))
    plt.text(0, l[nos-2], "Percent: "+str(p[0])+"\n CGPA: "+str(p[1]), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    plt.plot(sems,sgpi)
    plt.scatter(sems,sgpi)
    plt.show()

def readAllRecords(f):
    import pandas as pd
    m =pd.read_csv(f,index_col=0)
    m =m.sort_values(by=['RollNo'])
    return m

def updateRecord(m,f):
    rollNo = int(input("Enter RollNo. of the Student :"))
    col = input("Enter name of the col :")
    val = (input("Enter the new value:"))
    #print(m)
    r=m.loc[rollNo].tolist()
    print(r)
    
    if col =='Name':
        r.pop(0)
        r.insert(0,val)
  
    elif col =='S1GP':
        del r[1:3]
        r.insert(1,float(val))
        r.insert(2,gradeCal([float(val)])[1])
        
    elif col =='S2GP':
        del r[3:5]
        r.insert(3,float(val))
        r.insert(4,gradeCal([float(val)])[1])
        
    elif col =='S3GP':
        del r[5:7]
        r.insert(5,float(val))
        r.insert(6,gradeCal([float(val)])[1])
        
    elif col =='S4GP':
        del r[7:9]
        r.insert(7,float(val))
        r.insert(8,gradeCal([float(val)])[1])
        
    elif col =='S5GP':
        del r[9:11]
        r.insert(9,float(val))
        r.insert(10,gradeCal([float(val)])[1])
        
    elif col =='S6GP':
        del r[11:13]
        r.insert(11,float(val))
        r.insert(12,gradeCal([float(val)])[1])
        

    
        
    l=[]
    for i in range (1,len(r[1:13]),2):
        if r[i] > 0 and r[i]<=10:
            l.append(r[i])
    p=pcalc(len(l),l)
    
    r.insert(0,rollNo)
    r.insert(16,p[0])
    r.pop()
    del r[14:16]
    g = gradeCal([p[1]])
    r.insert(14,round(g[0],2))
    r.insert(15,g[1])

    import pandas as pd
    rm =pd.read_csv(f)

    import csv
    with open(f, 'w' ,newline ='') as hf:
        tw =csv.writer(hf)
        tw.writerow(['RollNo','Name','S1GP','S1G','S2GP','S2G','S3GP','S3G','S4GP','S4G','S5GP','S5G','S6GP','S6G','CGPA','OAG','PER%'])
    for i in range(0,rm.shape[0],1):
        row = rm.iloc[i]
        if row[0] == rollNo:
            row=r
        import csv
        with open(f, 'a' ,newline ='') as of:
            tw =csv.writer(of)
            tw.writerow(row)
    
    print("updated record:",r)

def deleteRecord(name , rollNo ,f):
    import pandas as pd
    rm =pd.read_csv(f)
    r=[]
    #r=rm.loc[rollNo].tolist()
    import csv
    with open(f, 'w' ,newline ='') as hf:
        tw =csv.writer(hf)
        tw.writerow(['RollNo','Name','S1GP','S1G','S2GP','S2G','S3GP','S3G','S4GP','S4G','S5GP','S5G','S6GP','S6G','CGPA','OAG','PER%'])
    for i in range(0,rm.shape[0],1):
        row = rm.iloc[i]
        
        if row[0] == rollNo and row[1] == name:
            r=row.tolist()
            row=[]
        import csv
        with open('studentGrades.csv', 'a' ,newline ='') as f:
            tw =csv.writer(f)
            tw.writerow(row)
    print("deleted record:",r)

def gradeCal(l):
    g = []
    for i in l:
        if i>0 and i<4:
            g.append(i)
            g.append('F')
        elif i>=4 and i<5:
            g.append(i)
            g.append('D')
        elif i>=5 and i<6:
            g.append(i)
            g.append('C')
        elif i>=6 and i<7:
            g.append(i)
            g.append('B')
        elif i>=7 and i<8:
            g.append(i)
            g.append('B+')
        elif i>=8 and i<9:
            g.append(i)
            g.append('A')
        elif i>=9 and i<10:
            g.append(i)
            g.append('A+')
        elif i==10 :
            g.append(i)
            g.append('O')
    return g


f='studentGrades.csv'
print("This program can perform operations on the marks(SGPI) of the Students.")
print("Below is the list of operations this program does.")
print("Press '1' to calculate CGPI and Percentage.")
print("Press '2' to store marks of a student into a file.")
print("Press '3' to Draw a graph of the progress in acedemic SGPI's.")
print("Press '4' to view all the records in file.")
print("Press '5' to update a perticular record.")
print("Press '6' to delete a perticular record.")
print("Press '0' to Exit.")
c='y'

while c=='Y' or c=='y':
    
    print("===========================================================================================================")
    ch=int(input("\nEnter your choice:"))

    if ch==1:
        print("\nTo calculate CGPI and Percentage.")
        l=inputSemMarks()
        print(l[1])
        p =pcalc(l[0],l[1])
    
        print("CGPA is:"+str(p[1])+"\npercentage is:",str(p[0]))
        

    elif ch==2:
        print("\nTo store marks of a student into a file.")
        name = input("Enter Name of the Student :")
        rollNo = int(input("Enter RollNo. of the Student :"))
        l = inputSemMarks()
        r=[]
        r.append(rollNo)
        r.append(name)
        g = gradeCal(l[1])
        if l[0] ==2 :
            r = r+g+['','','','','','','','']
        elif l[0] ==3:
            r = r+g+['','','','','','']
        elif l[0] ==4:
            r = r+g+['','','','']
        elif l[0] ==5:
            r = r+g+['','']
        elif l[0] ==6:
            r = r+g

        
        else:
            print("This program does not supports to save the marks more the 6 semesters.")
        p =pcalc(l[0],l[1])
        print("CGPA is:"+str(p[1])+"\npercentage is:",str(p[0]))
        r =r + gradeCal([p[1]])
        r.append(p[0])
        addRecord(r,l[0],f)

    elif ch==3:
        print("To Draw a graph of the progress in acedemic SGPI's.")
        name = input("Enter Name of the Student :")
        rollNo = int(input("Enter RollNo. of the Student :"))
        #l=inputSemMarks()
        m =readAllRecords(f)
        r=m.loc[rollNo].tolist()
        l=[]
        for i in range (1,len(r[1:13]),2):
            if r[i] > 0 and r[i]<=10:
                l.append(r[i])
        drawGraph(len(l),l,name)

    elif ch==4:
        print("All the records in file.")
        m =readAllRecords(f)
        print(m)

    elif ch==5:
        print("To update a perticular record.")
        m=readAllRecords(f)
        updateRecord(m,f)
        #m =readAllRecords(f)
        #print(m)
        print("\n Record Updated Sucessfully...")

    elif ch==6:
        print("To delete a perticular record.")
        name = input("Enter Name of the Student :")
        rollNo = int(input("Enter RollNo. of the Student :"))
        deleteRecord(name , rollNo ,f)
        #m=readAllRecords(f)
        #print(m)
        print("\n Record Deleted Sucessfully...")
        
    elif ch==0:
        c=input("\n If u don't want to Exit press 'Y/y' else 'N/n' :")
