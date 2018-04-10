A =[10,9,8,3,1,0]
def order(A):
for i in range(len(A) - 1): 
if ((A[i]>A[i+1])) :
return False
return True
