import requests
import json
import csv

# Get token
# NewRequest = {'Content-Type': 'application/x-www-form-urlencoded'}
# url = 'http://iot.acrel-eem.com/oversea/entry/home/getRelayToken.action'
# x = requests.post(url, json= NewRequest)
# print(x.status_code, x.reason)
# print(x.content)
# response = requests.get("http://iot.acrel-eem.com/oversea/entry/home/getRelayToken.action")
# output = (response.json())
# output1 = output["data"]
# print(output1)

# Get power usage
# NewRequest2 = {'Content-Type': 'application/x-www-form-urlencoded', 'token':'f25d1b92c5014f76a99c7adede88c4f3', 'mark': 'relay'}
# url2 = 'http://iot.acrel-eem.com/oversea/energy/getEnergyTable.action'
# x2 = requests.post(url2, json= NewRequest2)
# print(x2.status_code, x2.reason)
# print(x2.content)
# response = requests.get("http://iot.acrel-eem.com/oversea/energy/getEnergyTable.action")
# output2 = (response.json())
# output12 = output2["data"]
# print(output12)
# -----------
# get meter real time data
# NewRequest = {'Content-Type': 'application/x-www-form-urlencoded', 'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTYwMDkwNzF9.HuBFQFsS3FVN-rMPsgXHzk2E4bOqvZp6uZhs3eDd9Ng', 'mark':'relay'}
# url = 'http://iot.acrel-eem.com/oversea/dataMonitor/getMonitor.action'
# x = requests.post(url, json= NewRequest)
# print(x.status_code, x.reason)
# print(x.content)
# response = requests.get("http://iot.acrel-eem.com/oversea/dataMonitor/getMonitor.action")
# output = (response.json())
# output1 = output["data"]
# print(output1)
# ------------------------------------


url = 'http://iot.acrel-eem.com/oversea/dataMonitor/getMonitor.action'
body = {
    'SwicthId': '12109137160038',
    'MeterSN': '12109137160011'
}
# Adding empty header as parameters are being sent in payload
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTYwMDkwNzF9.HuBFQFsS3FVN-rMPsgXHzk2E4bOqvZp6uZhs3eDd9Ng', 'mark':'relay'}
r = requests.post(url, data=body, headers=headers)
# print(r.status_code)
output = (r.json())
output1 = output['data']
print(output1)
exc_head = []
exc_data = []
for key in output1:
    exc_head.append(key)
    exc_data.append(output1[key])

with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(exc_head)

    # write the data
    writer.writerow(exc_data)
# print(exc_head)
# print(exc_data)
    



