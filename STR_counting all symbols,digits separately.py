#counting all symbols,digits separately
str="hh23!R$45w89^*5gk"
char_count=0
digit_count=0
symbol_count=0
for char in str:
  if char.isalpha(): 
    char_count+=1
  elif char.isdigit():
    digit_count+=1
  else:
    symbol_count+=1
    
print("char :",char_count)
print("digits:",digit_count)
print("symbols:",symbol_count)