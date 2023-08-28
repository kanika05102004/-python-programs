#calculating sum and avg of digits in str
str="ckuvho145^*^"
sum=0
count=0
print(len(str))
for char in str:
  if char.isdigit():
    sum+=int(char)
    count+=1
print("sum =",sum)
avg=(sum/count)
print("average=",avg)