import matplotlib.pyplot as plt
import pandas as pd


semesters =['I','II','III','IV','V','VI']


def drawGraph(nos,l):
    sems =semesters[:nos]
    sgpi = l #[8.2 , 8.2 , 9.2 , 9.8]
    """                                             This method takes Two parameters
                                                    nos : units on the x axis
                                                    l : list of size nos.
                                                    and returns the graph plot."""
    plt.xlabel("Semesters")
    plt.ylabel("SGPI")
    plt.title("Progress Graph of "+name+" in Degree")
    #plt.text(1.5,l[nos-2],name+" "+str(p))
    plt.text(0, l[nos-2], "Percent: "+str(p[0])+"\n CGPA: "+str(p[1]), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    plt.plot(sems,sgpi)
    plt.scatter(sems,sgpi)
    plt.show()


def updateRecord(m,f):
    name = input("Enter name of the studend u want update record of :")
    col = input("Enter name of the col :")
    val = float(input("Enter the new value:"))
    m.loc[name][col]=val
    
    r=m.loc[name].tolist()
    l=[]
    for i in r:
        if i > 0 and i<=10:
            l.append(i)
    p=pcalc(len(l),l)
    m.loc[name]["PER%"]=p[0]
    r=m.loc[name].tolist()
    r.insert(0,name)
    
    import csv
    with open(f, 'a' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(r)
    #m.drop_duplicates(["Name"],keep='last', inplace=True)
    print("updated record:",r)
    
    

def readAllRecords(f):
    import pandas as pd
    m =pd.read_csv(f,index_col=0)
    m.rename({"Unnamed: 5":"PER%"},axis=1,inplace=True)
    #m.drop_duplicates(["Name"],keep='last',inplace=True)
    
    return m
    
def addRecord(r,nos,f):   
    """                                     This method takes a list as an argument and
                                            adds the list into a csv file."""
    
    import csv
    with open(f, 'a' ,newline ='') as f:
        tw =csv.writer(f)
        tw.writerow(r)
    
    print(r)
    
    


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


#def start():
c='y'
while c=='y'or c=='Y':    
    name = input("Enter Name of the Student :")
    nos=int(input("\n Enter the no of semesters :"))
    l =[]
    for i in range(1,nos+1):
        print("Enter sgpi in sem",i)
        e=float(input())
        l.append(e)
    print(l)
    r=[]
    r.append(name)
    #r = r+l
    p =pcalc(nos,l)
    
    print("CGPA"+str(p[1])+"\npercentage is:",str(p[0]))
    #return r,l,nos,name,p
                
    f='DumystudentGrades.csv'
    if nos ==2 :
        #f='twoSems.csv'
        r = r+l+['','','','']
    elif nos==3:
        r = r+l+['','','']
        #f='threeSems.csv'
    elif nos==4:
        r = r+l+['','']
        #f='fourSems.csv'
    elif nos==5:
        r = r+l+['']
        #f='fiveSems.csv'
    elif nos==6:
        r = r+l
        #f='sixSems.csv'
    else:
        print("This program does not supports to save the marks more the 6 semesters.")

    r.append(p[0])

    arc = input("\nDo u want to add this record in to the file press 'Y/y' and if Not 'N/n' :")
    while arc=='Y' or arc=='y':
            addRecord(r,nos,f)
            arc='n'

    
    grplot = input("\nDo u want the graph representation of your record press 'Y/y' and if Not 'N/n' :")
    while grplot=='Y' or grplot=='y':
        drawGraph(nos,l)
        grplot='n'
        
    m=readAllRecords(f)
    rar = input("\nView all records in the file press 'Y/y' and if Not 'N/n' :")
    while rar =='Y' or rar=='y':
        print(m)
        rar='n'

    updr = input("\nDo u want to update any record press 'Y/y' and if Not 'N/n' :")
    while updr =='Y' or updr=='y':
        updateRecord(m,f)
        updr='n'
        
    c= input("\n For one more time press 'Y/y' and if Not 'N/n' :")






    
    
print("\n Thank you!!")












