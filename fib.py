for i in range(1,101):
    sum=3*i
    for j in range(1,101):
        sum=3*i+2*j
        for k in range(1,101):
            sum=3*i+2*j+0.5*k
            if(sum==100 and i+j+k==100):
                print(i,j,k)