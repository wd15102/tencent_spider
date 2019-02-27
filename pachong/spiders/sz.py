import requests
import json
url = 'https://szapp.singlewindow.cn/decserver/sw/dec/common/getMerchElement'
payload = {"codeTs":"0103912010","ieFlag":"I"}
headers = {'content-type': 'application/json','Cookie':'route1plat=45a6b96a894352987f8fea7dd5d422f0; JSESSIONID=91e384df-988f-495c-8cd2-108ec33fd7f8','Referer':'https://szapp.singlewindow.cn/decserver/sw/dec/cusCiqZhImport?cusIEFlag=I&dclTrnRelFlag=0&cusRmftFcbFlag=3&ngBasePath=https%3A%2F%2Fszapp.singlewindow.cn%3A443%2Fdecserver%2F'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.text)