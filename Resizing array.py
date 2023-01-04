#Resizing the array
#As we can't change it we will create a new array
a = [5,4,3,2,1]
b = [0]*(len(a)+3)
for i in range(len(a)):
  b[i]=a[i]
print(b) #Finally we got the extra space that we needed
 #coping then increasing