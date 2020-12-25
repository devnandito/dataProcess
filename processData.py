import os, sys, re, csv, json, pandas as pd
from datetime import datetime, timedelta

def menu():
    print('Select options')
    print('\t1 Read data a save without header to csv')
    print('\t2 Read data a save to json')
    print('\t3 Clean quotes and save to json')
    print('\t4 Verifycate quotes')
    print('\t5 Clean screen')
    print('\t6 Exit')

def ext(data):
    ext = data.split('.')
    ext = ext[1]
    return ext

def getLog():
    file_log = os.path.join(BASE_DIR, 'dataProcess/vars/processData.txt')
    f = open(file_log, "r")
    f1 = f.readlines()
    list_log = []
    for x in f1:
        list_log.append(x)
    f.close()
    return list_log

def saveLog(count, name, start, end, time_run, file_input):
    ext1 = '.txt'
    logFile = '%s%s%s'%(name.rstrip('\n'),count.rstrip('\n'),ext1)
    file_log = os.path.join(BASE_DIR, 'dataProcess/logs/'+logFile)
    f = open(file_log, 'w')
    f.write(printMessage(start, end, time_run, file_input))
    f.close()

def saveVar(count, name):
    file_log = os.path.join(BASE_DIR, 'dataProcess/vars/processData.txt')
    f = open(file_log, 'w')
    f.write(str(count)+'\n')
    f.write(str(name))
    f.close()

def timeNow(now):
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    now = timedelta(hours=ihour, minutes=iminute, seconds=isecond)
    return now

def printMessage(start, end, runtime, file_output):
    message = 'Time start: {}, Time end: {}, Runtime: {}, File: {}'.format(start, end, time_run, file_output)
    return message

def fileInput():
    file_input = input('Enter file:')
    return file_input

def fileOutput():
    file_output = input('Enter file output name:')
    return file_output

def printDataFrame(data_frame):
    cols = data_frame.columns.ravel()
    print(data_frame)
    print(cols)

def readDataFrame(file_input, ext):
    if ext == 'csv' or ext == 'txt':
        data_frame = pd.read_csv(file_input)
    elif ext == 'xlsx':
        data_frame = pd.read_excel(file_input)
    elif ext == 'json':
        data_frame = pd.read_json(file_input)
    return data_frame

def writeJson(handle):
    data_tmp = list()
    data_json = list()
    for line in handle:
        xsearch = (r'\"(.*)\"')
        stuff = re.search(xsearch, line)
        if stuff:
            data = re.findall(xsearch, line)
            print(data[0])
            data_tmp.append(data[0])
        else:
            data_tmp.append(line)
    for row in data_tmp:
        stuff = row.split(':')
        if len(stuff) == 2:
            print(stuff[0], stuff[1])
        elif len(stuff) == 3:
            print(stuff[0], stuff[1], stuff[2])
        else:
            data_json.append({
                'ci': stuff[0],
                'first_name': stuff[1],
                'last_name': stuff[2],
                'birthday': stuff[3],
                'code1': stuff[4],
                'sex': stuff[5],
                'type': stuff[6],
                'age': stuff[7],
                'nationality': stuff[8],
                'code2': stuff[9],
                'code3': stuff[10].rstrip(),
            })
    return data_json

def saveJson(ofile):
    with open(ofile, 'w+') as outfile:
        json.dump(data_json, outfile, indent=4, ensure_ascii=False)

def pathFile(file_output):
    output = os.path.join(BASE_DIR, 'dataProcess/results/'+file_output)
    return output

def verifQuotes(handle):
    for line in handle:
        xsearch = (r'\"(.*)\"')
        stuff = re.search(xsearch, line)
        if stuff:
            data = re.findall(xsearch, line)
            print(data[0])

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    while True:
        menu()
        options = input('Enter options:')
        options = options.lower()
        if options == '1':
            start = timeNow(datetime.now())
            try:
                file_input = fileInput()
            except:
                print('File not found')
                continue
            file_output = fileOutput()
            res = ext(file_input)
            if res == 'csv' or res == 'txt':
                data_frame = readDataFrame(file_input, res)
                printDataFrame(data_frame)
                ofile = pathFile(file_output)
                data_frame.to_csv(ofile, index=False, header=False)
            elif res == 'xlsx':
                data_frame = readDataFrame(file_input, res)
                printDataFrame(data_frame)
            elif res == 'json':
                data_frame = readDataFrame(file_input, res)
                printDataFrame(data_frame)
            end = timeNow(datetime.now())
            time_run = end - start
            print(printMessage(start, end, time_run, file_output))
            logs = getLog()
            count = int(logs[0])
            name = logs[1]
            saveLog(str(count), name, start, end, time_run, file_input)
            count +=1
            saveVar(count, name)
        
        elif options == '2':
            start = timeNow(datetime.now())
            try:
                file_input = fileInput()
            except:
                print('File not found')
                continue
            res = ext(file_input)
            data_frame = readDataFrame(file_input, res)
            printDataFrame(data_frame)
            end = timeNow(datetime.now())
            time_run = end - start
            print(printMessage(start, end, time_run, file_input))
            logs = getLog()
            count = int(logs[0])
            name = logs[1]
            saveLog(str(count), name, start, end, time_run, file_input)
            count +=1
            saveVar(count, name)
        elif options == '3':
            start = timeNow(datetime.now())
            try:
                file_input = fileInput()
                handle = open(file_input)
            except:
                print('File not found')
                continue
            file_output = fileOutput()
            data_json = writeJson(handle)
            ofile = pathFile(file_output)
            saveJson(ofile)
            end = timeNow(datetime.now())
            time_run = end - start
            print(printMessage(start, end, time_run, file_output))
            logs = getLog()
            count = int(logs[0])
            name = logs[1]
            saveLog(str(count), name, start, end, time_run, file_input)
            count +=1
            saveVar(count, name)
        elif options == '4':
            start = timeNow(datetime.now())
            try:
                file_input = fileInput()
                handle = open(file_input)
            except:
                print('File not found')
                continue
            verifQuotes(handle)
            end = timeNow(datetime.now())
            time_run = end - start
            print(printMessage(start, end, time_run, file_input))

            logs = getLog()
            count = int(logs[0])
            name = logs[1]
            saveLog(str(count), name, start, end, time_run, file_input)
            count +=1
            saveVar(count, name)

        elif options == '5':
            os.system('clear')
        elif options == '6':
            break
        else:
            continue