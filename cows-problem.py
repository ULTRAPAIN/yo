# Python code to implement the approach

# Function to check whether a distance is
# keeping all the cows in the barn

def ok(v,x,c):
	n=len(v)
	count=1
	d=v[0]
	for i in range(1,n):
		if(v[i]-d>=x):
			d=v[i]
			count=count+1
		else:
			continue
	if(count>=c):
		return True
	
	return False
	
# Function to find the maximum possible
# minimum distance between two cows
def aggressive_cows(v,n,k):
	ans=-1
	maxi=0
	for i in range(n):
		maxi=max(maxi,v[i])
	
	# Loop from 1 to max limit of the
	# barn length (here = 10^9)
	
	for i in range(1,maxi+1):
		if(ok(v,i,k)):
			ans=i
		else:
			break
	
	return ans
	
# Driver code
K=3
arr=[1,2,4,8,9]
N=len(arr)

# Function call
ans=aggressive_cows(arr,N,K)
print(ans)

# This code is contributed by Pushpesh Raj.
