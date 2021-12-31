import requests
import json
import csv
url = 'http://iot.acrel-eem.com/oversea/dataMonitor/getMonitor.action'
body = {
    'SwicthId': '12109137160038',
    'MeterSN': '12109137160011'
}
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTYwMDkwNzF9.HuBFQFsS3FVN-rMPsgXHzk2E4bOqvZp6uZhs3eDd9Ng', 'mark':'relay'}
r = requests.post(url, data=body, headers=headers)
# print(r.status_code)
output = (r.json())
output1 = output['data']
# print(output1)
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
    



