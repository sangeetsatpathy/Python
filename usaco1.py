k= int(input())
n=int(input())
x=1
linenumber=1
while(linenumber<=k):
	while(x<=n):
		print(x)
		x=x+1
	if(x==n):
		x=1
	linenumber=linenumber+1
