
import time

k = []

start = time.time()

x=""

while x!="'":
	x=input()
	k.append(time.time()-start)

for i in k:
	print('time.sleep(%f)' % i)