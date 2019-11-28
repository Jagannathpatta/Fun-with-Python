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

g = [10,9,8,7,9]
k = [11,12]
print(g)
print(len(g))
del g[1:3]
print(g)
print(len(g))
g.insert(1,gradeCal([9])[1])
print(g)
print(len(g))
