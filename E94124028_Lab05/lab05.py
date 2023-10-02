dict0 = {"index" : ("國文","英文","數學","自然","社會") , "StuA" : (50,60,70,80,90) , "StuB" : (57,86,73,82,43) , "StuC" : (97,96,86,97,83)}
print(dict0) #輸出整個dict0字典
totle = list(dict0.values())
index = totle[0]
StuA_score = totle[1]
StuB_score = totle[2]
StuC_score = totle[3]
A_sum = 0
B_sum = 0
C_sum = 0
for i in StuA_score: #計算出每個學生的總成績
    A_sum += i 
for j in StuB_score:
    B_sum += j
for k in StuC_score:
    C_sum += k 
print("A學生平均成績 : ", A_sum/5) #print出每個學生的平均成績
print("B學生平均成績 : ", B_sum/5)
print("C學生平均成績 : ", C_sum/5)
print(" ")
for a in range(5): #計算並print出每個科目的平均成績
    print(index[a],"平均成績 : ",(StuA_score[a]+StuB_score[a]+StuC_score[a])/3,sep='')