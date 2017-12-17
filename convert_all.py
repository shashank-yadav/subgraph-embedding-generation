import sys
import random

input_file = sys.argv[1]
output_file = sys.argv[2]
ca = sys.argv[3]
ci = sys.argv[4]
test_file = sys.argv[5]

test_formatted = 'data/test.txt'
graphs_formatted = 'data/aids.txt'
ca_formatted = 'data/ca.txt'
ci_formatted = 'data/ci.txt'
init_test = 'test.txt'
init_train = 'train.txt'
MAX_CA = 20000.0
MAX_CI = 20000.0

with open(input_file) as f:
	content = f.readlines()


content = [x.strip() for x in content] 

f_ = open(graphs_formatted,'w')
f = open(output_file,'w')

i = 0
nums = 0
graph_map = {}
v_dict = {}
e_dict = {}

while i < len(content):

	f.write( 't # '+str(nums)+'\n' )
	f_.write( '#'+str(nums)+'\n' )
	graph_map[int(content[i].split('#')[1])] = nums
	i += 1
 	
	vertices = int(content[i])
	f_.write(str(vertices)+'\n')
	
	for j in xrange(1,vertices+1):
		key = content[i+j]
		if key not in v_dict:
			v_dict[key] = len(v_dict)
		f.write('v '+str(j-1)+' '+str(v_dict[key])+'\n')
		f_.write(str(v_dict[key])+'\n')
 	
	i = i+vertices+1

	edges = int(content[i])
	f_.write(str(edges)+'\n')
	
	for j in xrange(1,edges+1):
		s, d, key = content[i+j].split(' ')
		if key not in e_dict:
			e_dict[key] = len(e_dict) + len(v_dict)
		f.write('e '+s+' '+d+' '+str(e_dict[key])+'\n')
		f_.write(s+' '+d+' '+str(e_dict[key])+'\n')

	i = i+edges+1

	nums += 1

f.close()
f_.close()

f = open(init_train,'w')

for x in range(100):
	if(random.random() < 0.5):
		f.write('1 0:1\n')
	else:
		f.write('-1 0:0\n')

f.close()

print "Number of graphs:", nums

with open(test_file) as f:
	content = f.readlines()

content = [x.strip() for x in content] 

f_ = open(test_formatted,'w')

i = 0
nums = 0

while i < len(content):

	f_.write( '#'+str(nums)+'\n' )
	i += 1
 	
	vertices = int(content[i])
	f_.write(str(vertices)+'\n')
	
	for j in xrange(1,vertices+1):
		key = content[i+j]
		if key not in v_dict:
			v_dict[key] = len(v_dict)
		f_.write(str(v_dict[key])+'\n')
 	
	i = i+vertices+1

	edges = int(content[i])
	f_.write(str(edges)+'\n')
	
	for j in xrange(1,edges+1):
		s, d, key = content[i+j].split(' ')
		if key not in e_dict:
			e_dict[key] = len(e_dict) + len(v_dict)
		f_.write(s+' '+d+' '+str(e_dict[key])+'\n')

	i = i+edges+1

	nums += 1

f_.close()


f = open(init_test,'w')

for x in range(nums):
	if(random.random() < 0.5):
		f.write('0:1\n')
	else:
		f.write('0:0\n')

f.close()


print "Number of test_graphs:", nums


d = {}

with open(ci) as f:
	content0 = f.readlines()

content0 = [int(x.strip()) for x in content0]

with open(ca) as f:
	content1 = f.readlines()

content1 = [int(x.strip()) for x in content1] 

f = open('labels.txt','w')
f_ca = open(ca_formatted,'w')
f_ci = open(ci_formatted,'w')

for x in content0:
	# d[graph_map[x]] = 0
	try:
		d[graph_map[x]] = 0
		if(random.random() < MAX_CI/len(content0)):
			f_ci.write(str(graph_map[x])+'\n')
	except Exception as e:
		pass

for x in content1:
	# d[graph_map[x]] = 0
	try:
		d[graph_map[x]] = 1
		if(random.random() < MAX_CI/len(content1)):
			f_ca.write(str(graph_map[x])+'\n')
	except Exception as e:
		pass

print len(graph_map)
print len(content0)+len(content1)
print len(d)

for x in xrange(0,len(graph_map)):
	try:
		f.write(str(d[x])+'\n')
	except Exception as e:
		f.write(str(0)+'\n')

f.close()
f_ca.close()
f_ci.close()
