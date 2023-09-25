nums = [3,2,2,3,6,5,4,3,2,1]
print("輸入的list為 : ",nums)
val = int(input("要刪除的數字是 : "))
while (val in nums):
    nums.remove(val)
print("刪除後!")
print("list長度剩下 : ",len(nums),", ","list變成 : ",nums)