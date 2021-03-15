import json
import requests
import time
from collections import defaultdict

if __name__ == '__main__':
    with open('D:/scrapyProjects/GetProxy/proxy/匿名.json', encoding='utf-8') as f:
        target_str = f.read()
    json_list = target_str.split('\n')[:-1]
    print(json_list, len(json_list))
    s = requests.session()
    avariable_proxy = []
    for proxy_dict in json_list:
        proxies = {}
        proxy_dict = json.loads(proxy_dict)
        proxies[proxy_dict['scheme']] = proxy_dict['proxy']
        try:
            resp = s.get('http://icanhazip.com/', proxies=proxies, timeout=50)
            target_ip = resp.text.strip()
            src_ip = proxy_dict['proxy'].split("//")[1].split(":")[0]
            # print(src_ip)
            if target_ip == src_ip:
                print("代理可用",target_ip)
                with open('D:/scrapyProjects/GetProxy/avaiable_proxy/useable.txt','ab') as f:
                    f.write((json.dumps(proxy_dict)+"\n").encode('utf-8'))
            else:
                print('代理不可用',src_ip)
        except Exception as e:
            print('超时')
            continue
    print(avariable_proxy, len(avariable_proxy))
