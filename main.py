from setup import URLS, HEADERS, D
import os
import sys

count = 0
for url in URLS:
    proxy = "10.170.6.5:8080"
    # res = requests.get(url, data=D[count],headers=HEADERS )
    cmd = "curl -s -X PATCH " + "-x " + proxy + " -H " + HEADERS[0] + " -H " + "'User-Agent:'" + " " + "-H " + HEADERS[1]\
          + " -k " + url + sys.argv[1] + " -d " + D[count]
    print(cmd)
    count += 1
    t = os.popen(cmd, 'r', 1)
    t.close()
