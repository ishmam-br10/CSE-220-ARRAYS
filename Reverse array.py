#reverse array
a = [1,2,3,4,5]
b = [0]*len(a)
for i in range(1, len(a)+1): # it will go to the a's length + 1 , starts from 1 because negative index of '0' is just zero
  b[i-1] = a[- i] # positive index of b e amra a er reverse gula implement korbo
print(b)

