#!/usr/local/bin/python

######################################################
## Hetzner Cloud Worker for Plex Remote Transoder  ###
##                  2018-09-16                     ###
##             markus(AT)omg-network.de            ###
######################################################

import os
import datetime
from hetznercloud import HetznerCloudClientConfiguration, HetznerCloudClient

configuration = HetznerCloudClientConfiguration().with_api_key("APIKEY").with_api_version(1)
client = HetznerCloudClient(configuration)

def getLoad():
    load = os.getloadavg()[0]
    return load

def delete_all_servers():
    servers = list(client.servers().get_all())
    for server in servers:
        server.delete()

def createServer():
    server_a, create_action = client.servers().create(name=genServerName(),
    server_type="cx41",
    image="ubuntu-16.04",
    datacenter="fsn1-dc8",
    start_after_create=True,
    user_data='''#cloud-config
	packages:
	 - screen
	 - git
     - htop
    ''')
    try:
        server_a.wait_until_status_is("running")
    except Exception:
        server_a.delete()
        createServer()
    return server_a.root_password + ' ' + server_a.public_net_ipv4

def genServerName():
    date = datetime.datetime.now().strftime("%y-%m-%d--%H-%M")
    return "Plex-Transcode-Worker-"+ date

print createServer()
