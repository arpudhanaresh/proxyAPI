import time
import getproxy
import json,requests,urllib.request
from traceback import print_exc
from ast import literal_eval
import pprint

def push_to_git():
    #Import dependencies
    from subprocess import call
    #Commit Message
    commit_message = "Updating json files"
    #Stage the file
    call('git add .', shell = True)
    # Add your commit
    call('git commit -m "'+ commit_message +'"', shell = True)
    #Push the new or update files
    call('git push origin master', shell = True)

def get_proxy():
    proxies=[]
    proxy= ["103.69.45.68:61011", "103.74.220.47:44073", "43.224.8.114:50333", "14.142.145.156:80", "103.206.130.118:8080"]
    i,j=0,0
    for a in range(len(proxy)):
        for p in proxy:
            user_agent = {'User-agent': 'Mozilla/5.0'}
            url = 'http://pubproxy.com/api/proxy?country=IN&limit=20&https=True&user_agent=true'
            while(j!=1):
                try:
                    j=0
                    resp = requests.get(url=url,headers=user_agent,proxies={"http": p, "https": p})
                    data = resp.json()
                    time.sleep(2.1)
                    for proxy in data['data']:
                        proxies.append(proxy['ipPort'])
                    print('Length of Proxy till '+str(i)+'th attempt is ',len(proxies))
                except Exception as e:
                    print('Skipped proxy '+str(p)+" "+str(i)+' time')
                    j=1
                finally:
                    i=i+1
    try:
        print("Entered Spy proxy")
        proxies=proxies+spy_proxy()
    except Exception :
        pass

    try:
        proxies=proxies+fate_proxy()
    except Exception:
        pass

    return proxies

def fate_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    np_list=[]
    for i in p_list:
        if i['country']=='IN':
            np_list.append(i)
    #print(len(np_list))
    proxy=[]
    for i in np_list:
        proxy.append((str(i['host'])+':'+str(i['port'])))
    return(proxy)

def spy_proxy():
    resp=requests.get('http://spys.me/proxy.txt')
    data=((resp.text).split("Google_passed(+)")[1]).split('\r')[0]
    data=data.split('\n')
    l=[]
    for i in data:
        if 'IN' in i:
            i=i.split(' IN')[0]
            l.append(i)
    return l


proxy_json={'data':get_proxy()}
import json
with open('proxy.json', 'w') as outfile:
    json.dump(proxy_json, outfile)
push_to_git()
