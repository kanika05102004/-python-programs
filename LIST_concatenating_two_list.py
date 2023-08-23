#concatenating two list 
list1=["m","na","i","kan"]
list2=["y","me","s","ika"]
list3=[i+j for i,j in zip(list1,list2) ]
print(list3)