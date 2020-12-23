# coding=utf-8

import os, sys, requests, json

from datetime import datetime, timedelta

def run(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    res = response
    return res


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours = ihour, minutes = iminute, seconds = isecond)
    
    uri = 'http://biblioteca.sas.gov.py:8080/handle/123456789/756'
    res = run(uri)
    data = res.text
    
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
