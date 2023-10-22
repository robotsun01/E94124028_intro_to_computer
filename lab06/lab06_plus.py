def function(str): #創建function函數
    if len(str)==1: #第一次時，迴傳原始字串
        return [str[0]]
    List = [] #建立空白的list
    for idx, c in enumerate(str): #配對字串對應的索引
        List += [c+substr for substr in function(str[:idx] + str[idx+1:])] #維持第一個數，將後面的數利用遞迴，進行排列組合，並將所有可能加入List

    return List

print(list(set(function(input(("輸入字串: ")))))) #將輸入的字串轉成set排除重複，再轉為list