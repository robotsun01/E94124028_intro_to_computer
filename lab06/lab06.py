def gcd(a, b): #定義函數def
    if b > a: #將a設為一定會大於b
        a,b = b,a
    if b == 0: #分母不能為0
        print("0 沒有gcd")
    elif a % b == 1: #若是除到最後餘數為1則互質
        print(f"{a} 和 {b} 互質")
    else:
      if a % b == 0: #除到最後找出最大公因數
          print(f"{a} 和 {b} 的gdc= ",b)
      else:
          return gcd(b, a %b ) #利用遞迴進行輾轉相除法

ans1 = gcd(80,20)
ans2 = gcd(10, 0)
ans3 = gcd(19,20)