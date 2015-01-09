import argparse
import boto.ec2
from pprint import pprint 
access_key = 'XXXXXXX'
secret_key = 'XxXXXXXXXx/husg7uC'
 
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = '/husg7uC'




def get_ec2_instances(reg):
#    ec2_conn = boto.ec2.connect_to_region(region,
#                aws_access_key_id=access_key,
#                aws_secret_access_key=secret_key)
#    reservations = ec2_conn.get_all_reservations()
#    for reservation in reservations:    
#        print region+':',reservation.instances

 ec2conn=boto.ec2.connect_to_region(reg,aws_access_key_id='XXXXXXXXXX',aws_secret_access_key='XXXXX/XXXXXX')
 #ec2conn = boto.ec2.connection.EC2Connection(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

 reservations = ec2conn.get_all_instances()
 instances = [i for r in reservations for i in r.instances]
 for i in instances:
    pprint(i.__dict__)
    break # remove this to list all instances 
 


def main():
    regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
                'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    #parser = argparse.ArgumentParser()
    #parser.add_argument('access_key', help='Access Key');
    #parser.add_argument('secret_key', help='Secret Key');
    #args = parser.parse_args()
    global access_key
    global secret_key
    #access_key = args.access_key
    #secret_key = args.secret_key
    
    for reg in regions: get_ec2_instances(reg)
 
if  __name__ =='__main__':main()
