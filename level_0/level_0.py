#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup

    for index in range(1024):
        payload = requests.post("http://158.69.76.135/level0.php", data={"id":725, "holdthedoor":"Submit"})
