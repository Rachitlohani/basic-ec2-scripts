from pprint import pprint
from boto import ec2


i_count=[]

ec2conn = ec2.connection.EC2Connection()
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
	i_count.append(i.instance_type)
	

instance_type = set(i_count)

for type in instance_type:
	print ("%s , %s " %(type  , i_count.count(type)) )
