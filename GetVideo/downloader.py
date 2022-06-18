# https://tartuulikool-my.sharepoint.com/:v:/g/personal/karlmv_ut_ee/EZ6j72i7Z_pDlzb1EGisfysBxLo0CQLcv_alYyCQB5Q8Rw?e=6OSSoT
import requests

site_url = 'https://tartuulikool-my.sharepoint.com/:v:/g/personal/karlmv_ut_ee/Eb_w5Gj4N0lIv3sIgmalcjQBWjktodUT3JRiO3GWkRAqCw?e=YfASkt'


r = requests.get(site_url)
with open('test.html', 'w') as f:
    f.write(r.text)


# URL = site_url + '&download=1'

# resp = requests.get(URL) # making requests to server

# with open('download.mp4', "wb") as f: # opening a file handler to create new file 
#     f.write(resp.content) 

