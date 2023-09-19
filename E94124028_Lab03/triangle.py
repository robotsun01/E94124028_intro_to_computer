S1 = int(input("請輸入第一個邊長:"))
S2 = int(input("請輸入第二個邊長:"))
S3 = int(input("請輸入第三個邊長:"))

if S1 + S2 > S3 and abs(S1- S2) < S3:
   if S1 == S2 == S3 :
      print("這是一個正三角形")
   elif S1 == S2 or S2 == S3 or S1 == S3:
       print("這是一個等腰三角形")
   else:
       print("這是一個一般三角形")
else:
    print("這三個邊不能構成一個合法的三角形")
      
