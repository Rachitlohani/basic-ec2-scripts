import requests
import json
import datetime, time

NEWRELIC_API_KEY = "newrelickey"
HOURS_TO_KEEP = 0

HEADERS = {"X-Api-Key": NEWRELIC_API_KEY}


def get_servers():
    SERVERS_URL = "https://api.newrelic.com/v2/servers.json"
    SERVERS_KEY = "servers"

    servers = []
    page = 1

    while True:
        data = {"page":page}
        response = requests.get(SERVERS_URL, headers=HEADERS, data=data)
        if response.status_code != 200:
            raise Exception("could not get servers - status code is not 200")
        json_response = json.loads(response.text)
        if json_response.has_key(SERVERS_KEY)==False:
            raise Exception("could not get servers - bad json response")
        servers_in_this_page = json_response[SERVERS_KEY]
        if len(servers_in_this_page) == 0:
            return servers
        servers += servers_in_this_page
        page+=1

def get_servers_to_delete(servers, last_reported_at_time):
    servers_to_delete = []
    for server in servers:
        server_last_reported_at_time_struct = time.strptime(server["last_reported_at"], "%Y-%m-%dT%H:%M:%S+00:00")
        server_last_reported_at_time_struct_datetime = datetime.datetime.fromtimestamp(time.mktime(server_last_reported_at_time_struct))
        if server_last_reported_at_time_struct_datetime < last_reported_at_time and server["reporting"]==False:
            servers_to_delete.append(server)
    return servers_to_delete

def delete_servers(servers_to_delete):
    DELETE_SERVERS_URL = "https://api.newrelic.com/v2/servers/%s.json"
    x=0
    for server_to_delete in servers_to_delete:
        server_id_to_delete = server_to_delete["id"]
        print "about to delete %(server_to_delete)s" % vars()
        response = requests.delete(DELETE_SERVERS_URL % server_id_to_delete, headers=HEADERS)
        if response.status_code != 200:
	   print "could not delete %(server_to_delete)s" % vars()
	   pass

servers = get_servers()
print "there are %s servers" % len(servers)
from_time = datetime.datetime.today() - datetime.timedelta(hours=HOURS_TO_KEEP)
servers_to_delete = get_servers_to_delete(servers, from_time)
#print servers_to_delete
#print "we are planning to delete %s servers" % len(servers_to_delete)
#for server in servers_to_delete:
#	print server["name"], ",", server["last_reported_at"]

if len(servers_to_delete) == 0:
    print "all servers are reporting. nothing to delete"
delete_servers(servers_to_delete)
