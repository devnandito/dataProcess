# coding=utf-8

import os, sys, requests, json

from datetime import datetime, timedelta

def run(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    # res = response.txt
    res = response
    return res


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    name_file = input('Enter name file:')

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours = ihour, minutes = iminute, seconds = isecond)
    
    uri = 'https://www.hacienda.gov.py/portalspir/data_lam.json?_search=false&nd=1608124197055&rows=10&page=1&sidx=&sord=asc'
    # uri = 'https://www.hacienda.gov.py/portalspir/data_lam.json'
    res = run(uri)
    data = res.text
    # data = res.json()
    # print(data)
    # list1 = list()
    # for row in data:
    #     list1.append(row)
    
    # for row in range(len(list1)):
    #     if list1[row] == 0:
    #         print(list1[row])
    # jsonResponse = res.json()
    # list1 = []
    # for key, value in jsonResponse.items():
    #     data = '{}:{}'.format(key, value)
    #     list1.append(data)
    
    f = open(name_file, 'w')
    f.write(data)
    f.close()

    # ofile = os.path.join(BASE_DIR, 'set/results/'+name_file)
    # with open(ofile, 'w+') as outfile:
    #     json.dump(list1, outfile, indent=4)
    
    now = datetime.now()
    ohour = now.hour
    ominute = now.minute
    osecond = now.second
    end = timedelta(hours=ohour, minutes=ominute, seconds=osecond)
    timerun = end - start
    message = '''
            Time start: {} \n
            Runtime: {} \n
            Time finish: {}
            '''.format(start, timerun, end)
    print(message)
