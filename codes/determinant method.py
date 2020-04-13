import numpy as np
def Stability(k):
		p = np.poly1d([1,3,3,1,k])    # enter the coefficients of characteristic polynomial
		c = p.c
		r = np.zeros((len(c)-1,len(c)-1))	 
		try:
			for i in range(len(r[0])):
				r[0][i] = c[2*i+1]       #filling the first row
		except IndexError:
			print("calculating...")
		try:
			for i in range(len(r[1])):
				 r[1][i] = c[2*i]    #filling the second row
		except IndexError:
			print("...")
		for j in range(2,len(r)):
			if(j%2==0):
				try:
					for i in range(len(r[i])):
						r[j][i]=r[0][i-j/2]
				except IndexError:
					print("...")
			else:
				try:
					for i in range(len(r[i])):
						r[j][i]=r[1][i-int(j/2)]
				except IndexError:
					print("...")
		print("Routh matrix=%s"%r)
		DET=np.zeros(len(c)-1)
		for i in range(len(c)-1):
			m=r[0:i+1,0:i+1]
			print("DET(%d)=%s"%(i,m))
			DET[i]=np.linalg.det(m)
			print("DET(%d)=%s"%(i,DET[i]))
		if(min(DET)>0):
			print("system is stable")
		else:
			print("system is unstable")	
k=[0.5,3]			
for i in range(2):
	print("k=%d"%k[i])
	Stability(k[i])      

		
			
			

			        				
		 	
				
		
			




			
