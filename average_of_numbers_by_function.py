#average of numbers by function
def average(*number):
  sum=0
  for i in number:
    sum=sum + i
  return sum/len(number)
c=average(5,2,3,6)
print(c)
  