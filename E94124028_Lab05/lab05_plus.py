dict0 = dict()
for b in range(1,5): #輸入keys
    number = list()
    title = input()
    for c in range(1,6): #輸入每個values
        if b == 1:
            number0 = input()
            number.append(number0)
        else:
            number0 = int(input())
            number.append(number0)
    dict0.setdefault(title,number)
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