def pcalc(nos , m):
    sum=0
    for i in range (0,nos):
        sum += m[i]
    cgpa=sum/nos

    percentage = (7.1*cgpa)+11
    print("\n CGPA :",cgpa)
    return percentage

c = 'y'
while c=='Y' or c=='y':
    
    nos=int(input("\n Enter the no of semesters:"))
    l =[]
    for i in range(1,nos+1):
        print("Enter sgpi in sem",i)
        e=float(input())
        l.append(e)
    print(l)

    print("percentage is:",pcalc(nos,l))


    c= input("\n For one more time press 'Y/y' and if Not 'N/n' :")

print("\n Thank you!!")
    
