import random
import sys

maxval = 64

activeFile = sys.argv[1]
inactiveFile = sys.argv[2]
testFile = sys.argv[3]

with open('sig_ca.txt','r') as f:
	content_ca = f.readlines()

da = dict()

dim_ca = min(len(content_ca),maxval)
content_ca = content_ca[0:dim_ca]

for i in xrange(0,len(content_ca)):
	line = content_ca[i]
	parents = line.strip().split()
	for x in parents:
		try:
			da[int(x)].append(i)
		except Exception as e:
			da[int(x)] = [i]




with open('sig_ci.txt','r') as f:
	content_ci = f.readlines()

di = dict()

dim_ci = min(len(content_ci),maxval)
content_ci = content_ci[0:dim_ci]

for i in xrange(0,len(content_ci)):
	line = content_ci[i]
	parents = line.strip().split()
	for x in parents:
		try:
			di[int(x)].append(i)
		except Exception as e:
			di[int(x)] = [i]



with open(activeFile,'r') as f:
	active_g = f.readlines()

with open(inactiveFile,'r') as f:
	inactive_g = f.readlines()

minSamples = min( len(active_g), len(inactive_g) )

if len(active_g) < len(inactive_g):
	inactive_g = random.sample(inactive_g, minSamples)
else:
	active_g = random.sample(active_g, minSamples)


f = open('train.txt','w')

for x in active_g:
	f.write('1')

	try:
		ones = set(da[int(x)])
	except Exception as e:
		ones = set([])

	for i in xrange(0,dim_ca):
		if i in ones:
			f.write(' '+str(i)+':1')
		else:
			f.write(' '+str(i)+':0')

		# except Exception as e:
		# 	f.write(' '+str(i)+':0')



	try:
		ones = set(di[int(x)])
	except Exception as e:
		ones = set([])

	for i in xrange(0,dim_ci):
		# try:
		if i in ones:
			f.write(' '+str(i+dim_ca)+':1')
		else:
			f.write(' '+str(i+dim_ca)+':0')
				
		# except Exception as e:
		# 	f.write(' '+str(i+dim_ca)+':0')


	f.write('\n')


for x in inactive_g:
	f.write('-1')

	try:
		ones = set(da[int(x)])
	except Exception as e:
		ones = set([])

	for i in xrange(0,dim_ca):
		# try:
		if i in ones:
			f.write(' '+str(i)+':1')
		else:
			f.write(' '+str(i)+':0')

		# except Exception as e:
		# 	f.write(' '+str(i)+':0')

	try:
		ones = set(di[int(x)])
	except Exception as e:
		ones = set([])

	for i in xrange(0,dim_ci):
		# try:
		if i in ones:
			f.write(' '+str(i+dim_ca)+':1')
		else:
			f.write(' '+str(i+dim_ca)+':0')
				
		# except Exception as e:
		# 	f.write(' '+str(i+dim_ca)+':0')

	f.write('\n')

f.close()



# Testing

with open(testFile,'r') as f:
	content = f.readlines()

num_g = 0
for x in content:
	if x[0] == '#':
		num_g += 1


with open('sig_ca_test.txt','r') as f:
	content_ca = f.readlines()

da = dict()

dim_ca = min(len(content_ca),maxval)
content_ca = content_ca[0:dim_ca]

for i in xrange(0,len(content_ca)):
	line = content_ca[i]
	parents = line.strip().split()
	for x in parents:
		try:
			da[int(x)].append(i)
		except Exception as e:
			da[int(x)] = [i]




with open('sig_ci_test.txt','r') as f:
	content_ci = f.readlines()

di = dict()

dim_ci = min(len(content_ci),maxval)
content_ci = content_ci[0:dim_ci]

for i in xrange(0,len(content_ci)):
	line = content_ci[i]
	parents = line.strip().split()
	for x in parents:
		try:
			di[int(x)].append(i)
		except Exception as e:
			di[int(x)] = [i]


f = open('test.txt','w')

for x in xrange(0,num_g):
	
	try:
		ones = set(da[int(x)])
	except Exception as e:
		ones = set([])

	for i in xrange(0,dim_ca):
		if i in ones:
			f.write(str(i)+':1 ')
		else:
			f.write(str(i)+':0 ')

	try:
		ones = set(di[int(x)])
	except Exception as e:
		ones = set([])

	for i in xrange(0,dim_ci):
		if i in ones:
			f.write(str(i+dim_ca)+':1 ')
		else:
			f.write(str(i+dim_ca)+':0 ')
				
	f.write('\n')

f.close()




