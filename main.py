# This is where the main file will be. It will take care of the entire conversion.
# Ideally, another file can be associated with exporting the image but we can worry about it later

import requests

width = 300
height = 300

params={"cht": "qr",
        "chs": f"{width}x{height}",
        "chl": "https://github.com/KabrG",
        "choe": "UTF-8"}
r = requests.get(url='https://chart.googleapis.com/chart?', params=params)
r.raise_for_status()

with open("qr.png", "wb") as qr:
    qr.write(r.content)