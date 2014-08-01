import csv
from boto import ec2
import pprint
ec2conn = ec2.connection.EC2Connection()
with open('test.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    reservations = ec2conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
      #print(i.__dict__)
      #break;
        row = []
        if 'Application' in i.tags:
        # print "%s (%s) [%s]" % (i.tags['Application'], i.public_dns_name, i.tags['Name'])
         row.append( i.tags['Application'] )
         row.append( i.public_dns_name)
         row.append(i.state)
        #data = ['%i.tags['Application'], %i.public_dns_name, %i.state)'.split(",") ]
         a.writerow(row)
         print row;
         #break # remove this to list all instances
