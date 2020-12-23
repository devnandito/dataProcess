# coding=utf-8

'''# -*- coding: utf-8 -*-  #!/usr/lib/python3/'''
import os, sys
import requests
import csv
import json
import smtplib
#import time
from datetime import datetime, timedelta

from progressbar import ProgressBar

pbar = ProgressBar()

def run(url, init, finish):
    list_uri = []
    for item in pbar(range(init,finish)):
    # for item in range(init,finish):
        ci = str(item)
        uri = url + ci
        response = requests.get(uri)
        response.raise_for_status()
        resp = ci + ':' + response.text
        list_uri.append(resp)
    return list_uri


if __name__ == '__main__':

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours = ihour, minutes = iminute, seconds = isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(BASE_DIR, 'dataSnpp/var8.txt')

    f = open(filename, "r")
    f1 = f.readlines()
    list1 = []
    for x in f1:
        list1.append(x)

    init = int(list1[0])
    finish = int(list1[0])+int(50)
    count = int(list1[1])
    ext=".csv"
    tfile = "%s%s%s"%(list1[2].rstrip('\n'),list1[1].rstrip('\n'),ext)
    nfile = os.path.join(BASE_DIR, 'dataSnpp/res/8/'+tfile)
    f.close()
#    resp = run('https://regobpat.mtess.gov.py/identidad_snpp/alumno/output/sii_ci_local.php?tipod=1&&ci=', init, finish)
    resp = run('https://identidad.mtess.gov.py/alumno/sii_ci_local.php?tipod=1&&ci=', init, finish)
    with open(nfile, 'w+') as f:
       writer = csv.writer(f)
       writer.writerow(('cedula:name:lastname:birthday:code:sex:type:age:nationality:var1:var2',))
       for i in resp:
           writer.writerow((i,))

    init = finish
    #finish = init + 50
    count += 1
    f = open(filename, "w")
    f.write(str(init)+"\n")
    #f.write(str(finish)+"\n")
    f.write(str(count)+"\n")
    f.write(str(list1[2]))
    f.close()

    now = datetime.now()
    ohour = now.hour
    ominute = now.minute
    osecond = now.second
    end = timedelta(hours = ohour, minutes = ominute, seconds = osecond)
    timerun = end - start

    message = "Se genero correctamente el archivo %s \n Hora de Inicio: %s \n Fecha de Fin: %s \n Tiempo ejecución: %s"        %(tfile, start, end, timerun)

    ext1 = ".txt"
    logFile = "%s%s%s"%(list1[2].rstrip('\n'),list1[1].rstrip('\n'),ext1)
    filename1 = os.path.join(BASE_DIR, 'dataSnpp/log/8/'+logFile)
    f = open(filename1, "w")
    f.write(str(message))
    f.close()    