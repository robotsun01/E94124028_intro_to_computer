a = ["A"]
b = ["B"]
c = ["C"]
for i in range(1,4):
    for j in range(1,4):
        if i == 1:
           if j == 1:
            print("輸入A學生成績")   
            a.append(int(input("國文:")))
           elif j == 2:    
            a.append(int(input("數學:")))
           else:    
            a.append(int(input("英文:")))
            a.append(round((a[1]+a[2]+a[3])/3,1))
        elif i == 2:
           if j == 1:
            print("輸入B學生成績")   
            b.append(int(input("國文:")))
           elif j == 2:    
            b.append(int(input("數學:")))
           else:    
            b.append(int(input("英文:")))
            b.append(round((b[1]+b[2]+b[3])/3,1))    
        else:
           if j == 1:
            print("輸入C學生成績")   
            c.append(int(input("國文:")))
           elif j == 2:    
            c.append(int(input("數學:")))
           else:    
            c.append(int(input("英文:")))
            c.append(round((c[1]+c[2]+c[3])/3,1))    
print(a)
print(b)
print(c)
