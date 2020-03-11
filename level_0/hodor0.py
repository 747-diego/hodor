#!/usr/bin/python3
import requests
PayLoads = {'id':'823', 'holdthedoor':'Submit'}
for index in range(1, 1024):
    p = requests.post('http://158.69.76.135/hodor0.php', data = PayLoads)
