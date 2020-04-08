import numpy as np
print("enter the degree:")
N=input()
hurwitzmatrix=np.zeros((N+1,((N/2)+1)))
print("enter coefficients:")
for i in range(((N/2)+1)):
	hurwitzmatrix[0][i]=input()
for i in range((N/2)+1):
		hurwitzmatrix[1][i]=input()
for i in range(N-1):
	if(N%2==1):
		for j in range(((N-1)/2)):
			if((hurwitzmatrix[i+1][0]!=0)and(not(np.array_equal(hurwitzmatrix[i+1],np.zeros((N/2)+1))))):
				hurwitzmatrix[2+i][j]=(hurwitzmatrix[i][j+1]*hurwitzmatrix[i+1][0]-hurwitzmatrix[i][0]*hurwitzmatrix[i+1][j+1])/(hurwitzmatrix[i+1][0])
			if((hurwitzmatrix[i+1][0]==0)and(not(np.array_equal(hurwitzmatrix[i+1],np.zeros((N/2)+1))))):
				hurwitzmatrix[i+1][0]=0.0000001
				hurwitzmatrix[2+i][j]=(hurwitzmatrix[i][j+1]*hurwitzmatrix[i+1][0]-hurwitzmatrix[i][0]*hurwitzmatrix[i+1][j+1])/(hurwitzmatrix[i+1][0])
		if(((np.array_equal(hurwitzmatrix[i+1],np.zeros((N/2)+1))))):
			hurwitzmatrix[i]=(hurwitzmatrix[i])/(np.gcd.reduce(hurwitzmatrix[i],dtype=int))
			for k in range((N/2)+1):
				hurwitzmatrix[i+1][k]=hurwitzmatrix[i][k]*(N-i-2*k)
			hurwitzmatrix[i+1]=hurwitzmatrix[i+1]/(np.gcd.reduce(hurwitzmatrix[i+1],dtype=int))
			for j in range(((N-1)/2)):
				hurwitzmatrix[2+i][j]=(hurwitzmatrix[i][j+1]*hurwitzmatrix[i+1][0]-hurwitzmatrix[i][0]*hurwitzmatrix[i+1][j+1])/(hurwitzmatrix[i+1][0])
					
	else:
		for j in range(((N)/2)):
			if((hurwitzmatrix[i+1][0]!=0)and(not(np.array_equal(hurwitzmatrix[i+1],np.zeros((N/2)+1))))):
				hurwitzmatrix[2+i][j]=(hurwitzmatrix[i][j+1]*hurwitzmatrix[i+1][0]-hurwitzmatrix[i][0]*hurwitzmatrix[i+1][j+1])/(hurwitzmatrix[i+1][0])
			if((hurwitzmatrix[i+1][0]==0)and(not(np.array_equal(hurwitzmatrix[i+1],np.zeros((N/2)+1))))):
				hurwitzmatrix[i+1][0]=0.0000001
				hurwitzmatrix[2+i][j]=(hurwitzmatrix[i][j+1]*hurwitzmatrix[i+1][0]-hurwitzmatrix[i][0]*hurwitzmatrix[i+1][j+1])/(hurwitzmatrix[i+1][0])
		if(((np.array_equal(hurwitzmatrix[i+1],np.zeros((N/2)+1))))):
			hurwitzmatrix[i]=(hurwitzmatrix[i])/(np.gcd.reduce(hurwitzmatrix[i],dtype=int))
			for k in range((N/2)+1):
				hurwitzmatrix[i+1][k]=hurwitzmatrix[i][k]*(N-i-2*k)
			hurwitzmatrix[i+1]=hurwitzmatrix[i+1]/(np.gcd.reduce(hurwitzmatrix[i+1],dtype=int))
			for j in range(((N-1)/2)):
				hurwitzmatrix[2+i][j]=(hurwitzmatrix[i][j+1]*hurwitzmatrix[i+1][0]-hurwitzmatrix[i][0]*hurwitzmatrix[i+1][j+1])/(hurwitzmatrix[i+1][0])

RHSpoles=0
for i in range(N):
	if(hurwitzmatrix[i][0]/hurwitzmatrix[i+1][0]<0):
		RHSpoles+=1
		
	
				
print(hurwitzmatrix)
print("no of rhs poles:"+str(RHSpoles))
