#!/usr/bin/python3
if __name__ == "__main__":
    import requests

    API_ENDPOINT = "http://158.69.76.135/level0.php"
    info = {"id":"725", "holdthedoor":"Submit+Query"}
    for index in range(0, 1020):
        payload = requests.post(url = API_ENDPOINT, data = info)
