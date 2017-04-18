import time
from datetime import datetime as d

localhost = "127.0.0.1"
websitelist = ["www.facebook.com","www.twitter.com","facebook.com","twitter.com"]
host_path = "/etc/hosts"
host_temp = "hosts"

while True:
    if d(d.now().year,d.now().month,d.now().day,9) < d.now() < d(d.now().year,d.now().month, d.now().day,18):
        print("Working time..")
        with open(host_temp,'r+') as file:
            content = file.read()
            for website in websitelist:
                if website in content:
                    pass
                else:
                    file.write(localhost + " " + website + "\n")
    else:
        print("Personal time..")
        with open(host_temp,'r+') as file:
            contentlist = file.readlines()
            file.seek(0)
            for line in contentlist:
                if all(website not in line for website in websitelist):
                    file.write(line)
            file.truncate()
    time.sleep(5)
