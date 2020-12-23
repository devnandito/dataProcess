import pandas as pd, json, csv, re, os, sys
from datetime import datetime, timedelta

if __name__ == '__main__':
    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    while True:
        initial = input('Enter options start/quit:')
        initial = initial.lower()
        if initial == 'quit':
            break
        elif initial == 'start':
            file_log = os.path.join(BASE_DIR, 'set/vquerylog.txt')
            f = open(file_log, "r")
            f1 = f.readlines()
            list_log = []
            for x in f1:
                list_log.append(x)
            count = int(list_log[0])
            fname = list_log[1]
            f.close()

            file_open = input('Enter file:')
            file_output = input('Enter file output:')

            handle = open(file_open)
            data = list()
            for line in handle:
                stuff = line.split('\n')
                data.append(stuff[0])
            data_json = list()
            line = 0
            for row in data:
                line +=1
                tmp = row.split(',')
                department = tmp[0].split('[')
                department = department[1].split('"')
                department = department[1]
                district = tmp[1].split('"')
                district = district[1]
                document = tmp[2].split('"')
                document = document[1]
                name = tmp[3].split('"')
                name = name[1]
                lastname = tmp[4].split('"')
                lastname = lastname[0]
                sex = tmp[5].split('"')
                sex = sex[1]
                status = tmp[6].split('"')
                status = status[1]
                date_in = tmp[7].split('"')
                date_in = date_in[1]
                # indi = tmp[8].split(']')
                data_json.append({
                    'department': department,
                    'district': district,
                    'document': document,
                    'fullname': name + lastname,
                    'sex': sex,
                    'status': status,
                    'date_in': date_in,
                    # 'indi': indi[0].split('"')[1]
                })
                # print(department[1], ':', tmp[1], ':', tmp[2], ':', tmp[3], '', tmp[4], ':', tmp[5], ':', tmp[6], ':', tmp[7], ':', indi[0])
            
            ofile = os.path.join(BASE_DIR, 'set/results/'+file_output)
            with open(ofile, 'w+') as outfile:
                json.dump(data_json, outfile, indent=4)

            # for row in data_json[:5]:
            #     print(row['department'], row['district'], row['document'], row['fullname'], row['sex'], row['status'], row['date_in'], row['indi'])
            
            for row in data_json[:50]:
                print(row['fullname'],row['sex'])
            
            print(len(data_json))
            
            now = datetime.now()
            ohour = now.hour
            ominute = now.minute
            osecond = now.second
            end = timedelta(hours=ohour, minutes=ominute, seconds=osecond)
            timerun = end - start
            message = '''
                    Time start: {} \n
                    Runtime: {} \n
                    Time finish: {} \n
                    File: {}
                    '''.format(start, timerun, end, file_output)
            print(message)
            count += 1
            f = open(file_log, 'w')
            f.write(str(count)+'\n')
            f.write(str(list_log[1]))
            f.close()
        else:
            continue
