# This is where the main file will be. It will take care of the entire conversion.
# Ideally, another file can be associated with exporting the image but we can worry about it later

import requests

width = 1000
height = 1000

params={'cht': 'qr',
        'chs': f'{width}x{height}',
        'chl': ''}
r = requests.get(url='https://chart.googleapis.com/chart?', params=params)

print(r)