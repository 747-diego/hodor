#!/usr/bin/python3
import requests
PayLoads = {"id":"725", "holdthedoor":"Submit"}
for index in range(1, 1024):
    p = requests.post("http://158.69.76.135/level0.php", data = PayLoads)
