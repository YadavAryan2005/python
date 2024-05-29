a=[4,3,2,1]
for pas in range(1,len(a)):
    for i in range(0,len(a)-pas):
        if(a[i]>a[i+1]):
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t

print(a)