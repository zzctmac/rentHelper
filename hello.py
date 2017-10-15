import json
import httplib

url = "http://service.shmetro.com/i/fa?metoh=getAllLineList"


conn = httplib.HTTPConnection("service.shmetro.com")

conn.request("POST", url)

resp = conn.getresponse()

res = resp.read()


allLineFile = open("alline.json", "w+")

allLineFile.write(res)
allLineFile.close()

res = json.loads(res)

lineUrl = "http://service.shmetro.com/i/fa?metoh=getLineList&line="

for i, v in enumerate(res):
    print v['line'], v['lineCode']
    lconn = httplib.HTTPConnection("service.shmetro.com")

    lconn.request("POST", lineUrl + v['lineCode'])

    lineFile = open("line" + v['lineCode'] + ".json", "w+")

    lresp = lconn.getresponse()

    lres = lresp.read()

    lineFile.write(lres)

    lineFile.close()

    lres = json.loads(lres)
    for li, lv in enumerate(lres):
        print " ", lv['station']

