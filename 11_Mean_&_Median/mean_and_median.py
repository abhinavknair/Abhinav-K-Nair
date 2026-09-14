import numpy as np

N=100
x=np.random.uniform(0,1,N)
mean=np.mean(x)
median=np.median(x)

#sorting the data in ascending order
for i in range(len(x)):
  for j in range(0,len(x)-i-1):
    if x[j]>x[j+1]:
      x[j],x[j+1]=x[j+1],x[j]
#print(x)

#finding the median
if len(x)%2==1:
  median_t=x[len(x)//2]
elif len(x)%2==0:
  median_t=(x[(len(x)-1)//2]+x[len(x)//2])/2
print("median_t:",median_t)

#finding the mean
for i in range(1,len(x)):
  x[i]=x[i-1]+x[i]
  #print(x[i])
mean_t=x[i]/len(x)

print("mean_t:",mean_t)
print("mean:",mean)
print("median:",median)
