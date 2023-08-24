#sorting the string
str="SwfCgJbrbCLbbH"
lower=[]
upper=[]
for char in str:
  if char.islower():
    lower.append(char)
  else:
    upper.append(char)
sorted_str=("".join(lower+upper))
print("result:",sorted_str)