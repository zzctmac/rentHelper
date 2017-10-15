# coding=utf-8
from bean.Manager import Manager
import json

m = Manager()

line1Name = '1号线'
line1Code = 1
line2Name = '2号线'
line2Code = 2

f = open("line1.json")
line1Text = f.read()
line1Json = json.loads(line1Text)
f.close()

m.add_line(line1Name, line1Code, line1Json)

f = open("line2.json")
line2Text = f.read()
line2Json = json.loads(line2Text)
f.close()
m.add_line(line2Name, line2Code, line2Json)


m.find_ways('人民广场'.decode("UTF-8"), '新闸路'.decode("UTF-8"))

