import requests
import json
import hashlib
requests.packages.urllib3.disable_warnings()

def get_token():
    url = "https://www.ggcx.com/api/SafeVerify/GetNVCCode"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'application/json, text/plain, */*',
        'Source': 'web',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'Bearer NylLlaC+Hezul5bILK+12VZKXSpDdtbBXprCv',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.ggcx.com/main/record',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close'
        }

    req = requests.get(url, headers=headers, verify=False)
    return_data = json.loads(req.content.decode())
    if return_data['StateCode'] == 1:
        token = return_data['Result']
        return  hashlib.md5((token + 'NylLlaC+Hezul5bILK+12VZKXSpDdtbBXprCv').encode()).hexdigest()
    else:
        print('return error!')

def query(domain):
    token = get_token()
    url = "https://www.ggcx.com/api/Beian"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Source': 'web',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'Bearer NylLlaC+Hezul5bILK+12VZKXSpDdtbBXprCv',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.ggcx.com/main/record',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close'
        }
    data = {
        'domain': domain,
        'type': 0,
        'verifyCode': token
    }
    req = requests.post(url, headers=headers, data=data, verify=False)
    result = json.loads(req.content.decode())
    # {"StateCode":1,"Reason":"成功","Result":{"Owner":"","CompanyName":"北京百度网讯科技有限公司","CompanyType":"企业","SiteLicense":"京ICP证030173号-1","SiteName":"百度","MainPage":"www.baidu.com","VerifyTime":"2023-01-10 09:43:35","UpdateTime":"2023-03-27 10:17:17"}}
    if result['StateCode'] == 1:
        print(domain + ': ' + result['Result']['CompanyName'])
        return result['Result']['CompanyName']
    else:
        return domain + 'error:' + req.content.decode()


if __name__ == '__main__':
    targets = []

    with open('targets.txt', 'r', encoding='utf-8') as f:
        targets = f.readlines()

    # main(targets)

    results = []
    company_list = []
    errors = []
    count = 0           # 访问接口指定时间内到达500次会暂时无法请求
    for i in targets:
        if count >= 499:
            print("request 500! now at ", i)
            break
            count = 0
        try:
            com = query(i.rstrip('\n'))
            if 'error:' not in com:
                # print(com)
                results.append(i.rstrip('\n') + ': \t\t' + com + '\n\n')
                company_list.append(com.rstrip() + '\n')
        except Exception as e:
            print('error: ', e)
            errors.append(i)
            continue
        count += 1
    with open('results.txt', 'w', encoding='utf-8') as f:
        f.writelines(results)
    with open('company_list.txt', 'w', encoding='utf-8') as f:
        f.writelines(company_list)
    with open('errors.txt', 'w', encoding='utf-8') as f:
        f.writelines(errors)

