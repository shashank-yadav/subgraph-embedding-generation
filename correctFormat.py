import sys

file = sys.argv[1]

with open(file,'r') as f:
	content = f.readlines()


starts = []
for i in xrange(0,len(content)):
	line = content[i]
	if line[0]=='#':
		starts.append(i)

# toRemove = False

# if starts[-1] == len(content)-1:
# 	toRemove = True
# else:
# 	vCount = int(content[starts[-1]+1].strip())
# 	if len(content) < starts[-1]+vCount+1:
# 	 	toRemove = True
# 	else:
# 		eCount = int(content[starts[-1] + vCount + 2].strip())
# 		if len(content) < starts[-1]+vCount+1:
# 	 		toRemove = True


f = open(file+'.corrected','w')
for i in xrange(0,starts[-1]):
	f.write(content[i])

f.close()